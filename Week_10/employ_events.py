from typing import Callable, Any, Dict, List, Set
import random

class Event:
    """A simple event system to manage subscribers and notify them."""
    def __init__(self):
        self._handlers: List[Callable[..., Any]] = []
    def subscribe(self, handler: Callable[..., Any]) -> None:
        self._handlers.append(handler)
    def unsubscribe(self, handler: Callable[..., Any]) -> None:
        self._handlers.remove(handler)
    def notify(self, *args, **kwargs) -> None:
        for handler in list(self._handlers):
            handler(*args, **kwargs)

class Payroll:
    """A simple payroll system to manage employee names."""
    def __init__(self):
        self._names: Set[str] = set()
    def contains(self, name: str) -> bool:
        return name in self._names
    def add(self, name: str) -> None:
        self._names.add(name)
    def remove(self, name: str) -> None:
        self._names.discard(name)
    def all(self) -> Set[str]:
        return set(self._names)
    
class OrganizationMonitor:
    """Monitors organization events related to hiring."""
    def __init__(self):
        self.on_new_hire = Event()
        self.on_conflict_and_error = Event()
        self.on_rollback = Event()
    
    def hire(self, name: str) -> None:
        context: Dict[str, Any] = {'performed': []}

        self.on_new_hire.notify(name = name, context = context, monitor = self)

# Handler
def payroll_handler(
    name: str,
    context: Dict[str, Any],
    monitor: OrganizationMonitor,
    payroll: Payroll
):
    if payroll.contains(name):
        monitor.on_conflict_and_error.notify(name=name, reason = "already existed", context = context, monitor = monitor)
    else:
        payroll.add(name)
        context['performed'].append(('payroll added', name))
        print('Payroll added for', name)

def paper_handler(
    name: str,
    context: Dict[str, Any],
    monitor: OrganizationMonitor
):
    if ('payroll added', name) in context['performed']:
        context['performed'].append(('paper ordered', name))
        print('Paper ordered for', name)
    else:
        monitor.on_conflict_and_error.notify(name=name, reason = "No payroll added", context = context, monitor = monitor)

def admin_id_request_handler(
    name: str, 
    context: Dict[str, Any],
    monitor: OrganizationMonitor
):
    if ('payroll added', name) in context['performed']:
        requested_id = random.randint(100000, 999999)
        context['performed'].append(('id requested', requested_id))
        print(f'Admin ID {requested_id} requested for', name)
    else:
        monitor.on_conflict_and_error.notify(name = name, reason = 'No payroll added', context = context, monitor = monitor)

def rollback_handler(
    name: str, 
    reason: str, 
    context: Dict[str, Any], 
    monitor: OrganizationMonitor, 
    payroll: Payroll
):
    performed = context.get('performed', [])
    if not performed:
        print(f'No actions to rollback for {name}, reason: {reason}')
        return
    
    for kind, value in reversed(performed):
        if kind == 'payroll added':
            payroll.remove(value)
            print('Rolled back payroll for', value)
        elif kind == 'paper ordered':
            print('Rolled back paper order for', value)
        elif kind == 'id requested':
            print('Rolled back admin ID request for', value)
        else:
            print('Unknown action to rollback:', kind, value)

    context['performed'].clear()
    context['rollback'] = True

    monitor.on_rollback.notify(name = name, reason = reason, context = context, monitor = monitor)
    print(f'Rollback completed for {name}, reason: {reason}')

def wire_up(monitor: OrganizationMonitor, payroll: Payroll) -> None:
    monitor.on_new_hire.subscribe(lambda name, context, monitor: payroll_handler(name, context, monitor, payroll))
    monitor.on_new_hire.subscribe(paper_handler)
    monitor.on_new_hire.subscribe(admin_id_request_handler)
    monitor.on_conflict_and_error.subscribe(lambda name, reason, context, monitor: rollback_handler(name, reason, context, monitor, payroll))

if __name__ == "__main__":
    payroll = Payroll()
    monitor = OrganizationMonitor()
    wire_up(monitor, payroll)

    while True:
        name = input("Enter the name of the new hire (or 'exit' to quit): ")
        if name.lower() == 'exit':
            break
        monitor.hire(name)
        print('Current payroll:', payroll.all())
        print('-' * 30)