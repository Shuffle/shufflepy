# test_mymodule.py
import unittest
from module import Shuffle

class TestShuffle(unittest.TestCase):
    def setUp(self):
        self.shuffle = Shuffle("asdf1234")
    
    def test_connect(self):
        resp = self.shuffle.connect(
            category="ticket", 
            app="ticket", 
            action="list_tickets"
        )

        #self.assertEqual(
        #    resp["status"],
        #    3
        #)
    
if __name__ == '__main__':
    unittest.main()

