from tempfile import template

from shopping_cart.templatetags.cart_template_tag import register


@register.filter
def count_true(value):
    return value.filter(boolean_field=True).count()
