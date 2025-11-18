from typing import Iterable, Any

def greater_count(iter: Iterable[Any], min: float):
    if iter is None:
        return 0
    
    count = 0
    for item in iter:
        try: 
            value = float(item)
        except (TypeError, ValueError):
            continue

        if value >= min:
            count += 1

    return count

def main():
    temperatures = [22.5, 25.0, 27.3, 19.8, 25.0, 30.0, 24.9]

    res = greater_count(temperatures, 25.0)

    print("Temperatures: ", temperatures)
    print("Number of temperatures >= 25.0:", res)

if __name__ == "__main__":
    main()