from setuptools import setup, find_packages
setup(
    name='shufflepy',   # Name of the package
    version='0.1.6',    # Version number
    description='Use Shufflepy to control Shuffle and Singul', 
    long_description=get_long_description(),  
    long_description_content_type='text/markdown',  
    author='Fredrik Saito Odegaardstuen',  
    author_email='frikky@shuffler.io',  
    url='https://github.com/shuffle/shufflepy',  
    packages=find_packages(),  
    install_requires=[  
        'requests',
        'tqdm',
    ],
    classifiers=[  
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify Python version requirements
)

def get_long_description():
    try:
        import requests
        url = "https://raw.githubusercontent.com/shuffle/shufflepy/main/README.md"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Warning: failed to fetch remote README.md: {e}")
        return "Shufflpy package - CLI and library. ERROR: Failed to load README"

