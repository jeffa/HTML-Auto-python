__version__='0.0.1'

class Tag:

    def __init__( self, params={} ):

        self.encodes = params['encodes'] if 'encodes' in params else ''
        self.encode  = params['encode']  if 'encode'  in params else ''
        self.indent  = params['indent']  if 'indent'  in params else ''
        self.level   = params['level']   if 'level'   in params else ''
        self.sort    = params['sort']    if 'sort'    in params else ''
        self.newline = "\n"              if 'indent'  in params else ''

    def tag( self, params={} ):
        return "<html />"


class Attr:

    def __init__( self, params={} ):
        self.hash   = hash
        self.sorted = sorted

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
