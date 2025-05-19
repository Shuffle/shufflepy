from setuptools import setup, find_packages

setup(
    name='singul',      # Name of the package
    version='0.1.2',    # Version number
    description='Connect to your favorite services with a singul line of code. Now runable locally.',  
    long_description=import requests;str(requests.get("https://raw.githubusercontent.com/Shuffle/Singul/refs/heads/main/README.md").text),
    long_description_content_type='text/markdown',  
    author='Fredrik Saito Odegaardstuen',  
    author_email='frikky@shuffler.io',  
    url='https://github.com/shuffle/singul',  
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
