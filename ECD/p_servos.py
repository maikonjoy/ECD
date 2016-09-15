# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
from gercontro import models
from gercontro.models import Servo
from django.http import HttpResponse
from gercontro import forms
from django.shortcuts import render
from django.shortcuts import redirect


def incluir(request):
    objIgreja = models.Igreja.objects.get(id = request.POST['igreja'])
    objServo = Servo.create(request.POST['nome'], request.POST['tel1'], request.POST['tel2'],objIgreja)
    objServo.save()
    frmServo = forms.ServoForm()
    request.session['msg'] = 'Cadastro inserido com sucesso!'
    return redirect('servos')

#recupera todos os objetos
def recuperaServos():
    objServos = models.Servo.objects.all()
    return objServos

#recupera todos um objeto especifico pelo id
def recuperaServo(id):
    objServo = models.Servo.objects.get(id=id)
    return objServo

def updateServo(request):
	idObj = request.POST['id']
	objServo = models.Servo.objects.get(id=idObj)
	
	objServo.nome = request.POST['nome']
	objServo.telefone1 = request.POST['tel1']
	objServo.telefone2 = request.POST['tel2']
	objServo.Igreja = models.Igreja.objects.get(id = request.POST['igreja'])
	objServo.save()
	request.session['msg'] = 'Cadastro alterado com sucesso!'
	return redirect('servos')

#exclui um objeto especifico pelo id e o retorna para confirmar a exclusao do objeto
def excluirServo(request):
	idObj = request.GET['id']
	print ("Id Excluir "+str(idObj))
	objServo = models.Servo.objects.get(id=idObj)
	objServo.delete()
	request.session['msg'] = 'Cadastro excluido com sucesso!'
	return redirect('servos')

def escalar(request):
    idServo = models.Servo.objects.get(request.POST['idServo'])
    idEncontro = models.Encontro.objects.get(request.POST['idEncontro'])
    idDepartamento = models.Departamento.objects.get(request.POST['idDepartamento'])

    if (request.POST['cor']):
        cor = request.POST['cor']
    if (request.POST['obs']):
        obs = request.POST['obs']

    objEscala = models.EscalaServos.create(idServo, idEncontro, idDepartammento)
    objEscala.save()
    return render(request, 'gercontro/escalaServos.html',{
        'return': "true",
        'title':'Gercontro | Escala de Servos',
        'frmEscalaServo' : frmEscalaServo,
    })

#recupera todos os objetos
def recuperaEscalaServos(request):
    if (request.POST['idEncontro']):
        encontro = request.POST['idEncontro']
    objEscala = models.Servo.objects.filter(idEncontro = encontro)
    return objEscala