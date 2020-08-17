"""
python vs java
"""
class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        self._voltage = 12

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, volts):
        print("WARNING: this can cause problems")
        self._voltage = volts

    @voltage.deleter
    def voltage(self):
        print("WARNING: the radio will stop working")
        del self._voltage

class Vehicle:
    def __init__(self, color, model):
        self.color = color
        self.model = model

class Device:
    def __init__(self):
        self._voltage = 12

class Car1(Vehicle, Device):
    def __init__(self, color, model, year):
        Vehicle.__init__(self, color, model)
        Device.__init__(self)
        self.year = year

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, volts):
        print("WARNING: this can cause problems")
        self._voltage = volts

    @voltage.deleter
    def voltage(self):
        print("WARNING: the radio will stop working")
        del self._voltage

    def __str__(self):
        return f'Car {self.color} : {self.model} : {self.year}'
        # return 'Car {} : {} : {}'.format(self.color, self.model, self.year)

    def __repr__(self):
        return 'Car({!r}, {!r}, {!r})'.format(self.color, self.model, self.year)

    def __eq__(self, other):
        return self.year == other.year and self.model == other.model and self.color == other.color

# myCar = Car1("yellow", "Beetle", 1966)
# print(repr(myCar))
# print(str(myCar))

# using the comparison python dunder methods
class Area:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __eq__(self, other):
        if isinstance(other, Area):
            return self.height * self.width == other.height * other.width
        else:
            return False

    def __hash__(self):
        return hash((self.height, self.width))

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if isinstance(other, Area):
            return self.height * self.width < other.height * other.width
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Area):
            return self.height * self.width > other.height * other.width
        else:
            return False

    def __le__(self, other):
        # less-than-or-equal
        if isinstance(other, Area):
            return self.height * self.width <= other.height * other.width
        else:
            return False

    def __ge__(self, other):
        # greater-than-or-equal
        if isinstance(other, Area):
            return self.height * self.width >= other.height * other.width
        else:
            return False

    def __str__(self):
        return 'Height is {} and the width is {}'.format(self.height, self.width)

# testing dunder methods
a1 = Area(7, 10)
a2 = Area(35, 2)
a3 = Area(8, 9)
a4 = Area(8, 9)

# print('Testing ==')
# print(a1 == 'hello')
# print(a1 == a2)
# print(a1 == a3)
# print(a3 == a4)

# testing __eq__ and __hash__ functions
area = Area(7, 10)
area1 = Area(8, 10)
area2 = Area(9, 10)

area_dict = {}
area_dict[area] = 1
area_dict[area1] = 2
area_dict[area2] = 3

# print(area_dict)
for i in area_dict:
    print(i)
