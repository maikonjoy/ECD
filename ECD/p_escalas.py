# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
from gercontro import models
from gercontro.models import Servo
from django.http import HttpResponse
from gercontro import forms
from django.shortcuts import render
import json
from django.utils import simplejson
from django.shortcuts import redirect
from django.db.models import Q


def incluir(request):
    idServo = models.Servo.objects.get(id = request.POST['idServo'])
    idEncontro = models.Encontro.objects.get(id = request.POST['idEncontro'])
    idDepartamento = models.Departamento.objects.get(id = request.POST['idDepartamento'])
    cor = ''
    obs = ''
    
    if (request.POST['cor']):
        cor = request.POST['cor']
    if (request.POST['obs']):
        obs = request.POST['obs']

    objEscala = models.EscalaServos.create(idServo, idEncontro, idDepartamento,cor,obs)
    objEscala.save()
    frmEscalaServo = forms.EscalaServoForm()
    request.session['msg'] = 'Cadastro inserido com sucesso!'
    return redirect('escalaServos')

#recupera a escala do encontro mais recente cadastrado
def recuperaUltimaEscalaServos():
    objEscala = models.EscalaServos.objects.all()
    return objEscala

#recupera todos os objetos
def recuperaEscalaServos(request):
    if (request.POST['idEncontro']):
        encontro = request.POST['idEncontro']
    objEscala = models.Servo.objects.filter(idEncontro = encontro)
    return objEscala

def updateEscala(request):
	idObj = request.POST['id']
	objEscala = models.EscalaServos.objects.get(id=idObj)
	
	objEscala.nome = request.POST['nome']
	objEscala.telefone1 = request.POST['tel1']
	objEscala.telefone2 = request.POST['tel2']
	objEscala.Igreja = models.Igreja.objects.get(id = request.POST['igreja'])
	objEscala.save()
	request.session['msg'] = 'Cadastro alterado com sucesso!'
	return redirect('escalaServos')

#exclui um objeto especifico pelo id e o retorna para confirmar a exclusao do objeto
def excluirEscala(request):
	idObj = request.GET['id']
	print ("Id Excluir "+str(idObj))
	objEscala = models.EscalaServos.objects.get(id=idObj)
	objEscala.delete()
	request.session['msg'] = 'Cadastro excluido com sucesso!'
	return redirect('escalaServos')

def recuperaLideresQuarto():
    lideres = models.EscalaServos.objects.filter(Q(departamento_id = 16)|Q(departamento_id=17)).order_by('servo__nome')
    return lideres

def gerarArvoreEscalas(request):
    servosEscalados = models.EscalaServos.objects.all()
    jServos =simplejson.dumps( [{'text': o.servo.nome + ' ('+ o.servo.igreja.descricao+')',
                              'id': '999' + str(o.servo.id),
                           'parent': o.departamento_id,
                           } for o in servosEscalados])
    
    return HttpResponse(jServos)