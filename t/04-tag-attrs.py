import unittest
from HTML.Auto import Tag

class TestTagAttrs(unittest.TestCase):

    def test_simple(self):
        auto = Tag()

        self.assertEqual(
            '<p class="paragraph" />',
            auto.tag( { 'tag': 'p', 'attr': { 'class': 'paragraph' } } ),
            'empty paragraph tag correct'
        )

        self.assertEqual(
            '<p class="paragraph">0</p>',
            auto.tag( { 'tag': 'p', 'attr': { 'class': 'paragraph' }, 'cdata': 0 } ),
            'paragraph tag correct'
        )

        self.assertEqual(
            '<colgroup span="0">0</colgroup>',
            auto.tag( { 'tag': 'colgroup', 'attr': { 'span': 0 }, 'cdata': 0 } ),
            'colgroup tag correct'
        )

        self.assertEqual(
            '<colgroup span="3"><col /></colgroup>',
            auto.tag( {'attr': {'span': 3}, 'cdata': [{'attr': {}, 'tag': 'col'}], 'tag': 'colgroup'} ),
            'colgroup tag correct'
        )

        self.assertEqual(
            '<colgroup span="3"><col /><col /></colgroup>',
            auto.tag( {'attr': {'span': 3}, 'cdata': [{'attr': {}, 'tag': 'col'},{'attr': {}, 'tag': 'col'}], 'tag': 'colgroup'} ),
            'colgroup tag correct'
        )

        self.assertEqual(
            '<table><colgroup><col /><col /><col /></colgroup><colgroup><col /><col /><col /></colgroup><colgroup><col /><col /><col /></colgroup></table>',
            auto.tag({ 'tag': 'table', 'cdata': [
                {'tag': 'colgroup', 'attr': {}, 'cdata': [{'tag': 'col', 'attr': {}}, {'tag': 'col', 'attr': {}}, {'tag': 'col', 'attr': {}}] },
                {'tag': 'colgroup', 'attr': {}, 'cdata': [{'tag': 'col', 'attr': {}}, {'tag': 'col', 'attr': {}}, {'tag': 'col', 'attr': {}}] },
                {'tag': 'colgroup', 'attr': {}, 'cdata': [{'tag': 'col', 'attr': {}}, {'tag': 'col', 'attr': {}}, {'tag': 'col', 'attr': {}}] } ] }),
            'colgroup tag correct'
        )

        self.assertEqual(
            '<table><colgroup><col /><col /><col /></colgroup><colgroup><col /><col /><col /></colgroup><colgroup><col /><col /><col /></colgroup><tr><th>a</th><th>b</th><th>c</th></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td>6</td></tr></table>',
            auto.tag({ 'tag': 'table', 'cdata': [
                {'tag': 'colgroup', 'attr': {}, 'cdata': [{'tag': 'col', 'attr': {}}, {'tag': 'col', 'attr': {}}, {'tag': 'col', 'attr': {}}]},
                {'tag': 'colgroup', 'attr': {}, 'cdata': [{'tag': 'col', 'attr': {}}, {'tag': 'col', 'attr': {}}, {'tag': 'col', 'attr': {}}]},
                {'tag': 'colgroup', 'attr': {}, 'cdata': [{'tag': 'col', 'attr': {}}, {'tag': 'col', 'attr': {}}, {'tag': 'col', 'attr': {}}]},
                {'tag': 'tr', 'attr': {}, 'cdata': [{'tag': 'th', 'attr': {}, 'cdata': 'a'}, {'tag': 'th', 'attr': {}, 'cdata': 'b'}, {'tag': 'th', 'attr': {}, 'cdata': 'c'}]},
                {'tag': 'tr', 'attr': {}, 'cdata': [{'tag': 'td', 'attr': {}, 'cdata': '1'}, {'tag': 'td', 'attr': {}, 'cdata': '2'}, {'tag': 'td', 'attr': {}, 'cdata': '3'}]},
                {'tag': 'tr', 'attr': {}, 'cdata': [{'tag': 'td', 'attr': {}, 'cdata': '4'}, {'tag': 'td', 'attr': {}, 'cdata': '5'}, {'tag': 'td', 'attr': {}, 'cdata': '6'}]}
            ] }),
            'colgroup tag correct'
        )


if __name__ == '__main__':
    unittest.main()
