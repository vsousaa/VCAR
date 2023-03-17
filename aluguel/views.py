from django.shortcuts import render, redirect
from .models import Carro
from .forms import CarroForm


def index(request):

     return render(request, "index.html")  

def listar_carro(request):
        carros = Carro.objects.all()
        context = {"carros": carros}
        return render(request, "carro/listar.html", context)

def detalhar_autor(request, pk):
        carro = Carro.objects.get(pk=pk)
        context = {"carro": carro}
        return render(request, "carro/detalhar.html", context)

def cadastrar_carro(request):
        if request.method == "POST":
            form = CarroForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                form = CarroForm()
                return render(request, "carro/cadastrar.html", {'form': form})
        else:
            form = AutorForm()
            return render(request, "carro/cadastrar.html", {'form': form})
