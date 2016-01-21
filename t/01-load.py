import unittest
from HTML.Auto import Tag
from HTML.Auto import Attr

class TestLoad(unittest.TestCase):

    def test_tag(self):
        auto = Tag()
        self.assertEqual( auto.encodes, '', 'encodes param not set' )
        self.assertEqual( auto.encode, '',  'encode param not set' )
        self.assertEqual( auto.indent, '',  'indent param not set' )
        self.assertEqual( auto.level, '',   'level param not set' )
        self.assertEqual( auto.sort, '',    'sort param not set' )
        self.assertEqual( auto.newline, '', 'newline param not set' )

        auto = Tag({ 'encodes':1, 'encode':'<>', 'indent':"\t", 'level':4, 'sort':1 })
        self.assertEqual( auto.encodes, 1,      'encodes param set' )
        self.assertEqual( auto.encode, '<>',    'encode param set' )
        self.assertEqual( auto.indent, "\t",    'indent param set' )
        self.assertEqual( auto.level, 4,        'level param set' )
        self.assertEqual( auto.sort, 1,         'sort param set' )
        self.assertEqual( auto.newline, "\n",   'newline param set' )

    def test_attr(self):
        self.assertTrue( Attr() )

if __name__ == '__main__':
    unittest.main()
