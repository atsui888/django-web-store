from django import template


def currency_euro(value):
    return f"{value:.2f} €"


register = template.Library()

register.filter("currency_euro", currency_euro)  # name of the filter, function
