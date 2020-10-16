#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

from frequency2wavelength import __author__, __version__, __email__

setup(name="f2w",
     version='.'.join([str(v) for v in __version__]),
     description="calculate frequency2wavelength and vice versa",
     author=__author__,
     author_email=__email__,
     packages=find_packages(),
     include_package_data=True,
     install_requires=[
         "setuptools",
         "Pint",
         "scipy",
         "numpy"],
     py_modules=['f2w'],
     scripts=['./bin/f2w'],
     project_urls={
        'Documentations': 'http://lj25fp.asux-ae-ai-gitlab.aptiv.today/f2w',
        'Source': 'https://github.com/afeldman/f2w',
        'Tracker': 'https://github.com/afeldman/f2w/issues'
     },
)