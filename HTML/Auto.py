import re
from cgi import escape

__version__='0.0.2'

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

        ctype     = type( cdata )
        rendered  = ''
        no_indent = 0

        if not type( attr ) is Attr:
            attr = Attr( attr, self.sort )

        if ctype is list:

            if type( cdata[0] ) is dict:
                self.level += 1
                rendered = self.newline

                for hash in cdata:
                    rendered += self.tag( hash )
                
                self.level -= 1
            else:
                string = ''
                for scalar in cdata:
                    string += self.tag({ 'tag': tag, 'attr': attr, 'cdata': scalar })
                return string

        elif ctype is dict:
            self.level += 1
            rendered = self.newline + self.tag( cdata )
            self.level -= 1

        else:
            # empty tag
            if not len( str( cdata ) ):
                return '<' + tag + str(attr) + ' />'

            rendered = cdata #TODO: encoding happens here
            no_indent = 1

        indent = '' if no_indent else self.indent * self.level

        return (self.indent * self.level) + \
            '<' + tag + str( attr ) + '>' + \
            str( rendered ) + indent + \
            '</' + tag + '>' + self.newline


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
                val = self.stringify( val ) if type( val ) is dict else val
                val = self.rotate( val )    if type( val ) is list else val
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

    def stringify( self, attrs ):
        keys = sorted( attrs.keys() ) if self.sort else attrs.keys()
        vals = []
        for key in keys:
            val = attrs[key]
            if type( val ) is list:
                val = self.rotate( val )
            elif type( val ) is dict:
                k = sorted( val.keys() ) if self.sort else val.keys()
                val = k[0]
            vals.append( '%s: %s' % ( key, val ) )
        trail = ';' if len( vals ) else ''
        return '; '.join( vals ) + trail


class Table:

    def portrait( *args ):
        generate( *args, 'theta', 0 )
    def landscape( *args ):
        generate( *args, 'theta', -270, 'tgroups', 0 )
    def north( *args ):
        generate( *args, 'theta', 0 )
    def west( *args ):
        generate( *args, 'theta', -270, 'tgroups', 0 )
    def east( *args ):
        generate( *args, 'theta',   90, 'tgroups', 0, 'pinhead', 1 )
    def south( *args ):
        generate( *args, 'theta', -180, 'tgroups', 0, 'pinhead', 1 )

    def __init__( *args ):
        1

    def generate( self, *args ):
        params = self._process( *args )

        return self._make_table( params )

    def _make_table( self, params ):
        cdata = []
        return params['auto'].tag({ 'tag': 'table' })

    def _process( self, *args ):
        params = self._args( *args )
        return params

    def _args( self, *thingy ):
        data = []
        args = {}

        things = list( thingy )
        while things:
            thing = things.pop(0)
            if type( thing ) is list:
                if type( thing[0] ) is list:
                    data = thing
                else:
                    data.append( thing )
            elif type(thing) is dict:
                data = thing.pop( 'data', None )
                args = thing
            else:
                if thing is 'data':
                    data = things.pop(0)
                else:
                    args[thing] = things.pop(0)

        args['auto'] = Tag({
            'indent': args.get( 'indent', '' ),
            'level': args.get( 'level', 0 ),
            'sort': args.get( 'attr_sort', 0 )
        })

        self.data = data
        return args
