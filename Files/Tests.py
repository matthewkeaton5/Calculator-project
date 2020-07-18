import unittest
from Files import CSV
from Files import Calculator

class tests(unittest.TestCase):
    def setup(self):
        self.calc = Calculator()

    def result(self):
        self.assertEqual(self.calc.solution,0)

    def testIsInstance(self):
        self.assertIsInstance(self.calc, Calculator)

    def add(self):
        addCSV = CSV("Files/Unit Test Addition.csv").csv_data
        for x in addCSV:
            self.assertEqual(self.calc.add(x["Value 1"], x["Value 2"]), x["Solution"])
            self.assertEqual(self.calc.solution, x["Solution"])

    def sub(self):
        subCSV = CSV("Files/Unit Test Subtraction.csv").csv_data
        for x in subCSV:
            self.assertEqual(self.calc.subtract(x["Value 1"], x["Value 2"]), x["Solution"])
            self.assertEqual(self.calc.solution, x["Solution"])

    def mult(self):
        multCSV = CSV("Files/Unit Test Multiplication.csv").csv_data
        for x in multCSV:
            self.assertEqual(self.calc.multiple(x["Value 1"], x["Value 2"]), x["Solution"])
            self.assertEqual(self.calc.solution, x["Solution"])

    def div(self):
        divCSV = CSV("Files/Unit Test Division.csv").csv_data
        for x in divCSV:
            self.assertEqual(self.calc.divide(x["Value 1"], x["Value 2"]), x["Solution"])
            self.assertEqual(self.calc.solution, x["Solution"])

    def square(self):
        squareCSV = CSV("Files/Unit Test Square.csv").csv_data
        for x in squareCSV:
            self.assertEqual(self.calc.squaring(x["Value 1"], x["Value 2"]), x["Solution"])
            self.assertEqual(self.calc.solution, x["Solution"])

    def root(self):
        rootCSV = CSV("Files/Unit Test Square Root.csv").csv_data
        for x in rootCSV:
            self.assertEqual(self.calc.squarerooting(x["Value 1"], x["Value 2"]), x["Solution"])
            self.assertEqual(self.calc.solution, x["Solution"])

    if __name__ == "__main__":
        unittest.main()