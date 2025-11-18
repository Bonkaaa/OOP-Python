from typing import List

def GreaterCount(lst: List[float], min: float):
    count = 0
    for item in lst:
        if item >= min:
            count += 1
    return count

def main():
    temperatures: List[float] = []

    temperatures.extend([22.5, 25.0, 27.3, 19.8, 25.0, 30.0, 24.9])

    count_element = 0

    for t in temperatures:
        if t >= 25.0:
            count_element += 1
    
    print("Temperatures:", temperatures)
    print("Count using foreach loop (>= 25):", count_element)

    count_method = GreaterCount(temperatures, 25.0)
    print("Count using GreaterCount function (>= 25):", count_method)

if __name__ == "__main__":
    main()

    