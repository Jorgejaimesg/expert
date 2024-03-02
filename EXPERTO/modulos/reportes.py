import os
import modulos.comprobacion as c

def aprovados(campers:dict,estado):
    for idx,item in campers.items():
        if item['estado']==estado:
            print (f'{item["id"]}. {item["nombre"]}')
    os.system('pause')

def trainers(trainers:dict):
    for item in trainers:
        print(item)
    os.system('pause')

def rutasreportes(campus):
    lista=[1,2,3]
    opciones=['1. JAVA','2. NODEJS','3. NETCORE']
    for item in opciones:
        print (item)
    try:   
        op=c.comprobar(f'INGRESE LA RUTA: ')
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

    print('REPORTE DE RUTA POR SALONES')
    for key,value in campus['horarios'].items():
        for llave,valor in value.items():
            if valor['ruta']==ruta:
                grupo=campus['horarios'][key][llave]['grupo']
                estudiantes=campus['horarios'][key][llave]['n_estudiantes']
                trainer=campus['horarios'][key][llave]['trainer']
                print(f"grupo: {grupo}, ruta: {ruta}, estudiantes: {estudiantes}, trainer: {trainer}")
            
        os.system('pause')

def reprobados(campus):
    estriesgo=[]
    estaprovados=[]
    lista=[1,2,3]
    opciones=['1. JAVA','2. NODEJS','3. NETCORE']
    for item in opciones:
        print (item)
    try:   
        op=c.comprobar(f'INGRESE LA RUTA: ')
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

    print('REPORTE DE RUTA POR SALONES')
    for key,value in campus['horarios'].items():
        for llave,valor in value.items():
            if valor['ruta']==ruta:
                for item in valor['n_estudiantes']:
                    if campus['campers'][item]['estado']=='APROVADO':
                               estaprovados.append(item)
                    elif campus['campers'][item]['estado']=='RIESGO':
                               estriesgo.append(item)                
                    grupo=campus['horarios'][key][llave]['grupo']
                    trainer=campus['horarios'][key][llave]['trainer']
                    print(f"grupo: {grupo}, ruta: {ruta}, estudiantes aprovados: {estaprovados}, estudiantes en riesgo: {estriesgo}, trainer: {trainer}") 
                    estriesgo=[]
                    estaprovados=[]
    os.system('pause')           