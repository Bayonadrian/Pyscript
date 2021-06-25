class string:

    def getLen(self, name: str, txt: str, var= True):

        if var == True:

            return 'var {name} = {txt}.length;'.format(name= name, txt= txt)

        else:

            return 'var {name} = "{txt}".length;'.format(name= name, txt= txt)

    def getSlice(self, name: str, txt: str, *args, var= True):

        if len(args) <= 2:

            if len(args) == 1:

                start = args[0]

                if var == True:

                    return 'var {name} = {txt}.slice({start});'.format(name= name, txt= txt, start= start)

                else:

                    return 'var {name} = "{txt}".slice({start});'.format(name= name, txt= txt, start= start)

            else:

                start = args[0]
                end = args[1]

                if var == True:
                    
                    return 'var {name} = {txt}.slice({start}, {end});'.format(name= name, txt= txt, start= start, end= end)
                
                else:

                    return 'var {name} = "{txt}".slice({start}, {end});'.format(name= name, txt= txt, start= start, end= end)


        elif len(args) == 0:

            raise Exception('Have to put an argument')

        else:

            raise Exception('Too much arguments')

    def repl(self, name: str, txt: str, rep: str, to: str, var= True):

        if var == True:

            return 'var {name} = {txt}.replace("{rep}", "{to}");'.format(name= name, txt= txt, rep= rep, to= to)

        else:

            return 'var {name} = "{txt}".replace("{rep}", "{to}");'.format(name= name, txt= txt, rep= rep, to= to)



    