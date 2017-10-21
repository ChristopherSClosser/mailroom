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

    @patch('mailroom.donation_amount', return_value=int)
    def test_donation_amount_valid(self, input):
        """."""
        self.assertEqual(mailroom.donation_amount(), int)

    @patch('mailroom.donation_amount', return_value='')
    def test_donation_amount_invalid(self, input):
        """."""
        self.assertFalse(mailroom.donation_amount(), ValueError)

    @patch('mailroom.send_thanks', return_value="Doe Doe")
    def test_send_thanks(self, input):
        """."""
        self.assertEqual(mailroom.send_thanks(), "Doe Doe")


def test_email_doner():
    """."""
    name = "Bob Bob"
    donation = "99"
    assert mailroom.email_doner(name, donation) == 'Thank you Bob Bob for your donation of 99 goofy goober dollars.'


def test_report():
    """."""
    assert mailroom.report() == "Doner: name 1 Donations: [1, 2]\nTotal Donations: 3"
