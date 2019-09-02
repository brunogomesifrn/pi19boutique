from django.forms import ModelForm
from .models import Tipo, Produto

class TipoForm(ModelForm):
	class Meta():
		model = Tipo
		fields = ['nome']

class ProdutoForm(ModelForm):
	class Meta():
		model = Produto
		fields = ['nome', 'valor', 'foto']