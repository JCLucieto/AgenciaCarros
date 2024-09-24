from django.db import models

class Fabricante(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=15, blank=False, null=False)

    # Subscreve str de models.Model para não mostrar no admin "Object(n)" e sim o nome do frabricante
    def __str__(self):
        return self.nome


class Carro(models.Model):
    id = models.AutoField(primary_key=True)
    fabricante = models.ForeignKey(Fabricante, on_delete = models.PROTECT, related_name = 'carro_fabricante')
    modelo = models.CharField(max_length=30)
    ano =  models.IntegerField(blank=False, null=False)
    cor = models.CharField(max_length=20)
    placa = models.CharField(max_length=10, blank=True, null=True)
    preco = models.FloatField(max_length=9, blank=False, null=False)
    foto = models.ImageField(upload_to='fotos/')

    # Subscreve str de models.Model para não mostrar no admin "Object(n)" e sim o modelo do carro
    def __str__(self):
        return self.modelo
    
