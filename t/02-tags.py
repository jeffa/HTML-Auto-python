import unittest
from HTML.Auto import Tag
from HTML.Auto import Attr

class TestTags(unittest.TestCase):

    def test_tag(self):
        auto = Tag()
        self.assertEqual( auto.tag( { 'tag':'html' } ), '<html />' )
        self.assertEqual( auto.tag( { 'tag':'html', 'cdata':'' } ), '<html />' )

    def test_cdata(self):
        auto = Tag()
        self.assertEqual( auto.tag( { 'tag':'foo', 'cdata':'bar' } ), '<foo>bar</foo>' )


if __name__ == '__main__':
    unittest.main()
