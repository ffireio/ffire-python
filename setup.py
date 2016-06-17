import codecs
import os

from setuptools import setup
from setuptools import find_packages

import ffire


def parse(*args, **kwargs):
    """Parse documentation files into internal variable for rendering with setup
    """
    # noinspection PyPep8Naming
    SEPARATOR = kwargs.get('separator', '\n')
    coding = kwargs.get('coding', 'UTF-8')
    stream = []

    for arg in args:
        with codecs.open(arg, 'r', coding) as document:
            stream.append(document.read())

    return SEPARATOR.join(stream)


LONG_DESCRIPTION = parse('README.rst')

CLASSIFIERS = [
    'Development Status :: Alpha - 1',
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: Implementation :: CPython",
    'Topic :: Events',
    'Topic :: Software :: Engineering :: Development :: Libraries :: Python Modules',
]


setup(
    name='ffire',
    description='GUI Style Events for Web Applications',
    url='http://github.com/rayattack/ffire',
    version=ffire.__version__,
    license='MIT',
    author='Raymond Ortserga',
    author_email='r.ortserga@fetchr.us',
    zip_safe=False,
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=['pika', 'boto3'],
    keywords='Events Publish Subscribe Fire Raise Web API',
    classifiers=CLASSIFIERS,
    long_description=LONG_DESCRIPTION
)
