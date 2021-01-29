# -*- coding: utf-8 -*-

from setuptools import setup

from pynepcord import __version__
from pynepcord import __license__
from pynepcord import __author__


with open('README.md') as f:
  readme = f.read()

with open('requirements.txt') as f:
  requirements = f.read().splitlines()


setup(name='pynepcord',
      author=__author__,
      url='https://github.com/NellyD3v/pynepcord',
      version=__version__,
      packages=('pynepcord', 'pynepcord.base', 'pynepcord.aio'),
      license=__license__,
      classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
      ),
      description='Python SDK for the NeppedCord API',
      long_description=readme,
      long_description_content_type="text/markdown",
      include_package_data=True,
      install_requires=requirements)
