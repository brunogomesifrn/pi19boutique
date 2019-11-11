from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Tipo, Produto
from .forms import TipoForm, ProdutoForm



def index(request):
	return render( request, 'index.html')

def usuario(request):
	usuario = request.user

	contexto = {
		'usuario': usuario,
	}
	return render(request, 'usuario.html', contexto)





