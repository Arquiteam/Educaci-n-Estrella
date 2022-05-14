from django.db import models
from django.db import models

class SucursalAcompañamiento(models.Model):
    numAsistencias = models.IntegerField(null=False, default=0)
    sCurso = models.OneToOneField(to='ServicioCurso.ServicioCurso', on_delete=models.SET_NULL, null=True)
    sEdContinua = models.OneToOneField(to='ServicioEducacionContinua.ServicioEducacionContinua', on_delete=models.SET_NULL, null=True)
    sBoEmpleo = models.OneToOneField(to='ServicioBolsaEmpleo.ServicioBolsaEmpleo', on_delete=models.SET_NULL, null=True)
    sAtPsicologica = models.OneToOneField(to='ServicioAtencionPsicologica.ServicioAtencionPsicologica', on_delete=models.SET_NULL, null=True)
    sMentoria = models.OneToOneField(to='ServicioMentoria.ServicioMentoria', on_delete=models.SET_NULL, null=True)
    estudiante = models.OneToOneField(to='Estudiante.Estudiante', on_delete=models.CASCADE, null=True)

    def __str__(self):
        
        return '%s' % (self.numAsistencias)