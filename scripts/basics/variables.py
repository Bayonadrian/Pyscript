class variables:

    def var(self, **kwargs):

        if len(kwargs) == 1:

            args = kwargs.items()

            args = tuple(args)

            name = args[0][0]

            value = args[0][1]

            return 'var {name} = {value};'.format(name= name, value= value)

        elif len(kwargs) < 1:

            raise Exception('Have to put a parameter')

        else:

            raise Exception('Too much parameters')

    def let(self, **kwargs):

        if len(kwargs) == 1:

            args = kwargs.items()

            args = tuple(args)

            name = args[0][0]

            value = args[0][1]

            return 'let {name} = {value};'.format(name= name, value= value)
        
        elif len(kwargs) < 1:

            raise Exception('Have to put a parameter')

        else:

            raise Exception('Too much parameters')

    def const(self, **kwargs):

        if len(kwargs) == 1:

            args = kwargs.items()

            args = tuple(args)

            name = args[0][0]

            value = args[0][1]

            return 'const {name} = {value};'.format(name= name, value= value)

        elif len(kwargs) < 1:

            raise Exception('Have to put a parameter')

        else:

            raise Exception('Too much parameters')