class ShoppingCart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = request.session.setdefault('shopping', {})
        if cart == {}:
            self.session['shopping'] = cart
            self.cart = cart
            self.session.modified = True
        else:
            self.cart = cart

    def save(self):
        self.session['shopping'] = self.cart
        self.session.modified = True

    def add(self, product):
        if str(product.id) not in self.cart:
            self.cart[product.id] = {
                'product_id': product.id,
                'name': product.name,
                'price': product.price,
                'quantity': 1,
                'image': product.image.url
            }
        else:
            for key, value in self.cart.items():
                if key == str(product.id):
                    value['quantity'] += 1
                    value['price'] += product.price
                    break
        self.save()

    def subtract(self, product):
        if str(product.id) in self.cart:
            self.cart[str(product.id)]['price'] = float(self.cart[str(product.id)]['price'] - product.price)
            self.cart[str(product.id)]['quantity'] -= 1
            if self.cart[str(product.id)]['quantity'] == 0:
                del self.cart[str(product.id)]

        self.save()

    def remove(self, product):
        if str(product.id) in self.cart.keys():
            del self.cart[product.id]
            self.save()

    def clear(self):
        self.cart.clear()
        self.session['shopping'] = {}
        self.session.modified = True
