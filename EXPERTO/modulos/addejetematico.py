import os
import modulos.comprobacion as c

########### AÑADIR EJE TEMATICO ################################################################

def addeje(campus:dict):
    lista=[1,2,3]
    opciones=['1. JAVA','2. NODEJS','3. NETCORE']
    lista2=[1,2,3,4,5]
    opciones2=['1. FUNDAMENTOS','2. WEB','3. FORMAL','4. BASEDATOS','5. BACKEND']
############################################ SELECCIONAR RUTA ###############################
    for item in opciones:
            print (item)
    try:   
        op=c.comprobar('INGRESE LA RUTA A LA QUE LE DESEA AGREGAR UN EJE TEMATICO: ')
        if op not in lista:
            print('RUTA NO VALIDA')
            os.system('pause')
    except ValueError:
        print('DATO INVALIDO')
        os.system('pause')

    if op==1:
        ruta='java'
    elif op==2:
        ruta='nodejs'
    else:
        ruta='netcore'

################################################# SELECCIONAR MODULO ############################
    for item in opciones2:
            print (item)
    try:   
        op2=c.comprobar('INGRESE LA RUTA A LA QUE LE DESEA AGREGAR UN EJE TEMATICO: ')
        if op2 not in lista2:
            print('RUTA NO VALIDA')
            os.system('pause')
    except ValueError:
        print('DATO INVALIDO')
        os.system('pause')

    if op2==1:
        modulo='fundamentos'
    elif op2==2:
        modulo='web'
    elif op2==3:
        modulo='formal'
    elif op2==4:
        modulo='basedatos'
    else:
        modulo='backend'
    if modulo in campus['rutas'][ruta]:
        print(f'LOS MODULOS QUE ACTUALMENTE SE ENCUENTRAN REGISTRADOS SON \n {campus["rutas"][ruta][modulo]}')
        nuevo_eje=c.comprobarT('INGRESE EL NUEVO EJE TEMATICO, SI YA SE ENCUENTRA REGISTRADO ESCRIBA N:').lower()
        if nuevo_eje not in campus['rutas'][ruta][modulo]and nuevo_eje!='n':
                campus['rutas'][ruta][modulo].append(nuevo_eje)
    
        else:
            print('SERA REDIRIJIDO AL MENU PRINCIPAL')
            os.system('pause')