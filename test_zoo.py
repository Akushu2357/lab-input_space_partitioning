import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_C1b1_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), None)

    def test_C1b2_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test_C1b3_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_C1b4_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
    
    def test_C1b5_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(99), 100)
       
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()