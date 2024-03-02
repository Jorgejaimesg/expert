import modulos.menu as m
import modulos.addCamper as ac
import modulos.admision as ad
import modulos.trainers as t
import modulos.addejetematico as eje
import modulos.creargrupo as cg
import modulos.notas as n
import modulos.reportes as r
if __name__=='__main__':
    campus={
        'campers':{},
        'rutas':{
            'java':{
                'fundamentos':['introducciónalgoritmia', 'pseint', 'python'],
                'web':['html', 'css', 'bootstrap'],
                'formal':['java', 'javascript', 'c#'],
                'basedatos':['mysql', 'mongodb', 'postgresql'],
                'backend':['netcore', 'springboot', 'nodejs', 'express']
            },
            'nodejs':{
                'fundamentos':['introducciónalgoritmia', 'pseint', 'python'],
                'web':['html', 'css', 'bootstrap'],
                'formal':['java', 'javascript', 'c#'],
                'basedatos':['mysql', 'mongodb', 'postgresql'],
                'backend':['netcore', 'springboot', 'nodejs', 'express']
            },
            'netcore':{
                'fundamentos':['introducciónalgoritmia', 'pseint', 'python'],
                'web':['html', 'css', 'bootstrap'],
                'formal':['java', 'javascript', 'c#'],
                'basedatos':['mysql', 'mongodb', 'postgresql'],
                'backend':['netcore', 'springboot', 'nodejs', 'express'] } 
                },
        'horarios':{
            '6a10':{
                    'artemis':{
                        'capacidad':33,
                        'n_estudiantes':[],
                        'grupo':'',
                        'trainer':'',
                        'ruta':'',
                        'fechainicio':'',
                        'fechafinal':''
                            },
                    'apolo':{
                            'capacidad':33,
                            'n_estudiantes':[],
                            'grupo':'',
                            'trainer':'',
                            'ruta':'',
                            'fechainicio':'',
                            'fechafinal':''
                            },
                    'sputnik':{
                        'capacidad':33,
                        'n_estudiantes':[],
                        'grupo':'',
                        'trainer':'',
                        'ruta':'',
                        'fechainicio':'',
                        'fechafinal':''}
                            },
            '10a14':{
                    'artemis':{
                        'capacidad':33,
                        'n_estudiantes':[],
                        'grupo':'',
                        'trainer':'',
                        'ruta':'',
                        'fechainicio':'',
                        'fechafinal':''
                            },
                    'apolo':{
                            'capacidad':33,
                            'n_estudiantes':[],
                            'grupo':'',
                            'trainer':'',
                            'ruta':'',
                            'fechainicio':'',
                            'fechafinal':''
                            },
                    'sputnik':{
                        'capacidad':33,
                        'n_estudiantes':[],
                        'grupo':'',
                        'trainer':'',
                        'ruta':'',
                        'fechainicio':'',
                        'fechafinal':''}
                            },
            '14a18':{
                    'artemis':{
                        'capacidad':33,
                        'n_estudiantes':[],
                        'grupo':'',
                        'trainer':'',
                        'ruta':'',
                        'fechainicio':'',
                        'fechafinal':''
                            },
                    'apolo':{
                            'capacidad':33,
                            'n_estudiantes':[],
                            'grupo':'',
                            'trainer':'',
                            'ruta':'',
                            'fechainicio':'',
                            'fechafinal':''
                            },
                    'sputnik':{
                        'capacidad':33,
                        'n_estudiantes':[],
                        'grupo':'',
                        'trainer':'',
                        'ruta':'',
                        'fechainicio':'',
                        'fechafinal':''}
                            },
            '18a22':{
                    'artemis':{
                        'capacidad':33,
                        'n_estudiantes':[],
                        'grupo':'',
                        'trainer':'',
                        'ruta':'',
                        'fechainicio':'',
                        'fechafinal':''
                            },
                    'apolo':{
                            'capacidad':33,
                            'n_estudiantes':[],
                            'grupo':'',
                            'trainer':'',
                            'ruta':'',
                            'fechainicio':'',
                            'fechafinal':''
                            },
                    'sputnik':{
                        'capacidad':33,
                        'n_estudiantes':[],
                        'grupo':'',
                        'trainer':'',
                        'ruta':'',
                        'fechainicio':'',
                        'fechafinal':''}
                            }
                },
        'trainers':{},
    }
    isRunning=True
    while isRunning:
        op=m.menu_principal()
        if op==1:##REGISTRAR ESTUDIANTE✅
            ac.os.system('cls')
            print('CREAR ESTUDIANTE')
            ac.addCamper(campus)
            ac.os.system('pause')
        if op==2:## REGISTRAR TRAINER✅
            t.os.system('cls')
            print('CREAR TRAINER')
            t.addtrainer(campus)
            t.os.system('pause')
        if op==3:## REGISTRAR EJE✅
            eje.addeje(campus)
        if op==4:## GRUPOS✅
            cg.creargrupos(campus)
        if op==5:## REGISTRAR EXAMEN ADMISION✅
            ad.examenAdmision(campus)
            ad.os.system('pause')
        if op==6:## ASIGNAR RUTAS A ESTUDIANTES Y MEDIR CAPACIDAD✅
            cg.asignarrutas(campus)
        if op==7:##ASIGNAR NOTAS✅
            n.addnotas(campus['campers'])
            pass
        if op==8:
            isRegistros=True
            while isRegistros:
                opr=m.menu_registros()
                if opr=='A':
                    r.aprovados(campus['campers'],'INSCRITO')
                if opr=='B':
                    r.aprovados(campus['campers'],'APROVADO')
                if opr=='C':
                    r.trainers(campus['trainers'])
                if opr=='D':
                    r.aprovados(campus['campers'],'RIESGO')
                if opr=='E':
                    r.rutasreportes(campus)
                if opr=='F':
                    r.reprobados(campus)
                if opr=='G':## SALIR MENU PRINCIPAL ✅
                    isRegistros=False
        if op==9:##SALIR ✅
            isRunning=False
    pass