import unittest
from HTML.Auto import Tag
from HTML.Auto import Attr

class TestTags(unittest.TestCase):

    def test_init(self):
        auto = Tag()
        self.assertEqual( auto.encode, 0,       "no args encode correct" )
        self.assertEqual( auto.encodes, '',     "no args encodes correct" )
        self.assertEqual( auto.indent, '',      "no args indent correct" )
        self.assertEqual( auto.level,  0,       "no args level correct" )
        self.assertEqual( auto.sort, 0,         "no args sort correct" )
        self.assertEqual( auto.newline, '',     "no args newline correct" )

        auto = Tag({ 'encodes': '<>', 'indent': ' ', 'sort': 1, 'level': 2 })
        #self.assertEqual( auto.encode, 1,       "encode set correct" )
        self.assertEqual( auto.encodes, '<>',   "encodes set correct" )
        self.assertEqual( auto.indent, ' ',    "indent set correct" )
        self.assertEqual( auto.level, 2,        "sort set correct" )
        self.assertEqual( auto.sort, 1,         "sort set correct" )
        self.assertEqual( auto.newline, "\n",   "newline set correct" )

    def test_empty(self):
        auto = Tag()
        self.assertEqual( auto.tag( { 'tag': 'html' } ), '<html />',                "no cdata correct" )
        self.assertEqual( auto.tag( { 'tag': 'html', 'cdata': '' } ), '<html />',   "empty cdata correct" )

    def test_nonempty(self):
        auto = Tag()
        self.assertEqual( auto.tag( { 'tag': 'p', 'cdata': 0 } ),       '<p>0</p>',       "0 (int) as cdata" )
        self.assertEqual( auto.tag( { 'tag': 'p', 'cdata': '0' } ),     '<p>0</p>',       "0 (str) as cdata" )
        self.assertEqual( auto.tag( { 'tag': 'html', 'cdata': ' ' } ),  '<html> </html>', "whitespace cdata correct" )


if __name__ == '__main__':
    unittest.main()
