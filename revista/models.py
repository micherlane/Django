from django.db import models

class coleçao(models.Model):
    nome = models.CharField(max_length=20)


class caixa(models.Model):
    numero = models.IntegerField()
    etiqueta = models.CharField(max_length=20)
    cor = models.CharField(max_length=15)

class emprestimo(models.Model):
    data_emprestimo = models.DateField()
    data_devoluçao = models.DateField()

class revista(models.Model):
    numero_ediçao = models.IntegerField()
    ano = models.IntegerField()
    coleçao = models.ForeignKey(coleçao,on_delete=models.CASCADE)
    caixa = models.ForeignKey(caixa,on_delete=models.CASCADE)
    emprestimo = models.ForeignKey(emprestimo,on_delete=models.CASCADE)

grupo = (('1','Predio'),('2','Escola'))
class Amigo(models.Model):
    nome = models.CharField(max_length=100)
    nome_da_mae = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    grupo_amigo = models.CharField(max_length=100,choices=grupo)
    emprestimo = models.ForeignKey(emprestimo,on_delete=models.CASCADE)