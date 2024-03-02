import os
import modulos.comprobacion as c

########### AÑADIR CAMPERS ################################################################

def addCamper(campus:dict):
    id=c.comprobarT('INGRESE EL ID DEL CAMPER: ').upper()
    if id not in campus['campers']:
        nombre=c.comprobarT('INGRESE EL NOMBRE DEL CAMPER: ').upper()
        apellido=c.comprobarT('INGRESE EL APELLIDO DEL CAMPER: ').upper()
        direccion=c.comprobarT('INGRESE LA DIRECCION DEL CAMPER: ').upper()
        celular=c.comprobar('INGRESE TELEFONO DEL CAMPER: ')
        fijo=c.comprobar('INGRESE EL NUMERO FIJO DEL CAMPER: ')

        camper={
                'id':id,
                'nombre':nombre,
                'apellido':apellido,
                'estado':'INSCRITO',
                'ruta':'N/A',
                'grupo':'N/A',
                'direccion':direccion,
                'celula':celular,
                'fijo':fijo,
                'acudientes':{},
                'notas':{
                    'fundamentos':0,
                    'web':0,
                    'formal':0,
                    'basedatos':0,
                    'backend':0,}
                }
        isPadres=True
        while isPadres:
            nombre= c.comprobarT('INGRESE EL NOMBRE DEL ACUDIENTE: ').upper()
            celular_acudiente=c.comprobar('INGRESE TELEFONO DEL ACUDIENTE: ')
            acudiente={
                'nombre':nombre,
                'celular':celular_acudiente
            }

            camper['acudientes'][len(camper['acudientes'])+1]=acudiente
            isPadres=bool(input('DESEA INGRESAR OTRO ACUDIENTE S(SI) O ENTER(NO)'))


        campus['campers'][id]=camper
    else:
        print(f'EL ID:{id} YA SE ENCUENTRA REGISTRADO EN EL SISTEMA')