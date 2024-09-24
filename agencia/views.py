from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpRequest
from agencia.models import Carro
from agencia.models import Fabricante
from agencia.forms import CarroForm
from agencia.forms import FabricanteForm
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

# View como Função (FBV - Function Based View)
# def home(request):
#     logger.debug('Inicio')
#     if request.user.is_authenticated:
#         todos_os_carros = Carro.objects.all().order_by('fabricante__nome')
#         if "buscar" in request.POST:
#             nome_a_buscar = request.POST['buscar']
#             if nome_a_buscar:
#                 todos_os_carros = todos_os_carros.filter(modelo__icontains = nome_a_buscar).order_by('fabricante__nome')
#         return render(request, 'consultar_carros.html', {'carros': todos_os_carros} )
#     return redirect('login')  

# View como Classe (CBV - Class Based Views)
class Home(View):

    def get(self, request):
        logger.debug('Home - GET')
        if request.user.is_authenticated:
            todos_os_carros = Carro.objects.all().order_by('fabricante__nome')
            return render(request, 'consultar_carros.html', {'carros': todos_os_carros} )
        return redirect('login')   

    def post(self, request):
        logger.debug('Home - POST')   
        if request.user.is_authenticated:
            todos_os_carros = Carro.objects.all().order_by('fabricante__nome')
            if "buscar" in request.POST:
                nome_a_buscar = request.POST['buscar']
                if nome_a_buscar:
                    todos_os_carros = todos_os_carros.filter(modelo__icontains = nome_a_buscar).order_by('fabricante__nome')
            return render(request, 'consultar_carros.html', {'carros': todos_os_carros} )
        return redirect('login')   
     
   
# # View como Função
# def consultar_carros(request):
#     logger.debug('Inicio')
#     if request.user.is_authenticated:
#         todos_os_carros = Carro.objects.all().order_by('fabricante__nome')
#         if "buscar" in request.POST:
#             nome_a_buscar = request.POST['buscar']
#             if nome_a_buscar:
#                 todos_os_carros = todos_os_carros.filter(modelo__icontains = nome_a_buscar).order_by('fabricante__nome')
#         return render(request, 'consultar_carros.html', {'carros': todos_os_carros} )
#     return redirect('login')   

# View como Classe  (CBV Class Based Views)  -  Classe mais básica = View
class ConsultarCarros(View):
    
    def get(self, request):
        logger.debug('GET')
        if request.user.is_authenticated:
            todos_os_carros = Carro.objects.all().order_by('fabricante__nome')
            return render(request, 'consultar_carros.html', {'carros': todos_os_carros} )
        return redirect('login') 

    def post(self, request):
        logger.debug('POST')
        if request.user.is_authenticated:
            todos_os_carros = Carro.objects.all().order_by('fabricante__nome')
        if "buscar" in request.POST:
            nome_a_buscar = request.POST['buscar']
            if nome_a_buscar:
                todos_os_carros = todos_os_carros.filter(Q(modelo__icontains=nome_a_buscar) | 
                                                         Q(fabricante__nome__icontains=nome_a_buscar)).order_by('fabricante__nome')
            return render(request, 'consultar_carros.html', {'carros': todos_os_carros} )
        return redirect('login') 

# View como Classe  (CBV Class Based Views)  -  Classe mais específica = ListView
# No nosso caso, como estamos verificando se o usuario está autenticado não há
# muito ganho em relação a View normal. Se não estivessemos vericando a autenticação
# do usuario seriam apenas 3 linha
#
#   model = Carro
#   template_name = 'consultar_carros.html'
#   context_object_name = 'carros'
#

# View como Função
# def cadastrar_carro(request):
#     logger.debug('Inicio')
#     if request.user.is_authenticated:    
#         if request.method == 'POST':
#             form = CarroForm(request.POST, request.FILES)
#             if form.is_valid():
#                 form.save()
#                 return redirect ('consultar_carros')
#         else:
#             form = CarroForm()
#         return render(request, 'cadastrar_carro.html', {'carroform' : form})
#     return redirect('login')  

# View como Classe - Herdando de Classe Básica (View)
class CadastrarCarro(View):

    def get(self, request):
        logger.debug('GET')
        if request.user.is_authenticated:
            form = CarroForm()
            return render(request, 'cadastrar_carro.html', {'carroform' : form})
        return redirect('login')  

    def post(self, request):
        logger.debug('POST')
        if request.user.is_authenticated:
            form = CarroForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect ('consultar_carros')
            return render(request, 'cadastrar_carro.html', {'carroform' : form})
        return redirect('login')  


# View como Classe - Herdando de Classe (DetailView)
@method_decorator(login_required(login_url = 'login'), name = 'dispatch')
class DetalhesCarro(DetailView):
    logger.debug('Inicio')
    model = Carro
    template_name = 'detalhes_carro.html'
    

# View como Classe
@method_decorator(login_required(login_url = 'login'), name = 'dispatch')
class AlterarCarro(UpdateView):
    logger.debug('Inicio')
    model = Carro
    form_class = CarroForm
    template_name = 'alterar_carro.html'
    #success_url = '/consultar_carros/'

    def get_success_url(self):
        return reverse_lazy('detalhes_carro', kwargs={'pk' : self.object.pk})


# View como Função
@method_decorator(login_required(login_url = 'login'), name = 'dispatch')
class DeletarCarro(DeleteView):
    logger.debug('Inicio')
    model = Carro
    template_name = 'deletar_carro.html'
    success_url = '/consultar_carros/'


# View como Classe  (CBV Class Based Views)  -  Classe mais básica = View
class ConsultarFabricantes(View):
    
    def get(self, request):
        logger.debug('GET')
        if request.user.is_authenticated:
            todos_os_fabricantes = Fabricante.objects.all().order_by('nome')
            return render(request, 'consultar_fabricantes.html', {'fabricantes': todos_os_fabricantes} )
        return redirect('login') 

    def post(self, request):
        logger.debug('POST')
        if request.user.is_authenticated:
            todos_os_fabricantes = Fabricante.objects.all().order_by('nome')
        if "buscar" in request.POST:
            nome_a_buscar = request.POST['buscar']
            if nome_a_buscar:
                todos_os_fabricantes = todos_os_fabricantes.filter(nome__icontains=nome_a_buscar).order_by('nome')
            return render(request, 'consultar_fabricantes.html', {'fabricantes': todos_os_fabricantes} )
        return redirect('login') 


# View como Classe - Herdando de Classe (DetailView)
@method_decorator(login_required(login_url = 'login'), name = 'dispatch')
class DetalhesFabricante(DetailView):
    logger.debug('Inicio')
    model = Fabricante
    template_name = 'detalhes_fabricante.html'
    

# # View como Função
# def cadastrar_fabricante(request):
#     logger.debug('Inicio')
#     if request.user.is_authenticated:  
#         return render(request, 'cadastrar_fabricante.html')
#     return redirect('login')  


# View como Classe - Herdando de Classe Básica (View)
class CadastrarFabricante(View):

    def get(self, request):
        logger.debug('GET')
        if request.user.is_authenticated:
            form = FabricanteForm()
            return render(request, 'cadastrar_fabricante.html', {'fabricanteform' : form})
        return redirect('login')  

    def post(self, request):
        logger.debug('POST')
        if request.user.is_authenticated:
            form = FabricanteForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('consultar_fabricantes')
            return render(request, 'cadastrar_fabricante.html', {'fabricanteform' : form})
        return redirect('login')  

    
# # View como Função
# def alterar_fabricante(request):
#     logger.debug('Inicio')
#     if request.user.is_authenticated: 
#         return render(request, 'alterar_fabricante.html')
#     return redirect('login')  


# View como Classe
@method_decorator(login_required(login_url = 'login'), name = 'dispatch')
class AlterarFabricante(UpdateView):
    logger.debug('Inicio')
    model = Fabricante
    form_class = FabricanteForm
    template_name = 'alterar_fabricante.html'
    #success_url = '/consultar_fabricantes/'

    def get_success_url(self):
        return reverse_lazy('detalhes_fabricante', kwargs={'pk' : self.object.pk})


# # View como Função
# def deletar_fabricante(request):
#     logger.debug('Inicio')
#     if request.user.is_authenticated: 
#         return render(request, 'deletar_fabricante.html')
#     return redirect('login')  

# # View como Função
# @method_decorator(login_required(login_url = 'login'), name = 'dispatch')
# class DeletarFabricante(DeleteView):
#     logger.debug('Inicio')
#     model = Fabricante
#     template_name = 'deletar_fabricante.html'
#     success_url = '/consultar_fabricantes/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class DeletarFabricante(DeleteView):
    model = Fabricante
    template_name = 'deletar_fabricante.html'
    success_url = '/consultar_fabricantes/'

    def post(self, request, *args, **kwargs):
        fabricante = self.get_object()
        if Carro.objects.filter(fabricante=fabricante).exists():
            messages.error(request, 'Não é possível deletar este fabricante porque existem carros associados a ele.')
            # Permanece na mesma página
            return render(request, self.template_name, {'object': fabricante})

        # Se não houver carros associados, deleta o fabricante
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)

