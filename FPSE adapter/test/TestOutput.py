import unittest
from src.ConsoleOutput import ConsoleOutput

class TestOutput(unittest.TestCase):

    list_of_test_inputs = ["working", "test", "testing"]
    console_output = ConsoleOutput()


    def test_output(self):
        for input in self.list_of_test_inputs:
            self.console_output.display(input)


if __name__ == "__main__":
    TestOutput = TestOutput()
    TestOutput.test_output()