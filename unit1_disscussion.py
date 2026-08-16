"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    category = "Smart Device"

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display_info(self):
        return f"{self.name} is a {self.category} located in the {self.location}."


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    device_type = "Smart Thermostat"

    def __init__(self, name, location, temperature, schedule):
        super().__init__(name, location)
        self.temperature = temperature
        self.schedule = schedule

    def set_temperature(self, temperature):
        self.temperature = temperature
        return f"{self.name} temperature was set to {self.temperature} degrees."

    def display_info(self):
        return (
            f"{self.name} is a {self.device_type} located in the {self.location}. "
            f"Current temperature: {self.temperature} degrees. "
            f"Schedule: {self.schedule}."
        )


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    thermostat1 = ChildClass("Thermostat A", "Living Room", 72, ["7:00 AM - 70", "6:00 PM - 72"])
    thermostat2 = ChildClass("Thermostat B", "Bedroom", 68, ["10:00 PM - 68"])

    print("Class variable through class:", ChildClass.device_type)
    print("Class variable through object:", thermostat1.device_type)

    # This attribute belongs only to thermostat1's instance namespace.
    thermostat1.energy_saver = True

    print("Thermostat 1 namespace:", thermostat1.__dict__)
    print("Thermostat 2 namespace:", thermostat2.__dict__)
    print("ChildClass namespace:", ChildClass.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = ChildClass(
        "Main Thermostat",
        "Hallway",
        71,
        ["6:00 AM - 70", "9:00 PM - 68"]
    )

    shallow_copy = copy(original)
    deep_copy = deepcopy(original)

    # A shallow copy creates a new outer object but still references nested
    # mutable objects, so a change to the original list also appears here.
    # A deep copy recursively copies nested data, so its list stays independent.
    original.schedule.append("11:00 PM - 66")

    print("Original schedule:", original.schedule)
    print("Shallow copy schedule:", shallow_copy.schedule)
    print("Deep copy schedule:", deep_copy.schedule)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")
    parent_device = ParentClass("Home Hub", "Office")
    print(parent_device.display_info())

    print("\nTODO: Create and test your child object")
    thermostat = ChildClass(
        "Downstairs Thermostat",
        "Living Room",
        72,
        ["7:00 AM - 70", "6:00 PM - 72"]
    )
    print(thermostat.display_info())
    print(thermostat.set_temperature(69))

    demonstrate_namespaces()
    demonstrate_copying()

    # Student-created extension:
    # Check whether the thermostat is within a normal home temperature range.
    print("\n=== Student-Created Extension ===")
    if 60 <= thermostat.temperature <= 80:
        print(f"{thermostat.name} is within the normal temperature range.")
    else:
        print(f"Warning: {thermostat.name} is outside the normal temperature range.")


if __name__ == "__main__":
    main()