# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
from gercontro import models
from gercontro.models import Encontro
from django.http import HttpResponse
from django.shortcuts import render
from ECD import p_sitios
from ECD import p_encontristas
from django.db import connection

def incluir(request):
    objSitio = p_sitios.recuperaSitio(request.POST['sitio'])
    objEncontro = Encontro.create(request.POST['nroEvento'], request.POST['dtInicio'], request.POST['dtFim'],objSitio,request.POST['qtParticipantesPrev'],request.POST['qtParticipantesConf'],request.POST['qtOrgPrev'],request.POST['qtOrgConfirmados'],request.POST['valorParticipante'],request.POST['valorOrg'])
    objEncontro.save()

    return render(request, 'gercontro/encontros.html',{
        'return': "true",
    })

#recupera todos os objetos
def recuperaEncontros():
    objEncontros = models.Encontro.objects.all()
    return objEncontros

#recupera todos os objetos
def recuperaParticipantesPorEncontro():
    objEncontros = models.Encontro.objects.all()
    cursor = connection.cursor()
    cursor.execute('SELECT E.id,E.numero, E.dtInicio, E.dtFim, E.sitio_id, E.qtParticipantesPrev,E.qtOrgPrev,COUNT(P.id) AS qtd FROM gercontro_encontro AS E LEFT JOIN gercontro_encontrista AS P ON (E.id = P.encontro_id) group by (E.id) order by (E.id)')
    rows = cursor.fetchall()
    return rows

#recupera todos um objeto especifico pelo id
def recuperaEncontro(idObj):
	objEncontro = models.Encontro.objects.get(id=idObj)
	return objEncontro

def updateEncontro(request):
	idObj = request.POST.get['id']
	objEncontro = models.Encontro.objects.get(id=idObj)
	
	objEncontro.descricao = request.POST.get['descricao']
	objEncontro.responsavel = request.POST.get['responsavel']
	objEncontro.endereco = request.POST.get['endereco']
	objEncontro.bairro = request.POST.get['bairro']
	objEncontro.cidade = request.POST.get['cidade']
	objEncontro.uf = request.POST.get['uf']
	objEncontro.tel1 = request.POST.get['tel1']
	objEncontro.tel2 = request.POST.get['tel2']
	objEncontro.valor = request.POST.get['valor']
	objEncontro.obs = request.POST.get['obs']
	
	objEncontro.save()
	return render(request, 'gercontro/Encontros.html',{
		'objReturn' : 'editOK',
	})
#exclui um objeto especifico pelo id e o retorna para confirmar a exclusao do objeto
def excluirEncontro(request):
	idObj = request.POST.get['id']
	print ("Id Excluir "+str(idObj))
	objEncontro = models.Encontro.objects.get(id=idObj)
	objEncontro.delete()
	return render(request,'gercontro/Encontros.html',{
		'objReturn': objEncontro,
		})
	