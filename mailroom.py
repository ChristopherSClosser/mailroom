"""."""

import sys
# import easygui
doners = {'name': ['$', '$']}


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
    mailroom_prompt()
    return email


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
        # report()
    elif choice == 'Q':
        print(choice)
        sys.exit()
    else:
        return('You must type "TY" for thank-you emails,\
"RE" for a report, or "Q" to quit!')
        mailroom_prompt()


mailroom_prompt()
