import unittest
from HTML.Auto import Tag
from HTML.Auto import Attr

class TestLoad(unittest.TestCase):

    def test_load(self):
        self.assertTrue( Tag() )
        self.assertTrue( Attr() )

if __name__ == '__main__':
    unittest.main()
