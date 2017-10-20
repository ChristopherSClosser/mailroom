"""Mailroom testing."""
from mock import patch
from unittest import TestCase
import mailroom


class Test(TestCase):
    """Create mock data input for each possibility."""

    @patch('mailroom.mailroom_prompt', return_value='TY')
    def test_prompt_ty(self, input):
        """Test for input TY."""
        self.assertEqual(mailroom.mailroom_prompt(), 'TY')

    @patch('mailroom.mailroom_prompt', return_value='RE')
    def test_prompt_re(self, input):
        """Test for input RE."""
        self.assertEqual(mailroom.mailroom_prompt(), 'RE')

    @patch('mailroom.mailroom_prompt', return_value='Q')
    def test_prompt_q(self, input):
        """Test for input Q."""
        self.assertEqual(mailroom.mailroom_prompt(), 'Q')

    @patch('mailroom.mailroom_prompt', return_value='You must type "TY" for\
thank-you emails,"RE" for a report, or "Q" to quit!')
    def test_prompt_else(self, input):
        """Test for invalid input."""
        self.assertEqual(mailroom.mailroom_prompt(), 'You must type "TY" for\
thank-you emails,"RE" for a report, or "Q" to quit!')
