# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


setup(
	name="login_project",
	version="1.0.0",
	description="A sample login project using Flask.",
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
)