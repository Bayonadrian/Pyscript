from scripts.sistem.writer import writer
from scripts.basics.variables import variables

var = variables()

writer('test', 
    
)

from scripts.basics.functions import *
from scripts.basics.variables import variables

var = variables()

vars = (
        'uno',
        'dos',
        'tres',
        )

body = (
        var.var(uno= 1),
        var.let(dos= 2),
        var.const(tres= 3)
        )
        
fun = functions(name= 'fun', vars=vars, body=body)

print(fun.func())