"""Create setup.py."""


from setuptools import setup

setup(
    name='mailroom',
    package_dir={"": 'source'},
    description='Creating thank-you emails or printing a report.',
    author='Chris Closser & Brian Wheeler',
    py_modules=['mailroom'],
    extras_require={
        'testing': ['pytest', 'mock'],
        'development': ['ipython']
    },
    entry_points={
        'console_scripts': [
            'mailroom = mailroom:mailroom_prompt'
        ]
    }
)
