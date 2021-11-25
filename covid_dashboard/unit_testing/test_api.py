import pytest
from api.util import *

def test_find_US():
    if Find_Country("US") == 1:
        print("LOL")
    #assert Find_Country("US") == 1

# def func(x):
#     return x+1

# def test():
#     assert func(3) == 5