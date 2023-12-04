"""mirempet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from landpage.views import home,Eventos,Eventos_detalhes,formulario,convidadeo,pacoteparticipacao,patrocinio,formularioEmpresa,formularioEntreEmpresa,formularioEmpresaPatrocinio,formulario_empresa
from django.conf.urls.static import static
from django.conf import settings
from landpage.views import download_folder

urlpatterns = [

    #path('Eventos',home),
    #path('Painel-Controle',admin.site.urls),
    #path('download/<id>', download_folder, name='download'),
    #path('', Eventos, name='download'),
    path('',Eventos_detalhes,),
    #path('Registrar',formulario),
    #path('Registrar-Empresa',formularioEmpresa),
    #path('Registos-entre-empresa',formularioEntreEmpresa),
    #path('Registos-de-Patrocinio',formularioEmpresaPatrocinio),


    #path('convidado/<id>',convidadeo),
    #path('Pacote-de-participacao',pacoteparticipacao),
    #path('Pacote-de-Patrocinio',patrocinio),
    #path('Empresa-Participante/<id>',formulario_empresa),
 



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
