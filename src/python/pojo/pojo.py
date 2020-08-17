"""

"""
def concatenate(**kwargs):
    result = ""
    # iterating over the Python kwargs dictionary
    for args in kwargs.values():
        result +=args
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

class User:
    def __init__(self, name: str, village: str) -> None:
        self.name = name
        self.village = village

from typing import Any, Dict
from collections import OrderedDict

def user_from_dict(s: Dict[str, Any]) -> User:
    return User(**s)

def user_to_dict(x: User) -> Dict[str, any]:
    return vars(x)

data = {"name": "Uzumaki Naruto", "village": "Leaf Village"}
usr = user_from_dict(data)
print(usr.name)
usr_dict = user_to_dict(usr)
print(usr_dict["village"])

dictionary = OrderedDict()
dictionary['a'] = 1
dictionary['b'] = 1
dictionary['c'] = 1

print(dictionary)
print(dictionary.move_to_end('a'))
print(dictionary)





