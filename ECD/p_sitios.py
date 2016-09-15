# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
from gercontro import models
from gercontro.models import Sitio
from django.http import HttpResponse
from django.shortcuts import render

def start(self):
    print ('Hello')


def incluir(request):
    objSitio = Sitio.create(request.POST['descricao'], request.POST['responsavel'], request.POST['endereco'],request.POST['bairro'],request.POST['cidade'],request.POST['uf'],request.POST['tel1'],request.POST['tel2'],request.POST['valor'],request.POST['obs'])
    print objSitio.valor
    print objSitio.descricao
    objSitio.save()
    
    return render(request, 'gercontro/sitios.html',{
        'return': "true",
    })

#recupera todos os objetos
def recuperaSitios():
    objSitios = models.Sitio.objects.all()
    return objSitios

#recupera todos um objeto especifico pelo id
def recuperaSitio(id):
    objSitio = models.Sitio.objects.get(id=id)
    return objSitio

def updateSitio(request):
	idObj = request.POST['id']
	objSitio = models.Sitio.objects.get(id=idObj)
	
	objSitio.descricao = request.POST['descricao']
	objSitio.responsavel = request.POST['responsavel']
	objSitio.endereco = request.POST['endereco']
	objSitio.bairro = request.POST['bairro']
	objSitio.cidade = request.POST['cidade']
	objSitio.uf = request.POST['uf']
	objSitio.tel1 = request.POST['tel1']
	objSitio.tel2 = request.POST['tel2']
	objSitio.valor = request.POST['valor']
	objSitio.obs = request.POST['obs']
	
	objSitio.save()
	return render(request, 'gercontro/sitios.html',{
		'objReturn' : 'editOK',
	})
#exclui um objeto especifico pelo id e o retorna para confirmar a exclusao do objeto
def excluirSitio(request):
	idObj = request.GET['id']
	print ("Id Excluir "+str(idObj))
	objSitio = models.Sitio.objects.get(id=idObj)
	objSitio.delete()
	return render(request,'gercontro/sitios.html',{
		'objReturn': objSitio,
		})
	