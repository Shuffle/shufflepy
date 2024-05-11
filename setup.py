from setuptools import setup, find_packages

setup(
    name='shufflepy',
    version='0.1.0',
    description='Connect to your favorite services with a single line of code.' 
    author='shuffle'
    author_email='support@shuffler.io',
    packages=find_packages(),
    install_requires=[
        'requests>=2.31.0',
    ],
)
