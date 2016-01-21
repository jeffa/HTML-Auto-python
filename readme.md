HTML-Auto (python)
=====================
Just another HTML tag generator for Python.

Description
-----------
Generate HTML tags with ease (HTML4, HTML5, XHTML and SVG).

Synopsis
--------
```python
from HTML.Auto import Tag

auto = Tag()
print( auto.tag({ 'tag': 'li', 'cdata': 'item', 'attr': { 'class': 'foo' } }) )
```

Installation
------------
```
python setup.py install
```

License and Copyright
---------------------
See [License](License.md).
