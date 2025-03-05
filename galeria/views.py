from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Sua principal função e cuidar do que vai ser exibido em cada pagina, ou o que vai ser exibido e seu conteudo

def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')