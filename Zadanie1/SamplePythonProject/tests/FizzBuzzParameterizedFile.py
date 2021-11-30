import unittest
from sample.FizzBuzz import *

class FizzBuzzParameterizedFile(unittest.TestCase):

    def test_from_file(self):
        fileTest = open("data/fizz_buzz_data_test")
        tmpFizzBuzz = FizzBuzz()
        for line in fileTest:
            data = line.split(" ")
            inp, result = int(data[0]), data[1].strip("\n")
            self.assertEqual(tmpFizzBuzz.game(inp), result)
        fileTest.close()

    def test_from_file_exception(self):
        fileTest = open("data/fizz_buzz_data_test_exception")
        tmpFizzBuzz = FizzBuzz()
        for line in fileTest:
            test = line.strip("\n")
            self.assertRaises(Exception, tmpFizzBuzz.game, test)
        fileTest.close()


if __name__ == '__main__':
    unittest.main()
