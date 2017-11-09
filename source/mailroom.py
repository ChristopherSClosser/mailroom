"""Query user to create thank you email or generate a report."""

import sys

if sys.version_info[0] == 2:
    input = raw_input

doners = {'name 1': [1, 2], 'name 2': [1, 2, 4], 'name 3': [4, 1, 2], }


def send_thanks():
    """Take donor name and adds it to dict if needed."""
    full_name = input('Enter full name: ')
    if full_name == '':
        print('Try again')
        send_thanks()

    '''
    doners.setdefault(full_name, [])
    new_donation = donation_amount()
    doners[full_name].append(new_donation)
    return email_doner(full_name, new_donation)
    '''
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
        """Avoid IO error."""
        print(email)
        mailroom_prompt()

    return email


def report():
    """Create report of donors and their donations and total."""
    rep = ''
    for i in doners:
        total = sum(doners[i])
        rep += ('          Doner: {0}\n\
      Donations: {1}\n\
Total Donations: {2}\n\n'.format(i, doners[i], total))
    print(rep)
    mailroom_prompt()
    return rep


def donation_amount():
    """Add donation to donor."""
    donation = input('Enter donation amount: ')
    try:
        return float(donation)
    except ValueError:
        print('You must enter a integer')
        donation_amount()


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
    """Avoid IO error."""
    mailroom_prompt()
