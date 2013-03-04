import os, re
from setuptools import setup, find_packages

def _read_contents(fn):
    here = os.path.dirname( os.path.realpath(__file__) )
    filename = os.path.join(here, fn)
    with open(filename) as file:
        return file.read()

version = re.findall(r'__version__ = "(.*?)"', _read_contents("sharc/__init__.py"))[0]

setup(
    name='sharc',
    version=version,
    description="Sharded Counters for Google Appengine (GAE).",
    long_description=_read_contents('README.rst'),
    author="herr kaste",
    author_email="herr.kaste@gmail.com",
    license="Apache 2",
    url='http://github.com/kaste/sharc',
    download_url='http://github.com/kaste/sharc/tarball/master#egg=sharc-dev',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    tests_require=['pytest'],
    keywords="google appengine gae sharded counter ndb ",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        ],
)


