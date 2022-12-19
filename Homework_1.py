class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def total_price_for_product(self, quantity):
        return round(self.price * quantity, 2)


class ShoppingCart:
    def __init__(self) -> None:
        self.products = []
        self.quantities = []

    def add_product_to_cart(self, product: Product, quantity):
        self.products.append(product)
        self.quantities.append(quantity)

    def total_price_for_all(self):
        total = 0
        for (product, quantity) in zip(self.products, self.quantities):
            total += product.total_price_for_product(quantity)
        return round(total, 2)


product1 = Product("beer", 38)
product2 = Product("milk", 44.5)
product3 = Product('bar', 19.99)
product4 = Product('sausage', 30)
product5 = Product('pasta', 36)
product6 = Product('tomato', 7.7)

cart = ShoppingCart()
cart.add_product_to_cart(product1, 8)
cart.add_product_to_cart(product2, 1)
cart.add_product_to_cart(product3, 2)
cart.add_product_to_cart(product4, 0)
cart.add_product_to_cart(product5, 3)
cart.add_product_to_cart(product6, 7)

print(f'Total price for all products = {cart.total_price_for_all()} UAH')


