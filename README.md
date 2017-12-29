# mailroom
---
### Description
[![Build Status](https://travis-ci.org/ChristopherSClosser/mailroom.svg?branch=master)](https://travis-ci.org/ChristopherSClosser/mailroom) [![Coverage Status](https://coveralls.io/repos/github/ChristopherSClosser/mailroom/badge.svg)](https://coveralls.io/github/ChristopherSClosser/mailroom)

Version: 1.0

Creating thank-you emails or printing a report.
* Feature #1
* Feature #2
* Feature #3

### Authors
---
* [Chris Closser & Brian Wheeler](https://github.com/ChristopherSClosser/mailroom)

### Getting Started
---
##### *Prerequisites*
* python 2.7
* [python (3.6+)](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/)
* [git](https://git-scm.com/)

##### *Installation*
First, clone the project repo from Github. Then, change directories into the cloned repository. To accomplish this, execute these commands:

`$ git clone https://github.com/ChristopherSClosser/mailroom.git`

`$ cd mailroom`

Now now that you have cloned your repo and changed directories into the project, create a virtual environment named "ENV", and install the project requirements into your VE.

`$ python3 -m venv ENV`

`$ source ENV/bin/activate`

`$ pip install -e .`

`$ mailroom`

<pre>Welcome to the Mailroom
You can choose to display a report
or to add a new donation and generate a thank-you email.
Type 'Q' to return to the main menu or exit the program.

<pre>Available options:
               TY: Write Thank You
               RE: Create Report
                Q: Exit Program
 Choose an option:

### Test Suite
---
##### *Running Tests*
This application uses [pytest](https://docs.pytest.org/en/latest/) as a testing suite. To run tests, run:

``$ pytest``

To view test coverage, run:

``$ pytest --cov``
##### *Test Files*
The testing files for this project are:

| File Name | Description |
|:---:|:---:|
| `./source/test_mailroom.py` | Mailroom testing. |

### Development Tools
---
* *python* - programming language

### License
---
This project is licensed under MIT License - see the LICENSE.md file for details.
### Acknowledgements
---
* Coffee
* Trial and error

*This README was generated using [writeme.](https://github.com/chelseadole/write-me)*
