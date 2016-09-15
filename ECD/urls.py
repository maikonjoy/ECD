# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
import p_sitios
import p_encontros
import p_encontristas
import p_servos
import p_departamento
import p_escalas
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ECD.views.home', name='home'),
    # url(r'^ECD/', include('ECD.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'gercontro.views.home', name='home'),
	
	#URLs para Sitios
	url(r'^sitios', 'gercontro.views.sitios', name='sitios'),
	url(r'^i_sitios', 'gercontro.views.incluir_sitio', name='i_sitios'),
	url(r'^u_sitios', p_sitios.updateSitio, name='u_sitio'),
	url(r'^p_sitios', p_sitios.incluir, name='p_sitio'),
	url(r'^e_sitios', p_sitios.excluirSitio, name='e_sitio'),
    url(r'^recuperaSitio', p_sitios.recuperaSitio, name='recuperaSitio'),

	#URLs para Encontros
	url(r'^encontros', 'gercontro.views.encontros', name='encontros'),
	url(r'^i_encontros', 'gercontro.views.incluir_encontro', name='i_encontros'),
	url(r'^a_encontros', p_encontros.updateEncontro, name='u_encontro'),
	url(r'^p_encontros', p_encontros.incluir, name='p_encontro'),
	url(r'^e_encontros', p_encontros.excluirEncontro, name='e_encontro'),

	#URLs para encontristas
    url(r'^encontristas$', 'gercontro.views.encontristas', name='encontristas'),
	url(r'^i_encontristas$', 'gercontro.views.incluir_encontrista', name='i_encontristas'),
	url(r'^u_encontristas$', p_encontristas.updateEncontrista, name='u_encontrista'),
	url(r'^p_encontristas$', p_encontristas.incluir, name='p_encontrista'),
	url(r'^e_encontrista/$', p_encontristas.excluirEncontrista, name='e_encontrista'),
	url(r'^emiteCrachas', 'gercontro.views.emiteCrachas', name='emiteCrachas'),
    url(r'^revisarEncontristas', 'gercontro.views.revisarEncontristas', name='revisarEncontristas'),
    url(r'^revisaoEncontrista', p_encontristas.revisaoEncontrista, name='revisaoEncontrista'),
    url(r'^revisaoCracha', p_encontristas.revisaoCracha, name='revisaoCracha'),
    url(r'^geraCrachaEncontrista', p_encontristas.geraCrachaEncontrista, name='geraCrachaEncontrista'),

    #URLs para servos
    url(r'^servos$', 'gercontro.views.servos', name='servos'),
	#url(r'^i_servos$', 'gercontro.views.incluir_servo', name='i_servos'),
	url(r'^u_servos', p_servos.updateServo, name='u_servo'),
	url(r'^p_servos', p_servos.incluir, name='p_servo'),
	url(r'^e_servos', p_servos.excluirServo, name='e_servo'),

    #URLS para escalas
    url(r'^escalaServos','gercontro.views.escalaServos',name='escalaServos'),
    url(r'^i_escalas', p_escalas.incluir, name='i_escalas'),
    url(r'^e_escala', p_escalas.excluirEscala, name='e_escala'),
    url(r'^u_escala', p_escalas.updateEscala, name='u_escala'),
    url(r'^gerarArvoreEscalas',p_escalas.gerarArvoreEscalas,name='gerarArvoreEscalas'),

    #URLs para departamentos
    url(r'^departamentos$', 'gercontro.views.departamentos', name='departamentos'),
	#url(r'^i_departamentos$', 'gercontro.views.incluir_departamento', name='i_departamentos'),
	url(r'^u_departamentos', p_departamento.updateDepartamento, name='u_departamento'),
	url(r'^p_departamento', p_departamento.incluir, name='p_departamento'),
	url(r'^e_departamentos', p_departamento.excluirDepartamento, name='e_departamento'),
	url(r'^gerarArvore',p_departamento.gerarArvoreDptos,name='gerarArvore'),
    
    #URLs para igrejas
    url(r'^igrejas$', 'gercontro.views.igrejas', name='igrejas'),
    
    #url(r'^report_builder/', include('report_builder.urls')),
	#url(r'^p_encontros', p_encontros.start, name='p_encontros'),
	#url(r'^p_sitios', 'p_sitios.start', name='sitios'),
)
