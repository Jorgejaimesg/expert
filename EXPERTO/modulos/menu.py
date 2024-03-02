import os
############ MENU PRINCIPAL #############################################################################################################
def menu_principal():
    os.system('cls')
    titulo="""
    +++++++++++++++++++++++++++++++++++++++++++++++++++
    +++++++++++ M E N U   P R I N C I P A L +++++++++++
    ++++++++  C  A  M  P  U  S  L  A  N  D  S  ++++++++
    +++++++++++++++++++++++++++++++++++++++++++++++++++
    """
    opciones=[1,2,3,4,5,6,7,8,9]
    list_opciones=['1. REGISTRAR ESTUDIANTE ','2. REGISTRAR TRAINER','3. REGISTRAR NUEVO EJE TEMATICO','4. ASIGNAR RUTA Y SALON A TRAINER','5. EXAMEN DE ADMISION','6. ASIGNAR SALON A ESTUDIANTE', '7. INGRESAR NOTAS', '8. REGISTROS', '9. SALIR']
    print(titulo)
    for item in list_opciones:
        print(item)
    try:
        op=int(input('->'))
        if op not in opciones:
            print('OPCION INVALIDA')
            os.system('pause')
    except ValueError:
        print('DATO INVALIDO')
        os.system('pause')
    else:
        return op
    
############ MENU REGISTROS #################################################################################################################

def menu_registros():
    os.system('cls')
    titulo="""
    +++++++++++++++++++++++++++++++++++++++++++++++++++
    +++++++++++ M E N U   R E G I S T R O S +++++++++++
    ++++++++  C  A  M  P  U  S  L  A  N  D  S  ++++++++
    +++++++++++++++++++++++++++++++++++++++++++++++++++
    """
    print(titulo)
    opciones=['A','B','C','D','E','F','G']
    list_opciones=['A. CAMPERS EN ESTADO INSCRITO','B. CAMPERS QUE APROBARON EL EXAMEN INICIAL','C. ENTRENADORES','D. ESTUDIANTES CON BAJO RENDIMIENTO','E. CAMPERS Y TRAINERS ASOCIADOS CON UNA RUTA DE ENTRENAMIENTO','F. CUANTOS ESTUDIANTES APROBARON Y PERDIERON LOS MODULOS','G. REGRESAR AL MENU PRINCIPAL']
    for item in list_opciones:
        print(item)
    try:
        op=input('->').upper()
        if op not in opciones:
            print('OPCION INVALIDA')
            os.system('pause')
    except ValueError:
        print('DATO INVALIDO')
        os.system('pause')
    else:
        return op

    