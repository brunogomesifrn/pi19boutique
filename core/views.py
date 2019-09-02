from django.shortcuts import render

def paginainicial(request):
	return render('paginainicial.html')

def cadastro(request):
	return render('cadastro.html')

def login(request):
	return render('login.html')

def usuario(request):
	return render('usuario.html')
