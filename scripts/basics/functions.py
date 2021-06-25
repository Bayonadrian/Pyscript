class functions:

    def __init__(self, name: str, vars: tuple, body: tuple) -> None:
        
        self.name = name
        self.vars = vars
        self.body = body


    def func(self) -> str:

        vars = tuple(self.vars)
        body = tuple(self.body)

        start = 'function {name}{vars}{{\n'.format(name= self.name, vars=vars)

        body = ''

        for i in self.body:

            body = body + '     ' + i + ';' + '\n'

        start = start.replace("'", '')

        end = '}'

        txt = start + body + end

        return txt