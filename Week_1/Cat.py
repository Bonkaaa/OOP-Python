class Cat:
    """
    A class to represent a cat.
    """
    __instances = 0
    def __init__(self, weight: int, name: str):
        """
        Initializes a Cat object.
        Args:
            weight (int): The weight of the cat in kg.
            name (str): The name of the cat.
        """
        self.__name = name
        self.__weight = weight

        Cat.__instances += 1
    
    @staticmethod
    def HowManyCats():
        """
        Displays the number of Cat instances created.
        """
        print(f"{Cat.__instances} cats adopted")
    
    def TellWeight(self):
        """
        Displays the weight of the cat.
        """
        print(f"{self.__name} weighs {self.__weight} kg")

if __name__ == "__main__":
    Cat.HowManyCats()
    print("----------------------------")
    name = input("Enter cat's name: ")
    weight = int(input("Enter cat's weight (kg): "))
    print("----------------------------")
    cat1 = Cat(weight, name)
    cat1.TellWeight()
    print("----------------------------")
    Cat.HowManyCats()
    print("----------------------------")
    name = input("Enter cat's name: ")
    weight = int(input("Enter cat's weight (kg): "))
    print("----------------------------")
    cat2 = Cat(weight, name)
    cat2.TellWeight()
    print("----------------------------")
    Cat.HowManyCats()
    print("Exiting program.")
