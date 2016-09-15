# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
import p_encontros as Encontros
from gercontro import models
from gercontro.models import Encontrista
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import figures
from django.shortcuts import redirect
from django.db.models import Q
import os, sys
from PIL import Image

def incluir(request):
    objEncontro = Encontros.recuperaEncontro(request.POST['encontro'])
    objIgreja = models.Igreja.objects.get(id = request.POST['igreja'])
    objServo = models.EscalaServos.objects.get(id = request.POST['liderQuarto'])
    objEncontrista = Encontrista.create(objEncontro, objIgreja,request.POST['convidadoPor'],request.POST['telConvPor'], request.POST['nome'],request.POST['sobrenome'],request.POST['dtNascimento'],request.POST['endereco'],request.POST['bairro'],request.POST['cidade'],request.POST['uf'],request.POST['pontoRef'],request.POST['telefone'],request.POST['celular'],request.POST['estadoCivil'],request.POST['sexo'],request.POST['evangelico'],request.POST['freqCelula'],request.POST['celula'],request.POST['batizou'],request.POST['igrejaBatizou'],request.POST['problemaSaude'],request.POST['qualProblema'],request.POST['temAlergia'],request.POST['qualAlergia'],request.POST['gravida'],request.POST['tempoGravidez'],objServo,request.POST['obsGerais'])
    objEncontrista.save()

    request.session['msg'] = 'Cadastro inserido com sucesso!'
    return redirect('encontristas')

#recupera todos os objetos
def recuperaEncontristas():
    objEncontristas = models.Encontrista.objects.all()
    return objEncontristas

#recupera todos um objeto especifico pelo id
def recuperaEncontrista(request):
	idObj = request.GET['id']
	objEncontrista = models.Encontrista.objects.get(id=idobj)
	
	return render(request,'gercontro/Encontristas.html',{
		'objReturn': objEncontrista,
		})

def updateEncontrista(request):
    idObj = request.POST['id']
    objEncontrista = models.Encontrista.objects.get(id=idObj)
    idIgreja = request.POST['igreja']
    objEncontrista.igreja = models.Igreja.objects.get(id=idIgreja)
    objEncontrista.convidadoPor = request.POST['convidadoPor']
    objEncontrista.telConvPor = request.POST['telConvPor']
    objEncontrista.nome = request.POST['nome']
    objEncontrista.sobrenome = request.POST['sobrenome']
    objEncontrista.dtNascimento = request.POST['dtNascimento']
    objEncontrista.endereco = request.POST['endereco']
    objEncontrista.bairro = request.POST['bairro']
    objEncontrista.cidade = request.POST['cidade']
    objEncontrista.uf = request.POST['uf']
    objEncontrista.telefone = request.POST['telefone']
    objEncontrista.celular = request.POST['celular']
    objEncontrista.estadoCivil = request.POST['estadoCivil']
    objEncontrista.sexo = request.POST['sexo']
    objEncontrista.evangelico = request.POST['evangelico']
    objEncontrista.freqCelula = request.POST['freqCelula']
    objEncontrista.celula = request.POST['celula']
    objEncontrista.batizou = request.POST['batizou']
    objEncontrista.igrejaBatizou = request.POST['igrejaBatizou']
    objEncontrista.problemaSaude = request.POST['problemaSaude']
    objEncontrista.qualProblema = request.POST['qualProblema']
    objEncontrista.temAlergia = request.POST['temAlergia']
    objEncontrista.qualAlergia = request.POST['qualAlergia']
    objEncontrista.gravida = request.POST['gravida']
    objEncontrista.tempoGravidez = request.POST['tempoGravidez']
    idLiderQuarto = request.POST['liderQuarto']
    objEncontrista.liderQuarto = models.EscalaServos.objects.get(id=idLiderQuarto)
    objEncontrista.obsGerais = request.POST['obsGerais']

    objEncontrista.save()
    request.session['msg'] = 'Cadastro alterado com sucesso!'
    return redirect('encontristas')

#exclui um objeto especifico pelo id e o retorna para confirmar a exclusao do
#objeto
def excluirEncontrista(request):
    idObj = request.GET['id']
    print ("Id Excluir " + str(idObj))
    objEncontrista = models.Encontrista.objects.get(id=idObj)
    objEncontrista.delete()
    request.session['msg'] = 'Cadastro excluido com sucesso!'
    return redirect('encontristas')

def emitirCracha(lider, encontro):
    participantes = models.Encontrista.objects.filter()





def revisaoEncontrista(request):    
    idObj = request.POST['id']
    objEncontrista = models.Encontrista.objects.get(id=idObj)
    if(request.POST['evangelico']):
        objEncontrista.evangelico = request.POST['evangelico']
    if(request.POST['situacaoFinal']):
        objEncontrista.situacaoFinal = request.POST['situacaoFinal']
    if(request.POST['batizou']):
        objEncontrista.batizou = request.POST['batizou']
    if(request.POST['decidiuBatizar']):
        objEncontrista.decidiuBatizar = request.POST['decidiuBatizar']
    
    objEncontrista.save()

    return HttpResponse('ok')


def revisaoCracha(request):    
    
    idObj = request.POST['id']
    objEncontrista = models.Encontrista.objects.get(id=idObj)
    
    if(request.POST['cracha']):
        objEncontrista.cracha = request.POST['cracha']

    objEncontrista.save()
    return HttpResponse('ok')


#recupera todos os objetos
def recuperaParticipantesCracha(cor,lider):
    if (cor == ' ' and lider == ' '):
        encontristas = models.Encontrista.objects.filter(Q(cracha = 'N')|Q(cracha='R')).order_by('nome')
    elif (cor != ' ' and lider == ' '):
        encontristas = models.Encontrista.objects.filter((Q(cracha = 'N')|Q(cracha='R')),Q(liderQuarto_cor=cor)).order_by('nome')
    elif (cor == ' ' and lider != ' '):
        encontristas = models.Encontrista.objects.filter((Q(cracha = 'N')|Q(cracha='R')),Q(liderQuarto_id=lider)).order_by('nome')
    else:
        encontristas = models.Encontrista.objects.filter((Q(cracha = 'N')|Q(cracha='R')),Q(liderQuarto_cor=cor),Q(liderQuarto_id=lider)).order_by('nome')
    
        print encontristas
    return encontristas


def geraCrachaEncontrista(request):
    
    if(request.POST['cor']):
        cor = request.POST['cor']
    else:
        cor = None

    if(request.POST['liderQuarto']):
        lider = request.POST['liderQuarto']
    else:
        lider = None

    participantes = recuperaParticipantesCracha(cor,lider)

    return gerarCrachas(participantes)

  
 
def gerarCrachas(itens):
    pdf_file_name = 'Crachas'
    c = canvas.Canvas(pdf_file_name, pagesize=A4)
    qt = itens.__len__
    imagem = Image.open('gercontro/static/gercontro/imgs/cracha.png')
    print 'Gerando crachas. Aguarde...'
    i = 1
    for nome, sobrenome, igreja,lider in itens:	
        print nome
        print sobrenome
        print igreja
        print lider
        
        while (i<5 or nome):
            if (i== 1):
                altImagem = 620
                altNome = 710
                altLider = 670
                altIgreja = 630
            elif (i == 2):
                altImagem = 420
                altNome = 510
                altLider = 470
                altIgreja = 430
            elif (i == 3):
                altImagem = 220
                altNome = 310
                altLider = 270
                altIgreja = 230
            elif (i == 4):
                altImagem = 20
                altNome = 110
                altLider = 70
                altIgreja = 30

            #primeiro cracha
            c.drawImage(imagem.filename, 10,altImagem, width=290, height=200)		
            c.setFont('Helvetica-Bold',14,leading=None)
            c.drawString(80,altNome,nome.title()+' '+sobrenome.title())

            c.setFont('Helvetica-Bold',14,leading=None)
            c.drawString(80,altLider,lider.title())

            c.setFont('Helvetica-Bold',14,leading=None)
            c.drawString(80, altIgreja,igreja)

            #segundo cracha
            c.drawImage(imagem.filename, 300,altImagem, width=290, height=200)
            c.setFont('Helvetica-Bold',14,leading=None)
            c.drawString(370,altNome,nome.title()+' '+sobrenome.title())

            c.setFont('Helvetica-Bold',14,leading=None)
            c.drawString(370,altLider,lider.title())

            c.setFont('Helvetica-Bold',14,leading=None)
            c.drawString(370, altIgreja,igreja)

            if (i == 4):
                c.showPage()
            i+=1

    try:
        c.save()
        print '\nArquivo gerado com sucesso!'
    except Exception, e:
        raise e
