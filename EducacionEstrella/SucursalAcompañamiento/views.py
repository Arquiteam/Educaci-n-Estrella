from .logic import SucursalAcompañamientoLogic as sl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sucursalacompañamientos_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            sucursalacompañamiento_dto = sl.get_sucursalacompañamiento(id)
            sucursalacompañamiento = serializers.serialize('json', [sucursalacompañamiento_dto,])
            return HttpResponse(sucursalacompañamiento, 'application/json')
        else:
            sucursalacompañamientos_dto = sl.get_sucursalacompañamientos()
            sucursalacompañamientos = serializers.serialize('json', sucursalacompañamientos_dto)
            return HttpResponse(sucursalacompañamientos, 'application/json')

    if request.method == 'POST':
        sucursalacompañamiento_dto = sl.create_sucursalacompañamiento(json.loads(request.body))
        sucursalacompañamiento = serializers.serialize('json', [sucursalacompañamiento_dto,])
        return HttpResponse(sucursalacompañamiento, 'application/json')

@csrf_exempt
def sucursalacompañamiento_view(request, pk):
    if request.method == 'GET':
        sucursalacompañamiento_dto = sl.get_sucursalacompañamiento(pk)
        sucursalacompañamiento = serializers.serialize('json', [sucursalacompañamiento_dto,])
        return HttpResponse(sucursalacompañamiento, 'application/json')

    if request.method == 'PUT':
        sucursalacompañamiento_dto = sl.update_sucursalacompañamiento(pk, json.loads(request.body))
        sucursalacompañamiento = serializers.serialize('json', [sucursalacompañamiento_dto,])
        return HttpResponse(sucursalacompañamiento, 'application/json')

    if request.method == 'DELETE':
        sucursalacompañamiento_dto = sl.get_sucursalacompañamiento(pk)
        sl.delete_sucursalacompañamiento(pk)
        sucursalacompañamiento = serializers.serialize('json', [sucursalacompañamiento_dto,])
        return HttpResponse(sucursalacompañamiento, 'application/json')