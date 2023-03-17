from django.forms import ModelForm
from .models import Carro,Cliente,Aluguel

class CarroForm(ModelForm):
    class meta:
        model = Carro
        fields = ['placa,' 'marca', 'ano', 'modelo', 'data_compra']


    class AluguelForm(ModelForm):
        class meta:
            model = Cliente
            fields = ['codigo,' 'data_aluguel', 'data_entrega', 'diaria', 'placa' 'cpf']


        class ClientesForm(ModelForm):
            class meta:
                model = Cliente 
                fields = ['cpf,' 'nome', 'telefone', 'data_nascimento', 'endereço']
