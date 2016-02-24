HTML-Auto (python)
=====================
Just another HTML tag generator for Python.  [![pypi package](https://badge.fury.io/py/HTML-Auto.svg)](https://pypi.python.org/pypi/HTML-Auto) [![Build Status](https://api.travis-ci.org/jeffa/HTML-Auto-python.svg?branch=master)](https://travis-ci.org/jeffa/HTML-Auto-python)

Description
-----------
Generate HTML tags with ease (HTML4, HTML5, XHTML and SVG).

Synopsis
--------
```python
from HTML.Auto import Tag

auto = Tag()
print( auto.tag({ 'tag': 'li', 'cdata': 'item', 'attr': { 'class': 'foo' } }) )

print( auto.tag({ 'tag': 'hr' }) )
print( auto.tag({ 'tag': 'h1', 'cdata': 'heading' }) )
print( auto.tag({ 'tag': 'p', 'cdata': 'paragraph', 'attr': { 'class': 'para' } }) )

auto = Tag({ 'indent': '    ' })
attr = { 'style': { 'color': [ 'red', 'green' ] } }
print(
    auto.tag({
        'tag': 'ol',
        'attr': { 'reversed': 'reversed' },
        'cdata': [ list(map((lambda d: { 'tag': 'li', 'attr': attr, 'cdata': d }), [1,2,3,4,5])) ]
    })
)

tr_attr = { 'class': [ 'odd', 'even' ] }
print(
    auto.tag({
        'tag': 'table',
        'attr': { 'class': 'spreadsheet' },
        'cdata': [
            {
                'tag': 'tr',
                'attr': tr_attr,
                'cdata': {
                    'tag': 'th',
                    'attr': { 'style': { 'color': [ 'red', 'green' ] } },
                    'cdata': [ 'one', 'two', 'three' ],
                },
            },
            {
                'tag': 'tr',
                'attr': tr_attr,
                'cdata': {
                    'tag': 'td',
                    'attr': { 'style': { 'color': [ 'orange', 'blue' ] } },
                    'cdata': [ 'four', 'five', 'six' ],
                },
            },
            {
                'tag': 'tr',
                'attr': tr_attr,
                'cdata': {
                    'tag': 'td',
                    'attr': { 'style': { 'color': [ 'red', 'green' ] } },
                    'cdata': [ 'seven', 'eight', 'nine' ],
                },
            },
        ]
    })
)
```

Also includes HTML.Auto.Attr which provides rotating attributes.
```python
from HTML.Auto import Attr

auto = Attr({ 'foo': ['bar','baz','qux'] })

for i in range(4):
    print( str( auto ) ) 
```

Installation
------------
```
pip install HTML-Auto
```

License and Copyright
---------------------
See [License](License.md).
