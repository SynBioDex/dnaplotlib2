from setuptools import setup, find_packages

setup(
    name='DNAplotlib2',
    version='0.2.0',
    packages=find_packages(include=['dnaplotlib2', 'dnaplotlib2.*']),
    tests_require=['pytest'],
)