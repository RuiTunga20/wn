from django.contrib import admin
from landpage.models import *

# Register your models here.
admin.site.register(Pacotes)
admin.site.register(Pacotes_Patrocinio)
admin.site.register(Inscricao_empresa)

admin.site.login_template = '../Paginas/admin/login.html'




@admin.register(encontrosb2b)
class encontrosb2bAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'email','telefone','estado')  # Colunas exibidas na lista
    list_filter = ('estado',)  # Filtro por estado
    search_fields = ('id','nome', 'email')  # Pesquisa por nome ou email
    list_editable = ('estado',)
    list_display_links=('nome',)


@admin.register(EmpresaPatrocinio)
class EmpresaPatrocinioAdmin(admin.ModelAdmin):
    list_display = ('id','nome','email','telefone','estado')  # Colunas exibidas na lista
    list_filter = ('estado',)  # Filtro por estado
    search_fields = ('id','nome', 'email')  # Pesquisa por nome ou email
    list_editable = ('estado',)  # 
    list_display_links=('nome',)

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'cargo', 'empresa', 'email','telefone','estado')  # Colunas exibidas na lista
    list_filter = ('estado',)  # Filtro por estado
    search_fields = ('id','nome', 'email')  # Pesquisa por nome ou email
    list_editable = ('estado',)  # Torna o estado editável diretamente na lista
    list_display_links=('nome',)


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'email','telefone','estado')  # Colunas exibidas na lista
    list_filter = ('estado',)  # Filtro por estado
    search_fields = ('id','nome', 'email')  # Pesquisa por nome ou email
    list_editable = ('estado',)  # Torna o estado editável diretamente na lista
    list_display_links=('nome',)
