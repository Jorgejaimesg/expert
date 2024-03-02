
import os
import modulos.comprobacion as c

def modulos():
    lista=[1,2,3,4,5]
    opciones=['1. fundamentos','2. web','3. formal','4. basedatos','5. backend']
    for item in opciones:
        print(item)
    try:
        op=int(input('seleccione el modulo'))
        if op not in lista:
            modulos()
    except ValueError:
        modulos()
    else:
        return op

def addnotas(campers):
    
    id=c.comprobarT('INGRESE EL ID DEL ESTUDIANTE')
    if id in campers:
        if (campers[id]['estado']=='APROVADO' or campers[id]['estado']=='RIESGO') and campers[id]['ruta']!='N/A':
            op=modulos()
            if op==1:
                modulo='fundamentos'
            elif op==2:
                modulo='web'
            elif op==3:
                modulo='formal'
            elif op==4:
                modulo='basedatos'
            else:
                modulo='backend'

            teorica=c.comprobar(f'Ingrese la nota teorica del modulo {modulo} ')
            practica=c.comprobar(f'Ingrese la nota practica del modulo {modulo}')
            trabajos=c.comprobar(f'Ingrese la nota de trabajos del modulo {modulo}')

            notafinal=(teorica*0.30)+(practica*0.60)+(trabajos*0.10)
            campers[id]['notas'][modulo]=notafinal

            if notafinal>60:
                campers[id]['estado']='APROVADO'
            elif notafinal<=60 and notafinal>=50:
                campers[id]['estado']='RIESGO'
            elif notafinal<50:
                campers[id]['estado']='REPROVADO'
                print('EL ESTUDIANTE REPROBO, POR TAL MOTIVO NO PUEDE SEGUIR EN EL PROGRAMA')
        else:
            print('EL ESTUDIANTE REPROBO, POR TAL MOTIVO NO PUEDE SEGUIR EN EL PROGRAMA')
    else:
        print('EL ESTUDIANTE NO SE ENCUENTRA REGISTRADO EN EL SISTEMA O EN UNA RUTA')
    os.system('pause')

        
                
