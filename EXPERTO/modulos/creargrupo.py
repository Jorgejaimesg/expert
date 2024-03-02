import os
import modulos.comprobacion as c

def menusalon():
    lista=[1,2,3]
    opciones=['1. APOLO', '2. ARTEMIS','3. SPUTNIK']
    for item in opciones:
            print(item)
    try:    
        opr=c.comprobar('->')
        if opr not in lista:
            menusalon()
    except ValueError:
            menusalon()
    else:
        return opr
#########################################################################################################################
def addruta(campus,grupo):
    lista=[1,2,3]
    opciones=['1. JAVA','2. NODEJS','3. NETCORE']
    for item in opciones:
                print (item)
    try:   
        op=c.comprobar(f'INGRESE LA RUTA QUE VA A VER EL GRUPO {grupo}: ')
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
    return ruta
#########################################################################################################################
def addgrupo(campus,msg,hora):
    
    print('TRAINERS DISPONIBLE EN ESE HORARIO: ')
    for key,value in campus['trainers'].items():
        if ((value['horario']==msg) or (value['horario']=='AMBAS'))and((campus['horarios'][hora]['apolo']['trainer']!=value['nombre'])and(campus['horarios'][hora]['sputnik']['trainer']!=value['nombre'])and(campus['horarios'][hora]['artemis']['trainer']!=value['nombre'])):
            print(key)
    trainer=c.comprobarT('ESCRIBA EL NOMBRE DEL TRAINER: ').upper()
    if trainer in campus['trainers']:
        opr=menusalon()
        if opr==1:
            salon='apolo'
        elif opr==2:
            salon='artemis'
        else:
            salon='sputnik'
        if campus['horarios'][hora][salon]['grupo']=='':
            grupo=input('INGRESE EL NOMBRE DEL GRUPO: ').upper()
            campus['horarios'][hora][salon]['grupo']=grupo
            campus['horarios'][hora][salon]['trainer']=trainer
            ruta=addruta(campus,grupo)
            campus['horarios'][hora][salon]['ruta']=ruta
            fecha_inicio=c.comprobarT('INGRESE LA FECHA DE INICIO dd/mm/aaaa')
            fecha_final=c.comprobarT('INGRESE LA FECHA DE CULMINACION dd/mm/aaaa')
            campus['horarios'][hora][salon]['fechainicio']=fecha_inicio
            campus['horarios'][hora][salon]['fechafinal']=fecha_final
        else:
            print('ESTE SALON YA HA SIDO ASIGNADO A UN TRAINER')
    else:
        print('TRAINER INVALIDO')
###########################################################################################################################
def horario():
    print('SELECCIONE UN HORARIO EN DONDE DESEA ASIGNAR UN GRUPO')
    list=[1,2,3,4]
    options=['1. 6:00[am]-10:00[am]', '2. 10:00[am]-2:00[pm]', '3. 2:00[pm]-6:00[pm]', '4. 6:00[pm]-10:00[pm]']
    for item in options:
        print(item)
    try:
        op=c.comprobar('->')
        if op not in list:
            horario()
    except ValueError:
        horario()
    return op
##########################################################################################################################
def creargrupos(campus):
    
    ######### SELECCIONAR HORARIOS
    op=horario()

    if op==1:
        os.system('cls')
        addgrupo(campus,'MAÑANA','6a10')

    elif op==2:
        os.system('cls')
        addgrupo(campus,'MAÑANA','10a14')
    elif op==3:
        os.system('cls')
        addgrupo(campus,'TARDE','14a18')
                
    else:
        os.system('cls')
        addgrupo(campus,'TARDE','18a22')
    
    os.system('pause')

###########################################################################################################################
    
def asignarrutas(campus):
    id=c.comprobarT('INGRESE EL ID DEL ESTUDIANTE').upper()
    if (id in campus['campers']) and (campus['campers'][id]['ruta']=='N/A')and(campus['campers'][id]['estado']=='APROVADO'):
        opa=horario()
        if opa==1:
            hora='6a10'
        elif opa==2:
            hora='10a14'
        elif opa==3:
            hora='14a18'
        else:
            hora='18a22'
        ops=menusalon()
        if ops==1:
            salon='apolo'
        elif ops==2:
            salon='artemis'
        else:
            salon='sputnik'
        
        if campus['horarios'][hora][salon]['ruta']!='':
            if len(campus['horarios'][hora][salon]['n_estudiantes'])<campus['horarios'][hora][salon]['capacidad']:
                campus['campers'][id]['ruta']=campus['horarios'][hora][salon]['ruta']
                campus['campers'][id]['grupo']=campus['horarios'][hora][salon]['grupo']
                campus['horarios'][hora][salon]['capacidad']+=-1
                campus['horarios'][hora][salon]['n_estudiantes'].append(id)
            else:
                print('GRUPO LLENO')

        else:
            print('NO SE A ASIGNADO RUTA A ESE SALON')

        os.system('pause')