import unittest
from HTML.Auto import Attr

class TestTags(unittest.TestCase):

    def test_keys(self):
        auto = Attr()
        self.assertEqual( auto.key( '  ' ), '',             "only spaces" )
        self.assertEqual( auto.key( 'foo bar' ), 'foobar',  "with space" )
        self.assertEqual( auto.key( '">=//=>"' ), '',       "only scrubbed chars" )
        self.assertEqual( auto.key( 'foo<bar' ), 'foo<bar', "does not scrub < char" )

    def test_vals(self):
        auto = Attr()
        self.assertEqual( auto.val( '  ' ), '',             "only spaces" )
        self.assertEqual( auto.val( 'foo bar'), 'foo bar',  "with space" )
        self.assertEqual( auto.val( "'foo'" ), "'foo'",     "single quotes are not scrubbed" )
        self.assertEqual( auto.val( '"foo"' ), 'foo',       "double quotes are scrubbed" )

    def test_rotate(self):
        auto = Attr()
        list = [ 'one', 'two', 'three' ]
        self.assertEqual( auto.rotate( list ), 'one', "returns 1st val" )
        self.assertEqual( list, [ 'two', 'three', 'one' ], "list rotated" )

        self.assertEqual( auto.rotate( list ), 'two', "returns 1st val" )
        self.assertEqual( list, [ 'three', 'one', 'two' ], "list rotated" )

    def test_simple_autos(self):
        auto = Attr( { 'foo': 'bar', 'baz': 'qux' }, 1 )
        self.assertEqual( str( auto ), ' baz="qux" foo="bar"',   "correct simple autos" )

    def test_rotate_autos(self):
        auto = Attr( { 'foo': ['bar','baz','qux'], 'baz': ['foo','qux'] }, 1 )
        self.assertEqual( str( auto ), ' baz="foo" foo="bar"',          "correct rotate autos 1" )
        self.assertEqual( str( auto ), ' baz="qux" foo="baz"',          "correct rotate autos 2" )
        self.assertEqual( str( auto ), ' baz="foo" foo="qux"',          "correct rotate autos 3" )
        self.assertEqual( str( auto ), ' baz="qux" foo="bar"',          "correct rotate autos 4" )
        self.assertEqual( str( auto ), ' baz="foo" foo="baz"',          "correct rotate autos 5" )

    def test_nested_autos(self):
        auto = Attr( { 'foo': { 'bar': 'baz', 'qux': ['one','two','tre'] } }, 1 )
        self.assertEqual( ' foo="bar: baz; qux: one;"', auto.__str__(),          "correct nested autos" )
        self.assertEqual( ' foo="bar: baz; qux: two;"', auto.__str__(),          "correct nested autos" )
        self.assertEqual( ' foo="bar: baz; qux: tre;"', auto.__str__(),          "correct nested autos" )


if __name__ == '__main__':
    unittest.main()
