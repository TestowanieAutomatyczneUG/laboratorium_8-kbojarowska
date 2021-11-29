import unittest
from sample.FizzBuzz import *
from parameterized import parameterized, parameterized_class
import math

class FizzBuzzParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = FizzBuzz()

    @parameterized.expand([
        (5, "Buzz"),
        (3, "Fizz"),
        (15, "FizzBuzz"),
        (10, "Buzz"),
        (9, "Fizz"),
        (45, "FizzBuzz"),
        (-5, "Buzz"),
        (-3, "Fizz"),
        (-15, "FizzBuzz"),
        (-10, "Buzz"),
        (-9, "Fizz"),
        (-45, "FizzBuzz"),
        (538175, "Buzz"),
        (33333333333333, "Fizz"),
        (555555555555, "FizzBuzz"),
        (-538175, "Buzz"),
        (-33333333333333, "Fizz"),
        (-555555555555, "FizzBuzz"),
        (7, "7"),
        (43, "43"),
        (-24341, "-24341")

    ])
    def test_one_parameterized(self,number, expected):
        self.assertEqual(self.tmp.game(number), expected)

    @parameterized.expand([
        ("3"),
        ("5"),
        ("45"),
        ("-6"),
        ("-10"),
        ("-15"),
        (""),
        ([],),
        (["5"]),
        ([5],),
        ([2,5,3,2],),
        ({},),
        ({1:4},),
        ((),),
        ((1,3),),
        ("str"),
        ("Liczby dużo"),
        (5+2j,),
        (-4-1j,),
    ])
    def test_exception_parameterized(self, data):
        self.assertRaises(Exception, self.tmp.game, data)

@parameterized_class(('number', 'expected'), [
        (5, "Buzz"),
        (3, "Fizz"),
        (15, "FizzBuzz"),
        (10, "Buzz"),
        (9, "Fizz"),
        (45, "FizzBuzz"),
        (-5, "Buzz"),
        (-3, "Fizz"),
        (-15, "FizzBuzz"),
        (-10, "Buzz"),
        (-9, "Fizz"),
        (-45, "FizzBuzz"),
        (538175, "Buzz"),
        (33333333333333, "Fizz"),
        (555555555555, "FizzBuzz"),
        (-538175, "Buzz"),
        (-33333333333333, "Fizz"),
        (-555555555555, "FizzBuzz"),
])

class FizzBuzzParameterizedPackage2(unittest.TestCase):
    def setUp(self):
        self.tmp = FizzBuzz()

    def test_second_parameterized(self):
        self.assertEqual(self.tmp.game(self.number), self.expected)

@parameterized_class(('data'),[
    ("3"),
    ("5"),
    ("45"),
    ("-6"),
    ("-10"),
    ("-15"),
    ("",),
    ([],),
    (["5"]),
    ([5],),
    ([2,5,3,2],),
    ({},),
    ({1:4},),
    ((),),
    ((1,3),),
    ("str"),
    ("Liczby dużo"),
    (5+2j,),
    (-4-1j,),
])
class FizzBuzzParameterizedPackage3(unittest.TestCase):
    def setUp(self):
        self.tmp = FizzBuzz()

    def test_exception_parametrized_two(self):
        self.assertRaises(Exception, self.tmp.game, self.data)


if __name__ == '__main__':
    unittest.main()
