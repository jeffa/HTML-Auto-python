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
        str = ''
        return str

    def key( self, str ):
        # scrub key
        return str

    def val( self, str ):
        # scrub value
        return str

    def rotate( self, array ):
        str = "rotate" # shift array
        #array.push( val )
        return str

    def stringify( self, hash ):
        # do the things
        return "do the things!"
