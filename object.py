def function1():
    return 1

def function2():
    print("Case 2 selected")

def default():
    print("Value default")

opc = 1 

while (opc != 0):
    
    switch = {
        1: function1,
        2: function2
    }

    opc = int(input('Opc: '))
    case = switch.get(opc, default)
    case()