from .module import Singul 

from .base import BaseCategory
from .standalone import Standalone
from .assets import Assets
from .communication import Communication
from .eradication import Eradication
from .iam import IAM
from .intel import Intel
from .network import Network
from .other import Other
from .siem import SIEM

# Sets the default to be to run shufflepy standalone
# Overwritten with Singul()... 
_default_instance = Singul(standalone=True)

__all__ = ["Singul", "connect", "run", "download_binary", "remove_binary"]

"""
Connect to the default instance of Singul.
"""
def connect(*args, **kwargs):
    return _default_instance.connect(*args, **kwargs)

def remove_binary():
    return _default_instance.remove_binary()

def download_binary():
    tmp = Standalone()
    tmp.download_binary()

def run(*args, **kwargs):
    return connect(*args, **kwargs)

