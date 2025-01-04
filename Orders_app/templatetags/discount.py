from django import template

register = template.Library()


@register.simple_tag(name="get_discounted_total")
def get_discounted_total(cart, discount):
    """
    Calculate the discounted total price of items in the cart.
    """
    total = sum(item.quantity * item.products.price for item in cart.added_items.all())
    result = total - (total * (discount / 100))
    return result
