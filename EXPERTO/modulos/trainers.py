import os
import modulos.comprobacion as c

########### AÑADIR TRAINERS ################################################################

def addtrainer(campus:dict):
    grupo=[]
    lista=[1,2,3]
    opciones=['1. MAÑANA','2. TARDE','3. AMBOS']
    nombre=c.comprobarT('INGRESE EL NOMBRE DEL TRAINER: ').upper()
    if nombre not in campus['trainers']:
        id=c.comprobarT('INGRESE EL ID DEL TRAINER: ').upper()
        for item in opciones:
            print (item)
        try:   
            op=c.comprobar('INGRESE EL HORARIO: ')
            if op not in lista:
                print('HORARIO NO VALIDO')
                os.system('pause')
                addtrainer(campus)
        except ValueError:
            print('DATO INVALIDO')
            os.system('pause')
            addtrainer(campus)

        if op==1:
            horario='MAÑANA'
        elif op==2:
            horario='TARDE'
        else:
            horario='AMBAS'
        

        trainer={
                'id':id,
                'nombre':nombre,
                'horario':horario,
                'grupos':grupo
                }

        campus['trainers'][nombre]=trainer
    else:
        print(f'EL trainer:{nombre} YA SE ENCUENTRA REGISTRADO EN EL SISTEMA')