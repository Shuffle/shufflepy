# test_mymodule.py
import unittest
from module import Singul 

class TestSingul(unittest.TestCase):
    def setUp(self):
        self.shuffle = Singul("asdf1234")
    
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

