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
            '<colgroup span="3">0</colgroup>',
            auto.tag( { 'tag': 'colgroup', 'attr': { 'span': 3 }, 'cdata': 0 } ),
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

if __name__ == '__main__':
    unittest.main()
