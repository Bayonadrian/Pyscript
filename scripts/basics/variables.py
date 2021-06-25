class variables:

    def var(self, name, value):

        return 'var {name} = {value}'.format(name= name, value= value)

    def let(self, name, value):

        return 'let {name} = {value}'.format(name= name, value= value)

    def const(self, name, value):

        return 'const {name} = {value}'.format(name= name, value= value)