from django.forms import ModelForm
from .models import Tipo, Produto
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser 

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ('username', 'email', 'cpf')
		widgets = {
			'cpf': forms.TextInput(attrs={'placeholder': 'Somente Números'})
		}
		

class TipoForm(ModelForm):
	class Meta():
		model = Tipo
		fields = ['nome']

class ProdutoForm(ModelForm):
	class Meta():
		model = Produto
		fields = ['nome', 'valor', 'foto']
