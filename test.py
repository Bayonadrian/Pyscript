from scripts.sistem.writer import writer
from scripts.basics.variables import variables

var = variables()

writer('test', 
    var.var(),
    var.var(dos= 2)
)