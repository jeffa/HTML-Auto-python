import unittest
from HTML.Auto import Table

class TestTable(unittest.TestCase):

    def test_instance(self):
        data = [[1,'a'], [2,'b']]
        html = '<table>'
        #html = '<table><tr><th>1</th><th>a</th></tr><tr><td>2</td><td>b</td></tr></table>'

        gen  = Table()

        self.assertEqual(
            html,
            gen.generate( [1,'a'], [2,'b'] ),
            "two array refs"
        )

        self.assertEqual(
            html,
            gen.generate( data ),
            "one array ref"
        )

        self.assertEqual(
            html,
            gen.generate({ 'data': data }),
            "one named arg"
        )

    def test_class(self):
        data = [[1,'a'], [2,'b']]
        html = '<table>'

        self.assertEqual(
            html,
            Table( [1,'a'], [2,'b'] ).generate(),
            "two array refs"
        )

        self.assertEqual(
            html,
            Table( data ).generate(),
            "one array ref"
        )

        self.assertEqual(
            html,
            Table({ 'data': data }).generate(),
            "one named arg"
        )


if __name__ == '__main__':
    unittest.main()
