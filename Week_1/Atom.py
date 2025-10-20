class Atom:
    def __init__(self):
        """
        Initializes an Atom object.

        Args:
            number (int): The atomic number of the atom.
            symbol (str): The chemical symbol of the atom.
            name (str): The name of the atom.
            atomic_mass (float): The atomic mass of the atom.
        """
        self.number = 0
        self.symbol = ""
        self.name = ""
        self.atomic_mass = 0.0

    def accept(self):
        """
        Accepts user input to set the attributes of the Atom object.
        Returns:
            bool: True if input was accepted, False if the user chose to exit.
        """
        # Accept atomic number
        while True:
            try: 
                self.number = int(input("Enter atomic number: "))
                if self.number == 0:
                    return False
                if self.number > 0:
                    break
                else:
                    print("Atomic number must be a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        # Accept symbol
        while True:
            self.symbol = input("Enter symbol: ").strip()
            if self.symbol:
                break
            print("Invalid input. Symbol cannot be empty.")

        # Accept name
        while True:
            self.name = input("Enter name: ").strip()
            if self.name:
                break
            print("Invalid input. Name cannot be empty.")

        # Accept atomic mass:
        while True:
            try: 
                self.atomic_mass = float(input("Enter atomic weight: "))
                if self.atomic_mass > 0:
                    break
                else:
                    print("Atomic weight must be a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        return True
    
    def display(self):
        """
        Displays the attributes of the Atom object in a formatted manner.
        """
        print(f"{self.number:<5} {self.symbol:<5} {self.name:<10} {self.atomic_mass:<10.3f}")

if __name__ == "__main__":
    atoms = []
    print("Atomic Information")
    print("===================")

    for _ in range(10):
        atom = Atom()
        if not atom.accept():
            break
        atoms.append(atom)
        print("--------------------------------")

    print("\nNo   Sym  Name       Weight")
    print("------------------------------------")

    for atom in atoms:
        atom.display()




        