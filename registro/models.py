import datetime
from django.db import models

class Batalhao(models.Model):
    nome = models.CharField(max_length=20, null=False, unique=True)
    def __str__(self):
        return self.nome
    
#TIPOS DE VIATURAS
class TipoVtCarros(models.Model):
    tipo = models.CharField(max_length=20, null=False, unique=True)
    def __str__(self):
        return self.tipo
    
class TipoVtMotos(models.Model):
    tipo =  models.CharField(max_length=20, null=False, unique=True)
    def __str__(self):
        return self.tipo
    
#PNEUS
class PneusCarros(models.Model):
    modelo = models.CharField(max_length=30, unique=True, null=False)
    def __str__(self):
        return self.modelo
    
class PneusMotoDianteiro(models.Model):
    modelo = models.CharField(max_length=30, unique=True, null=False)
    def __str__(self):
        return self.modelo
class PneusMotoTraseiro(models.Model):
    modelo = models.CharField(max_length=30, unique=True, null=False)
    def __str__(self):
        return self.modelo

#VIATURAS
class ViaturasCarros(models.Model):
    prefixo = models.CharField(max_length=20, null=False, unique=True)
    nome_carro = models.CharField(max_length=30, null=False)
    odometro = models.IntegerField(null=False)
    batalhao_origem = models.ForeignKey(Batalhao,null=False, on_delete = models.CASCADE)
    tipo_viatura = models.ForeignKey(TipoVtCarros, null=False, on_delete=models.CASCADE)
    pneu = models.ForeignKey(PneusCarros, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.prefixo
    
class ViaturasMotos(models.Model):
    prefixo = models.CharField(max_length=20, null=False, unique=True)
    nome_moto = models.CharField(max_length=30, null=False)
    odometro = models.IntegerField(null=False)
    batalhao_origem = models.ForeignKey(Batalhao, null=False, on_delete=models.CASCADE)
    tipo_viatura = models.ForeignKey(TipoVtMotos, null=False, on_delete=models.CASCADE)
    pneu_dianteiro = models.ForeignKey(PneusMotoDianteiro, null = False, on_delete = models.CASCADE)
    pneu_traseiro = models.ForeignKey(PneusMotoTraseiro, null = False, on_delete = models.CASCADE)

    def __str__(self):
        return self.prefixo

#TABELAS DE PEDIDOS 
class PedidosCarros(models.Model):
    pim = models.CharField(max_length=25, null=False, unique=True)
    viatura = models.ForeignKey(ViaturasCarros, on_delete=models.CASCADE, null=False)
    quantidade = models.IntegerField(null=False)
    data = models.DateField(default = datetime.date.today)
    def __str__(self):
        return self.pim
    
class PedidosMotos(models.Model):
    pim = models.CharField(max_length=25, null=False, unique=True)
    viatura = models.ForeignKey(ViaturasMotos, null=False, on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False)
    data = models.DateField(default = datetime.date.today)
    def __str__(self):
        return self.pim
    

