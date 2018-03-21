#!/usr/bin/env python

import os
import re
import sys

from codecs import open

from setuptools import setup
from setuptools.command.test import test as TestCommand

here = os.path.abspath(os.path.dirname(__file__))


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


packages = ['microformats2']

requires = ['jsl>=0.2.4', 'jsonschema>=2.6.0']
test_requirements = ['pytest>=2.8.0']


setup(
    name='microformats2',
    version='0.1.0',
    description='A package for validating JSON-encoded microformats2 data via JSON Schema.',
    author='Jonathan LaCour',
    email='jonathan@cleverdevil.org',
    url='https://github.com/cleverdevil/microformats2',
    packages=packages,
    package_dir={'microformats2': 'microformats2'},
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=requires,
    zip_safe=False,
    cmdclass={'test': PyTest},
    tests_require=test_requirements,
)
