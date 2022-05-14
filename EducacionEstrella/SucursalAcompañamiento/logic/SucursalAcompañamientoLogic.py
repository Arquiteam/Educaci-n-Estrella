import sys
sys.path.append("..")
from ..models import SucursalAcompañamiento
from ServicioCurso.logic import ServicioCursoLogic as cl
from ServicioEducacionContinua.logic import ServicioEducacionContinuaLogic as ecl
from ServicioBolsaEmpleo.logic import ServicioBolsaEmpleoLogic as bel
from ServicioMentoria.logic import ServicioMentoriaLogic as ml
from ServicioAtencionPsicologica.logic import ServicioAtencionPsicologicaLogic as apl

def get_sucursalacompañamientos():
    sucursalacompañamientos = SucursalAcompañamiento.objects.all()
    return sucursalacompañamientos

def get_sucursalacompañamiento(var_pk):
    sucursalacompañamiento = SucursalAcompañamiento.objects.get(pk=var_pk)
    return sucursalacompañamiento

def update_sucursalacompañamiento(var_pk, new_var):
    sucursalacompañamiento = get_sucursalacompañamiento(var_pk)
    sucursalacompañamiento.numAsistencias = new_var["numAsistencias"]
    sucursalacompañamiento.sCurso = new_var["sCurso"]
    sucursalacompañamiento.sEdContinua = new_var["sEdContinua"]
    sucursalacompañamiento.sBoEmpleo = new_var["sBoEmpleo"]
    sucursalacompañamiento.sAtPsicologica = new_var["sAtPsicologica"]
    sucursalacompañamiento.sMentoria = new_var["sMentoria"]
    sucursalacompañamiento.usuario = new_var["usuario"]
    sucursalacompañamiento.save()
    return sucursalacompañamiento

def create_sucursalacompañamiento(var):
    sCursoInstancia= cl.create_scurso({
    "idText": "sc",
    "descripcion": "Descripcion",
    "numAsistencias": 0,
    "sucursal": None
})
    sEdContinuaInstancia=ecl.create_sedcontinua({
    "idText": "sec",
    "descripcion": "Descripcion",
    "numAsistencias": 0,
    "sucursal":None
})
    sBoEmpleoInstancia=bel.create_sboempleo({
    "idText": "sbe",
    "descripcion": "Descripcion",
    "numAsistencias": 0,
    "sucursal":None
})
    sAtPsicologicaInstancia=apl.create_satpsicologica({
    "idText": "sap",
    "descripcion": "Descripcion",
    "numAsistencias": 0,
    "sucursal":None
})
    sMentoriaInstancia=ml.create_smentoria({
    "idText": "sm",
    "descripcion": "Descripcion",
    "numAsistencias": 0,
    "sucursal":None
})
    estudianteInstancia=None

    sucursalacompañamiento = SucursalAcompañamiento(
                                                    numAsistencias=var["numAsistencias"],
                                                    sCurso=sCursoInstancia,
                                                    sEdContinua=sEdContinuaInstancia,
                                                    sBoEmpleo=sBoEmpleoInstancia,
                                                    sAtPsicologica=sAtPsicologicaInstancia, 
                                                    sMentoria=sMentoriaInstancia,
                                                    estudiante=estudianteInstancia
                                                    )
    sucursalacompañamiento.save()
    return sucursalacompañamiento

def delete_sucursalacompañamiento(var_pk):
    sucursalacompañamiento = get_sucursalacompañamiento(var_pk)
    sucursalacompañamiento.delete()