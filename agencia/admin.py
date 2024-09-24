from django.contrib import admin
from agencia.models import Carro
from agencia.models import Fabricante

# Para definir a forma de apresentação na página web do admin:
# 1 - que colunas aparecem
# 2 - que colunas possuem links para acessar a linha (registro)
# 3 - que campos para consulta são disponibilizados (a virgula é necessária quando só 1 item)
# 4 - que colunas para filtro
# 5 - quantos registros mostra por página
# 6 - que colunas são editáveis

class ListaFabricantes(admin.ModelAdmin):
    ''' Classe que lista os Fabricantes '''
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('nome',)
    list_per_page = 10

# Para aparecer na página web do admin com a apresentação acima
admin.site.register(Fabricante, ListaFabricantes)

class ListaCarros(admin.ModelAdmin):
    ''' Classe que lista os Carros '''
    list_display = ('id', 'fabricante', 'modelo', 'ano', 'cor', 'placa', 'preco')
    list_display_links = ('id', 'fabricante', 'modelo')
    search_fields = ('modelo',)
    list_filter = ('fabricante', 'modelo',)
    list_per_page = 10

# Para aparecer na página web do admin com a apresentação acima
admin.site.register(Carro, ListaCarros)

