"""Mailroom testing."""
from unittest.mock import patch
from unittest import TestCase
import mailroom
from faker import Faker
import pytest
from random import uniform, randint


fake = Faker()
fake_donors = {
    fake.name(): [uniform(0, 1000) for _ in range(randint(1, 10))]
    for _ in range(20)
}
small_donors = {
    'Jim Bob': [270.36, 609.35, 170.10],
    'Johny Walker': [70.13, 483.50, 29.23, 117.34, 594.88, 425.31, 730.61]
}


@pytest.mark.parametrize('donor_dictionary', [small_donors, fake_donors])
def test_generate_report(donor_dictionary):
    """Test that user_input does not raise any exceptions."""
    from mailroom import report
    report(donor_dictionary)


@pytest.mark.parametrize('donations, result', [([], 0), ([2, 6], 4)])
def test_cal_avg_donation(donations, result):
    """Test cal_avg_donation for proper output."""
    from mailroom import cal_avg_donation
    assert cal_avg_donation(donations) == result


@pytest.mark.parametrize('donor_dictionary, result',
                         [(small_donors, ['Johny Walker', 'Jim Bob'])])
def test_sort_donors(donor_dictionary, result):
    """Test sort_donors for proper output."""
    from mailroom import sort_donors
    assert sort_donors(donor_dictionary) == result
    

@pytest.mark.parametrize('user_input, result', [('100.22336', True),
                         ('20', True), ('', False), ('letter', False),
                         ('***', False)])
def test_validator_thank_you_donation(user_input, result):
    """Test validator_for_thank_you_donation for proper output."""
    from mailroom import validator_for_thank_you_donation
    assert validator_for_thank_you_donation(user_input) == result


@pytest.mark.parametrize('name, amount, result', [('John', 20000, """Thank you John
                                                    for your donation of 20000
                                                    goofy goober dollars.""")])
def test_email_doner(name, amount, result):
    """Test email_donor for proper output."""
    from mailroom import email_doner
    assert email_doner(name, amount) == result


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

    @patch('mailroom.send_thanks', return_value="Doe Doe")
    def test_send_thanks(self, input):
        """Test for name input."""
        self.assertEqual(mailroom.send_thanks(), "Doe Doe")


def test_email_doner():
    """Test that email is assembled properly."""
    name = "Bob Bob"
    donation = 99
    assert mailroom.email_doner(name, donation) == 'Thank you Bob Bob for your donation of 99 goofy goober dollars.'
