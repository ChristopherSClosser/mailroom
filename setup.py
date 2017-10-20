"""Create setup.py."""
# pip install -e
# pip install .
# setup.py

from setuptools import setup

setup(
    name='mailroom',
    description='Creating thank-you emails or printing a report.',
    author='Chris Closser & Brian Wheeler',
    py_modules=['name'],
    install_requires=[],
    extras_require={
        'testing': ['pytest'],
        'development': ['ipython']
    },
    entry_points={
        'console_scripts': [
            'runme=name:main'
        ]
    }
)
