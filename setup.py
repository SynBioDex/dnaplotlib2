from setuptools import setup

setup(
    name='DNAplotlib2',
    version='2.0',
    description = 'Genetic design visualization',
    packages= ['dnaplotlib2', 'dnaplotlib2.*'],
    tests_require = ['pytest'] 
)