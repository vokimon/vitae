#!/usr/bin/env python
from setuptools import setup, find_packages

readme = open("README.md").read()

setup(
	name = "vitae",
	version = "2.0",
	description =
		"Generates curriculum vitae from yaml file into several formats",
	author = "David García-Garzón",
	author_email = "voki@canvoki.net",
	url = 'https://github.com/vokimon/vitae',
	long_description = readme,
	license = 'GNU Affero General Public License v3 or later (AGPLv3+)',
	packages=find_packages(exclude=['*[tT]est*']),
	entry_points={
		'console_scripts': [
			'vitae = vitae.__main__:main',
			]
		},
	install_requires=[
		'yamlns>=0.6',
	],
	#include_package_data = True,
	test_suite = 'vitae',
#	test_runner = 'colour_runner.runner.ColourTextTestRunner',
	classifiers = [
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 2',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Intended Audience :: Developers',
		'Development Status :: 5 - Production/Stable',
		'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
		'Operating System :: OS Independent',
	],
)

