from setuptools import setup, find_packages

def get_long_description():
    import requests

    try:
        url = "https://raw.githubusercontent.com/shuffle/singul/main/README.md"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Warning: failed to fetch remote README.md: {e}")
        return "Singul package - CLI and library. ERROR: Failed to load README. " 

setup(
    name='singul',      # Name of the package
    version='0.1.3',    # Version number
    description='Connect to your favorite services with a singul line of code. Now runable locally.',  
    long_description=get_long_description(),  
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
