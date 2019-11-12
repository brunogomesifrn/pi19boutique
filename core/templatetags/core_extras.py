from django import template

register = template.Library()

@register.filter
def curtido(produto, usuario):
    return produto.curtido(usuario)