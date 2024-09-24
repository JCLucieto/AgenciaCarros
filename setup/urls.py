from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from agencia.views import (

                           # home, consultar_carros, cadastrar_carro, alterar_carro, deletar_carro,
                           # consultar_fabricantes, cadastrar_fabricante, alterar_fabricante, deletar_fabricante,

                           Home, ConsultarCarros, DetalhesCarro, CadastrarCarro, AlterarCarro, DeletarCarro,
                           ConsultarFabricantes, DetalhesFabricante, CadastrarFabricante, AlterarFabricante, DeletarFabricante)

from usuarios.views import cadastrar_usuario, login, logout


#--------------------------------------------------------------
#     URL                  Função que chama em views.py
#    'xyz/'                mostra_xyz
#--------------------------------------------------------------

urlpatterns = [

    path('admin/',                       admin.site.urls),

    path('',                             Home.as_view(),                    name = 'home'),

    path('login/',                       login,                             name = 'login'),
    path('logout/',                      logout,                            name = 'logout'),

    path('consultar_carros/',            ConsultarCarros.as_view(),         name = 'consultar_carros'),
    path('cadastrar_carro/',             CadastrarCarro.as_view(),          name = 'cadastrar_carro'),
    path('carro/<int:pk>/detalhes',      DetalhesCarro.as_view(),           name = 'detalhes_carro'),
    path('carro/<int:pk>/alterar',       AlterarCarro.as_view(),            name = 'alterar_carro'),
    path('carro/<int:pk>/deletar',       DeletarCarro.as_view(),            name = 'deletar_carro'),

    path('consultar_fabricantes/',       ConsultarFabricantes.as_view(),    name = 'consultar_fabricantes'),
    path('cadastrar_fabricante/',        CadastrarFabricante.as_view(),     name = 'cadastrar_fabricante'),
    path('fabricante/<int:pk>/detalhes', DetalhesFabricante.as_view(),      name = 'detalhes_fabricante'),
    path('fabricante/<int:pk>/alterar',  AlterarFabricante.as_view(),       name = 'alterar_fabricante'),
    path('fabricante/<int:pk>/deletar',  DeletarFabricante.as_view(),       name = 'deletar_fabricante'),

    path('cadastrar_usuario/',           cadastrar_usuario,                 name = 'cadastrar_usuario'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
