# Introducing the concept of @dataclass
# Automatically generates __init__,
# __repr__, __eq__ etcs

import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''
    Generate a random string of 15 lower_case characters
    '''

    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    '''
    A student class that was decorated by dataclass.
    __init__, __repr__, __eq__ etc has been auto generated.
    '''
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        '''
        An instance of dataclass will automatically call
        __post__init__ after __init__ was called
        '''
        self.login = self.name[0] + self.surname
