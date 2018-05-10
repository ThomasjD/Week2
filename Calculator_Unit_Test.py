#Calculator Unit Tests
#Remember the amazing Calculator app you did in Week 1.
#Write the same app but this time using the principles of Test Driven Development.
#Ask the user for input 1
#Ask the user for input 2
#Ask the user for operation (+, -, *, /)

#Create a separate class for Calculator


import unittest
from Calmodule import Calculator



class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        print("SETUP")
        self.calculator = Calculator()

    def test_add(self):
        print("test_add")
        result = self.calculator.calculate(5, '+', 4)
        self.assertEqual(9, result)

    def test_subtract(self):
        print("test_subtract")
        result = self.calculator.calculate(5, '-', 4)
        self.assertEqual(9, result)

    def tearDown(self):
        print("TEAR DOWN")

if __name__ == '__main__':
    unittest.main()

    
