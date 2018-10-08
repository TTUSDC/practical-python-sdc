# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

# Name keyword argument passed to setup function should be the same as package name (the name of the folder)

# While in this directory, run `pip install -e .` to install the package
setup(
	name="pizza", 
	description="my pizza package", 
	version="1.0.0", 
	packages=find_packages(),
	include_package_data=True, 
	zip_safe=False
)