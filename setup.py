from setuptools import setup, find_packages

setup(
	name='project1',
	version='1.0',
	author='Akhila Mora',
	authour_email='akhila.mora@ou.edu',
	packages=find_packages(exclude=('tests', 'docs')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']
)
