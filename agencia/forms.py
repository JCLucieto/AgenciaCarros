from django import forms
from agencia.models import Carro, Fabricante

class CarroForm(forms.ModelForm):  # Cria Forms a partir de um model
    class Meta:
        model = Carro
        labels = {'preco':'Preço',}
        fields = '__all__'

    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco < 20000:
            self.add_error('preco', 'Valor Mínimo Maior ou Igual a R$ 20.000,00')
        return preco
    
    def clean_ano(self):
        ano = self.cleaned_data.get('ano')
        if ano < 2000:
            self.add_error('ano', 'Não Aceitamos Carros Fabricados Antes de 2000')
        return ano
    


class FabricanteForm(forms.ModelForm):  # Cria Forms a partir de um model
    class Meta:
        model = Fabricante
        labels = {'nome':'Nome',}
        fields = '__all__'

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome or not nome.strip():
            self.add_error('nome', 'Nome Inválido')
        return nome