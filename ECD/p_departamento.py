# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
import json
from gercontro import models
from gercontro.models import Departamento
from django.http import HttpResponse
from gercontro import forms
from django.shortcuts import render
from django.core import serializers
from django.core.serializers.python import Serializer
from django.utils import simplejson
"""
class MySerialiser(Serializer):
    def end_object( self, obj ):
        self._current['id'] = obj._get_pk_val()
        self.objects.append( self._current )
"""
def incluir(request):
    pai = request.POST['pai']
    if pai == '':
        pai = '#'

    objDepartamento = Departamento.create(request.POST['pai'], request.POST['descricao'])
    objDepartamento.save()
    frmDepartamento = forms.DepartamentoForm()
    return render(request, 'gercontro/departamentos.html',{
        'return': "true",
        'title':'Gercontro | Departamentos',
        'frmDepartamento' : frmDepartamento,
        'departamentos' : recuperaDepartamentos(),
    })

#recupera todos os objetos
def recuperaDepartamentos():
    objDepartamentos = models.Departamento.objects.all()
    return objDepartamentos

#recupera todos um objeto especifico pelo id
def recuperaDepartamento(id):
    objDepartamento = models.Departamento.objects.get(id=id)
    return objDepartamento

def updateDepartamento(request):
	idObj = request.POST['id']
	objDepartamento = models.Departamento.objects.get(id=idObj)
	
	objDepartamento.nome = request.POST['pai']
	objDepartamento.telefone1 = request.POST['descricao']
	objDepartamento.save()
	return render(request, 'gercontro/departamentos.html',{
		'objReturn' : 'editOK',
	})

#exclui um objeto especifico pelo id e o retorna para confirmar a exclusao do objeto
def excluirDepartamento(request):
	idObj = request.GET['id']
	print ("Id Excluir "+str(idObj))
	objDepartamento = models.Departamento.objects.get(id=idObj)
	objDepartamento.delete()
	return render(request,'gercontro/departamentos.html',{
		'objReturn': objDepartamento,
		})

def gerarArvoreDptos(request):
  # objJson = json.dumps([dict(item) for item in Departamento.objects.all().values('id','pai', 'descricao')])
    objs = Departamento.objects.all()
    data =simplejson.dumps( [{'text': o.descricao,
                              'id': o.id,
                           'parent': o.pai,
                           } for o in objs])
    #print (" antes "+ str(data))
    
    return HttpResponse(data)


#METODO QUE ALTERA O FORMATO DO OBJETO DA CONSULTA PARA O FORMATO JSON
def formatoJson(c):
    rows = [x for x in c]
    cols = [x[0] for x in c.description]
    songs = []
    for row in rows:
      song = {}
      for prop, val in zip(cols, row):
         song[prop] = val
      songs.append(song)
    songsJSON = json.dumps(songs)
    return songsJSON	