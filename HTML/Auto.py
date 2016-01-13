__version__='0.0.1'

class Attr:

    def __init__( self, hash={}, sorted=0 ):
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

class Tag:

    def __init__( self, hash={}, sorted=0 ):
        self.hash   = hash
        self.sorted = sorted

    def tag( params={} ):
        return "<html />"
