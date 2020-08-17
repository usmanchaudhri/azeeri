"""

"""
import enum

class Animal(enum.Enum):
    dog = 1
    cat = 2
    lion = 3

print('The string representation of enum member is: ', end=" ")
print(Animal.dog)

print('The repr representation of enum member is: ', end=" ")
print(repr(Animal.dog))

print('The type of enum member is: ', end=" ")
print(type(Animal.dog))

print('The name and value of enum member is: ', end=" ")
print(Animal.dog.name, Animal.dog.value)

print('All the enum values are: ', end=" ")
for anim in Animal:
    print(anim)

print('Access Animal Enum by value', Animal(2))
print('Access Animal Enum by name', Animal['lion'])

