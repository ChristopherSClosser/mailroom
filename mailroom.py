"""."""

import sys
# import easygui
doners = {'name': ['$', '$']}


def send_thanks():
    """."""
    full_name = input('Enter full name')
    if full_name in doners:
        new_donation = donation_amount()
        doners[full_name].append(new_donation)
        email_doner = 'thank you'
    else:
        doners[full_name] = []
        new_donation = donation_amount()
        doners[full_name].append(new_donation)
        email_doner = 'thank you'
    print(email_doner)


def donation_amount():
    donation = input('Enter donation amount.')
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
