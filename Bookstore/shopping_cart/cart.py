from decimal import Decimal
from django.conf import settings
from books.models import Product

class Cart(object):

    def __init__(self, request):
        """Initialize cart"""
        
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            #Make empty cart session
            cart = self.session[settings.CART_SESSION_ID] = {}
            self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        # Add item to cart or update the quantity
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        
        if update_quantity:
            self.cart[product_id] ['quantity'] = quantity
        else:
            self.cart[product_id] ['quantity'] += quantity
        
        self.save()

    def remove(self, product):
        # Remove a product from the cart

        product_id = str(product_id)
        if product_id in self.cart[product_id]
        self.save()

    def save(self):
        # Update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart

        # Mark the session as modified to make sure it's saved
        self.session.modified = True

    def __iter__(self):
        # Iterate over items in cart and get products from database

        product_ids = self.cart.keys()
        #get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product_ids)] ['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        # Count the  items in cart and return the total
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        # Empty the cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['price'] * item['quantity'] for item in self.cart.values()))
    