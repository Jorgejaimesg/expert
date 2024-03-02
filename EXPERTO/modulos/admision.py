import os
import modulos.comprobacion as c

################ MIRAR SI YA HICIERON EL EXAMEN DE ADMISION Y SI NO REGISTRARLO PARA CAMBIAR SU ESTADO ###########################################3

def examenAdmision(campus:dict):
    id=c.comprobarT('INGRESE EL ID DEL CAMPER: ').upper()
    if (id in campus['campers']):
        if (campus['campers'][id]['estado']=='INSCRITO'):
            nota_teorica=c.comprobar('INGRESE LA NOTA TEORICA DEL EXAMEN DE ADMISION: ')
            nota_practica=c.comprobar('INGRESE LA NOTA PRACTICA DEL EXAMEN DE ADMISION: ')
            promedio=(nota_practica+nota_teorica)/2

            if promedio>=60:
                campus['campers'][id]['estado']='APROVADO'
            else:
                campus['campers'][id]['estado']='REPROBADO'

            print(f'el estudiante con id: {id} se encuentra {campus["campers"][id]["estado"]}')
        else:
            print('EL ESTUDIANTE YA PRESENTO PRUEBA DE ADMISION')
    else:
        print('EL ESTUDIANTE NO SE ENCUENTRA REGISTRADO')