import unittest
from src.ConsoleOutput import ConsoleOutput
from src.Switch import switch

class TestOutput(unittest.TestCase):

    list_of_test_inputs = ["working", "test", "testing"]
    list_of_test_inputs_alt = ["Varied", [1, 3], {"a": [1.2]}]

    console_output = ConsoleOutput()
    switch = switch()


    def test_output(self):
        for string in self.list_of_test_inputs:
            self.console_output.display(string)


    def test_output_alt(self):
        for item in self.list_of_test_inputs_alt:
            self.console_output.display(item)


    def test_show_top_card(self):
        card = ["H3"]
        self.console_output.display(self.switch.show_top_card(card))


    def test_show_top_card_alt(self):
        card = ["SK"]
        self.console_output.display(self.switch.show_top_card(card))
