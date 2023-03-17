from django.db import models

# Create your models here.
class Carro(models.Model):
    placa = models.CharField(max_length=15)
    marca = models.CharField(max_length=15)
    ano = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    data_compra = models.DateField()


    def __str__(self):
        return self.modelo

class Cliente(models.Model):
    cpf = models.CharField(max_length=15)
    nome = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField(max_length=15)
    endereço = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Aluguel(models.Model):
    codigo = models.IntegerField(primary_key=True, unique=True)
    data_aluguel = models.DateField()
    data_entrega = models.DateField()
    diaria = models.DecimalField(max_digits=10, decimal_places=2)
    placa = models.ForeignKey(Carro, on_delete=models.CASCADE)
    cpf = models.ForeignKey(Cliente, on_delete=models.CASCADE)