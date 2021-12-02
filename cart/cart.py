from decimal import Decimal

from django.conf import settings
from products.models import Product



class Cart:


    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, qty=1):
        """
        Adding and updating the users cart session data
        """
        product_id = str(product.id)

        if str(product.id) not in self.cart:
            self.cart[product_id]["qty"] = {'qty':0,"price": str(product.price)}

        else:
            self.cart[product_id]['qty']+=qty

        self.save()

    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return products
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]["product"] = product

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    def __len__(self):
        """
        Get the cart data and count the qty of items
        """
        return sum(item["qty"] for item in self.cart.values())



    def save(self):
        self.session.modified = True