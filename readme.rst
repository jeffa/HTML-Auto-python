+++++++++
HTML-Auto
+++++++++

Just another HMTL tag generator.

Installing
==========

Use pip:

    $ pip install HTML-Auto

Using HTML-Auto
===============

tags
----

Generate HTML tags with ease (HTML4, HTML5, XHTML and SVG).

    from HTML.Auto import Tag

    auto = Tag({ 'indent': '    ' })

    print( auto.tag({ 'tag': 'hr' }) )

    print( auto.tag({ 'tag': 'h1', 'cdata': 'heading' }) )

    print( auto.tag({ 'tag': 'p', 'cdata': 'paragraph', 'attr': { 'class': 'para' } }) )

attributes
----------

Also includes HTML.Auto.Attr which provides rotating attributes.

    attr = { 'style': { 'color': [ 'red', 'green' ] } }

    print(

        auto.tag({

            'tag': 'ol',

            'attr': { 'reversed': 'reversed' },

            'cdata': [ list(map((lambda d: { 'tag': 'li', 'attr': attr, 'cdata': d }), [1,2,3,4,5])) ]

        })

    )

development
===========

* Source hosted at `GitHub <http://github.com/jeffa/HTML-Auto-python>`_

Pull requests welcomed. Make sure your patches are well tested.
