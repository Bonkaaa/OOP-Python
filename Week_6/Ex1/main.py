# 20237451 - Nguyen Huu Kien
from Circle import Circle

def main():
    try:
        radius = float(input("Enter radius value: "))
        color = input("Enter color: ")
        weight = float(input("Enter weight's object: "))

        if not radius or not color or not weight:
            raise ValueError("All inputs must be provided and valid.")

        circle = Circle(radius, color, weight)
        circle.toString()
    except ValueError as ve:
        raise ve
    
if __name__ == "__main__":
    print("20237451 - Nguyen Huu Kien")
    print("----------------------------")
    main()
