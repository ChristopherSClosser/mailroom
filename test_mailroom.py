"""Mailroom testing."""
from unittest.mock import patch
from unittest import TestCase
from mailroom import prompt


def get_input(text):
    return input(text)


class Test(TestCase):

    @patch('prompt.get_input', return_value='TY')
    def test_prompt_ty(self, input):
        """."""
        self.assertEqual(prompt(), 'TY')

    @patch('prompt.get_input', return_value='RE')
    def test_prompt_re(self, input):
        """."""
        self.assertEqual(prompt(), 'RE')

    @patch('prompt.get_input', return_value='Q')
    def test_prompt_q(self, input):
        """."""
        self.assertEqual(prompt(), 'Q')
