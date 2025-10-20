class Car:
    """
    Represents a car with basic attributes and behaviors.
    """

    def __init__(
        self,
        make: str,
        model: str,
        color: str,
        yearBuilt: int
        ):
        """
        Initializes a Car object.

        Args:
            make (str): The manufacturer of the car.
            model (str): The model of the car.
            color (str): The color of the car.
            yearBuilt (int): The year the car was built.
        """
        self.make = make
        self.model = model
        self.color = color
        self.yearBuilt = yearBuilt

    def start(self):
        """
        Starts the car.
        """
        print(f"The {self.model} is started.")

    def stop(self):
        """
        Stops the car.
        """
        print(f"The {self.model} is stopped.")
    
    def display_info(self):
        """
        Displays information about the car.
        """
        print(f"Car Info:")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Year Built: {self.yearBuilt}")

    class Engine:
        """
        Represents a car engine with specific attributes and behaviors.
        """

        def __init__(self, horsepower: int, cylinders: int):
            """
            Initializes an Engine object.

            Args:
                horsepower (int): The horsepower of the engine.
                cylinders (int): The number of cylinders in the engine.
            """
            self.horsepower = horsepower
            self.cylinders = cylinders

        def start(self):
            """
            Starts the engine.
            """
            print("The engine is started.")

        def stop(self):
            """
            Stops the engine.
            """
            print("The engine is stopped.")
        
        def display_specs(self):
            """
            Displays specifications of the engine.
            """
            print(f"Engine Specs:")
            print(f"Horsepower: {self.horsepower}")
            print(f"Cylinders: {self.cylinders}")

    
if __name__ == "__main__":

    make = input("Enter car make: ")
    model = input("Enter car model: ")
    color = input("Enter car color: ")
    yearBuilt = int(input("Enter year built: "))
    print("--------------------------------")
    car = Car(make, model, color, yearBuilt)
    car.display_info()
    car.start()
    car.stop()

    print("--------------------------------")
    horsepower = int(input("Enter engine horsepower: "))
    cylinders = int(input("Enter number of engine cylinders: "))
    print("--------------------------------")
    engine = Car.Engine(horsepower, cylinders)
    engine.display_specs()
    engine.start()
    engine.stop()
    print("Exiting program.")

        