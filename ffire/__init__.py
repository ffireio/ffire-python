"""
Ffire is the GUI style event library for web applications.

ffire
~~~~~

Creating and firing events should be as easy as creating and firing events. No hurdles or curves necessary.
"""
from ffire.core.fire import Fire


ffire = Fire()

__all__ = ['ffire']


VERSION = (0, 0, 1)
SEPARATOR = '.'


def get_version():
    return SEPARATOR.join(map(lambda x: str(x), VERSION))

__version__ = get_version()
