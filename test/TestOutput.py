import unittest
from src.ConsoleOutput import ConsoleOutput

class TestOutput(unittest.TestCase):

    list_of_test_inputs = ["working", "test", "testing"]
    console_output = ConsoleOutput()


    def test_output(self):
        for string in self.list_of_test_inputs:
            self.console_output.display(string)
