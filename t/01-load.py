import unittest
from HTML.Auto import Tag
from HTML.Auto import Attr
from HTML.Auto import Table

class TestLoad(unittest.TestCase):

    def test_tag(self):
        auto = Tag()
        self.assertEqual( auto.encodes, '', 'encodes param not set' )
        self.assertEqual( auto.encode, 0,   'encode param not set' )
        self.assertEqual( auto.indent, '',  'indent param not set' )
        self.assertEqual( auto.level, 0,    'level param not set' )
        self.assertEqual( auto.sort, 0,     'sort param not set' )
        self.assertEqual( auto.newline, '', 'newline param not set' )

        auto = Tag({ 'encodes':'<>', 'encode':1, 'indent':"\t", 'level':4, 'sort':1 })
        self.assertEqual( auto.encodes, '<>',   'encodes param set' )
        self.assertEqual( auto.encode, 1,       'encode param set' )
        self.assertEqual( auto.indent, "\t",    'indent param set' )
        self.assertEqual( auto.level, 4,        'level param set' )
        self.assertEqual( auto.sort, 1,         'sort param set' )
        self.assertEqual( auto.newline, "\n",   'newline param set' )

    def test_attr(self):
        self.assertTrue( Attr() )

    def test_table(self):
        self.assertTrue( Table() )

if __name__ == '__main__':
    unittest.main()
