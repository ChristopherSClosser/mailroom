"""."""

import sys

doners = {'name 1': [1, 2], 'name 2': [1, 2, 4], 'name 3': [4, 1, 2], }


def send_thanks():
    """."""
    full_name = input('Enter full name: ')
    if full_name == '':
        print('Try again')
        send_thanks()
    if full_name in doners:
        new_donation = donation_amount()
        doners[full_name].append(new_donation)
        email_doner(full_name, new_donation)
    else:
        doners[full_name] = []
        new_donation = donation_amount()
        doners[full_name].append(new_donation)
        email_doner(full_name, new_donation)
    return email_doner


def email_doner(name, donation):
    """Print the email."""
    email = 'Thank you %s for your donation of %s goofy goober\
 dollars.' % (name, donation)
    if __name__ == "__main__":
        """."""
        print(email)
        mailroom_prompt()

    return email


def report():
    for i in doners:
        rep = ''
        total = sum(doners[i])
        rep += 'Doner: %s Donations: %s\nTotal Donations: %i' % (i, doners[i], total)
    print(rep)
    return rep


def donation_amount():
    """."""
    donation = input('Enter donation amount: ')
    if not int(donation):
        print('You must enter a integer')
        donation_amount()
    return donation


def mailroom_prompt():
    """Active prompt for send_thanks or report."""
    choice = input('Type "TY" for thank-you emails,\
"RE" for a report, or "Q" to quit.').upper()
    if choice == 'TY':
        print(choice)
        send_thanks()
    elif choice == 'RE':
        print(choice)
        report()
    elif choice == 'Q':
        print(choice)
        sys.exit()
    else:
        return('You must type "TY" for thank-you emails,\
"RE" for a report, or "Q" to quit!')
        mailroom_prompt()


if __name__ == "__main__":
    """."""
    mailroom_prompt()
