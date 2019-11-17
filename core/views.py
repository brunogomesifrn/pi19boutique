from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Produto, Favoritados
from .forms import ProdutoForm
from django.contrib.admin.views.decorators import staff_member_required



def index(request):
	return render(request, 'index.html')

def usuario(request):
	usuario = request.user
	lista = Produto.objects.all()

	contexto = {
	'lista_Produto': lista
	}
	if usuario.is_staff:
		return render(request, 'info.html', contexto)
	return render(request, 'usuario.html', contexto)

@staff_member_required(login_url='index')
def produto(request):
	form = ProdutoForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		form.save()
		return redirect('usuario')
	
	contexto = {
	'form': form
	}
	return render(request, 'produto.html', contexto)


def produto_favoritar(request, id):
	produto = Produto.objects.get(pk=id)
	Favoritados.objects.create(
		produto=produto,
		usuario=request.user
	)
	return redirect('usuario')

def excluir(request, id):
	lista = Produto.objects.get(pk=id)
	lista.delete()
	
	return redirect('usuario')
