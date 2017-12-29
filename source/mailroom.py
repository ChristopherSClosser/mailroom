"""Query user to create thank you email or generate a report."""

import sys

if sys.version_info[0] == 2:  # pragma no cover
    input = raw_input


donor_dict = {'name 1': [1.0, 2.0],
              'name 2': [1.0, 2.0, 4.0],
              'name 3': [4.0, 1.0, 2.0], }


def mailroom_prompt():  # pragma: no cover
    """Ask to print a report or send a thank-you.

    Will continue asking until the user types 'Q' to exit.
    """
    # donor_dict = {}
    print("""Welcome to the Mailroom
You can choose to display a report
or to add a new donation and generate a thank-you email.
Type 'Q' to return to the main menu or exit the program.""")
    while True:
        print("""
Available options:
               TY: Write Thank You
               RE: Create Report
                Q: Exit Program""")
        user_choice = user_input_validator(validator_for_main,
                                           ' Choose an option: ')

        if user_choice == 'Q':
            print('Thanks for using Mailroom')
            sys.exit()

        if user_choice == 'TY':
            send_thanks(donor_dict)

        if user_choice == 'RE':
            report(donor_dict)


def report(donor_dict):
    """Print a table of donation stats.

    Includes the donor's name, the total amount donated,
    the number of donations made, and the average
    donation amount.
    """
    list_of_donars = sort_donors(donor_dict)

    print ('Donation Report:\n{0:<20} {1:>10} {2:>4} {3:>8}\n{4}'
           .format('Name', 'Total $', '#', 'Avg $', '-' * 45))

    for donor in list_of_donars:
        total_donated_amount = sum(donor_dict[donor])
        num_donation = len(donor_dict[donor])
        avg_donation = cal_avg_donation(donor_dict[donor])

        print ('{0:<20} {1:>10.2f} {2:>4} {3:>8.2f}'.format(donor,
               total_donated_amount, num_donation, avg_donation))


def sort_donors(donor_dict):
    """Sort the list of donors by total amount donated.
    Returns a list of only the donors' names.
    """
    return sorted(list(donor_dict), key=lambda x: -sum(donor_dict[x]))


def cal_avg_donation(donations):
    """Calculate the average given a list of donations."""
    if not donations:
        return 0
    return sum(donations) / len(donations)


def send_thanks(donor_dict):  # pragma: no cover
    """Ask to print a list of donors or a thank-you email."""
    question = 'Enter a name or type \'list\' for a list of names: '
    name_input = user_input_validator(validator_for_thank_you, question)

    if name_input == 'Q':
        mailroom_prompt()

    if name_input.lower() == 'list':
        if not donor_dict:
            print('No donors recorded.')
        for name in list(donor_dict):
            print(name)
        send_thanks(donor_dict)

    else:
        if name_input not in donor_dict:
            donor_dict[name_input] = []

        donation_input = user_input_validator(validator_for_thank_you_donation,
                                              'Enter a donation amount: ')

        if donation_input == 'Q':
            mailroom_prompt()

        donation_input = float(donation_input)

        donor_dict[name_input].append(donation_input)
        print ('\n' + email_doner(name_input, donation_input))


def email_doner(name, amount):
    """Fill in a form thank-you email for a donation."""
    email_string = """Thank you {0} for your donation of {1} goofy goober dollars.""".format(name, amount)
    return email_string


def user_input_validator(validator, question):  # pragma: no cover
    """Validate a user input until it passes a validator function.

    validator: function, test for user input. Returns a truthy
               value for a valid input, falsey for invalid.
    question: str, prompt for user to answer
    """
    user_input = input(question).upper()

    while not validator(user_input) and user_input.upper() != 'Q':
        print('Invalid user input, input again\n')
        user_input = input(question).upper()
    return user_input


def validator_for_main(user_input):  # pragma no cover
    """Check that input is 'TY' or 'RE'."""
    if user_input == 'Q':
        sys.exit()
    return user_input == 'TY' or user_input == 'RE'


def validator_for_thank_you(name_input):  # pragma no cover
    """Check that input is made only of letters and spaces."""
    if not name_input:
        return False
    return True


def validator_for_thank_you_donation(donation_input):
    """Check that input can be a ."""
    try:
        float(donation_input)
        return True
    except ValueError:
        return False


if __name__ == '__main__':  # pragma no cover
    mailroom_prompt()
