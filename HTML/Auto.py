import re
from cgi import escape

__version__='0.0.1'

class Tag:

    def __init__( self, params={} ):
        self.encode  = 1                 if 'encode'  in params else 0
        self.sort    = 1                 if 'sort'    in params else 0
        self.level   = params['level']   if 'level'   in params else 0
        self.encodes = params['encodes'] if 'encodes' in params else ''
        self.indent  = params['indent']  if 'indent'  in params else ''
        self.newline = "\n"              if 'indent'  in params else ''

    def tag( self, params={} ):

        tag   = params['tag']
        cdata = params['cdata'] if 'cdata' in params else ''
        attr  = params['attr']  if 'attr'  in params else {}

        if not type( attr ) is 'Attr':
            attr = Attr( attr, self.sort )

        # empty tag
        if 'cdata' not in params or not params['cdata']:
            return '<' + tag + attr.__str__() + ' />'

        return '<' + tag + attr.__str__() + '>' + cdata + '</' + tag + '>'


class Attr:

    def __init__( self, params={}, sort=0 ):
        self.params = params
        self.sort   = sort

    def __str__( self ):
        attr  = ''
        seen = {}
        keys = sorted( self.params.keys() ) if self.sort else self.params.keys()
        for key in keys:
            if not key in seen:
                val = self.params[key]
                val = stringify( val ) if type( val ) is 'dict' else val
                val = rotate( val )    if type( val ) is 'list' else val
                attr += ' %s="%s"' % ( self.key( key ), self.val( val ) )
            seen[key] = 1

        return attr

    def key( self, key ):
        key = re.sub( '\s+', '', key )
        key = re.sub( '["\'>=\/]', '', key )
        return key

    def val( self, val ):
        if re.match( '^\s+$', val ):
            return ''
        val = re.sub( '"', '', val )
        return val

    def rotate( self, array ):
        val = array.pop(0)
        array.append( val )
        return val

    def stringify( self, hash ):
        keys = sorted( self.params.keys() ) if self.sort else self.params.keys()


