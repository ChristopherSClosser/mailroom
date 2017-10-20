"""."""

import sys
# doners = {'name': ['$', '$']}
#
#
# def send_thanks(full_name):
#     full_name = input('Enter full name')
#     new_donation = int(input())
#     doners[full_name] = new_donation
#     email_doner = 'thank you'
#     print email_doner
#     send_thanks()
#
#
# def report():
#     print(doners.keys())


def prompt():
    """Active prompt for send_thanks or report."""
    choice = input('Type "TY" for thank-you emails,\
    "RE" for a report, or "Q" to quit.').upper()
    if choice == 'TY':
        print(choice)
        # send_thanks()
    elif choice == 'RE':
        print(choice)
        # report()
    elif choice == 'Q':
        print(choice)
        sys.exit()
    else:
        print('You must type "TY" for thank-you emails,\
        "RE" for a report, or "Q" to quit!')
        prompt()
