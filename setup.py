from setuptools import setup, find_packages

setup(
    name='shufflepy',  # Name of the package
    version='0.0.91',  # Version number
    description='Use Singul to connect to API with a single line of code',  
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',  
    author='Fredrik Saito Odegaardstuen',  
    author_email='frikky@shuffler.io',  
    url='https://github.com/shuffle/shufflepy',  
    packages=find_packages(),  
    install_requires=[  
        'requests',
    ],
    classifiers=[  
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify Python version requirements
)
