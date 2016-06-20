import codecs
import os

from setuptools import setup
from setuptools import find_packages


VERSION = (0, 0, 7)
SEPARATOR = '.'


def get_version():
    return SEPARATOR.join(map(lambda x: str(x), VERSION))

__version__ = get_version()


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


#: LONG_DESCRIPTION = parse('README.rst')

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Communications",
    "Topic :: Internet",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
]


setup(
    name='ffire',
    description='GUI Style Events for Web Applications',
    url='http://github.com/ffireio/ffire-python',
    version=__version__,
    license='MIT',
    author='Raymond Ortserga',
    author_email='r.ortserga@fetchr.us',
    zip_safe=False,
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=['validators', 'requests'],
    keywords='Events Publish Subscribe Fire Raise Web API',
    classifiers=CLASSIFIERS,
    long_description=""
)
