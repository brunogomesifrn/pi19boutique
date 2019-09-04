from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Tipo, Produto
from .forms import TipoForm, ProdutoForm

def paginainicial(request):
	return render( request, 'paginainicial.html')


#@login_required

def cadastro(request):
	form = UserCreationForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('usuario')

	contexto = {
		'form': form
	}
	return render(request, 'cadastro.html', contexto)

def usuario(request):
	lista = Produto.objects.all()

	contexto = {
	'lista_Produto': lista
	}
	return render(request, 'usuario.html', contexto)
