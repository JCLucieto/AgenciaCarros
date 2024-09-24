from django import template
import locale

register = template.Library()


@register.filter(name='format_preco')
def format_preco(value):
    try:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(value, symbol='R$', grouping=True)
    except (TypeError, ValueError):
        return value
