from src.Switch import switch
from src.TestInput import TestInput
import unittest

class TestSwitch(unittest.TestCase):

    switch = switch()
    test_input = TestInput()


    deck = ['H8', 'D3','D4', 'D5', 'D6', 'D7', 'D8', 'D9',
            'D10', 'DJ', 'DQ', 'DK', 'SA', 'S2', 'S3', 'S4',
            'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ',
            'SK', 'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7',
            'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK']


    def set_up(self):
        self.switch.set_game_input(self.test_input)


    def test_switch(self):  #CPU wins
        hands = [['HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7'],['H9', 'H10', 'HJ', 'HQ', 'HK']]
        self.test_input.set_list_of_test_inputs(['HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7'])
        self.switch.play_switch(self.deck, hands)


    def test_can_play(self):
        hand = ["H3","J2","C2"]
        target = ["J8"]
        self.assertTrue(self.switch.can_play(hand, target))


    def test_can_play_card(self):
        card = "C8"
        target = ["C7"]
        self.assertTrue(self.switch.can_play_card(card, target))


    def test_computer_valid_cards(self):
        hand = ["H2","C8","C9","D5"]
        target = ["D8"]
        self.assertEqual(["C8","D5"], self.switch.computer_valid_cards(hand, target))