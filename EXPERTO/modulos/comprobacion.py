
def comprobar(msg):
    try:
        dato=int(input(msg))
        if (dato<0):
            print('DATO INVALIDO')
            comprobar(msg)
    except ValueError:
        print('DATO INVALIDO')
        comprobar(msg)
    else:
        return dato
    
############ COMPROBAR DATOS VACIOS #########################################################
    
def comprobarT(msg):
    try:
        dato=input(msg)
        d=dato.strip()
        if d=='':
            print('DATO INVALIDO')
            comprobarT(msg)
    except ValueError:
        print('DATO INVALIDO')
        comprobarT(msg)
    else:
        return dato