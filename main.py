#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Challenge:

#. Implement ``Product`` class
#. Each ``Product`` instance should implement properties:
    * ``name`` - a product's name, like apple, cheese etc.
    * ``price`` - a price for a single unit
#. ``Product`` instance should have a behavior of calculating total
   price for a specified quantity of goods
#. Implement ``ShoppingCart`` class
#. ``ShoppingCart`` instance should combine products instances and
    corresponding purchased quantities.
#. ``ShoppingCart`` instance should implement a method to calculate
   the total price of entire cart.

"""
# the first task "class Product"
# 1 option of the first task "class Product" when quantity is given with the product


class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price_for_product(self):
        return self.price * self.quantity


product1 = Product("beer", 38, 8)
product2 = Product("milk", 44.5, 1)
product3 = Product('bar', 19.99, 2)
product4 = Product('sausage', 30, 0)
product5 = Product('pasta', 36, 3)
product6 = Product('tomato', 7.7, 7)

products = [product1, product2, product3, product4, product5, product6]
for product in products:
    print(f'Total price of {product.name} = {int(product.total_price_for_product())}')


# the first task "class Product"
# 2 option of the first task "class Product" when quantity is given by the client in the console


class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def total_price_for_product(self, quantity):
        return int(self.price * quantity)


product1 = Product("beer", 38)
product2 = Product("milk", 44.5)
product3 = Product('bar', 19.99)
product4 = Product('sausage', 30)
product5 = Product('pasta', 36)
product6 = Product('tomato', 7.7)

products = [product1, product2, product3, product4, product5, product6]

i = 0
while i < len(products):
    print(f'Total price of {products[i].name} = {products[i].total_price_for_product(int(input()))}')
    i += 1


# the first task "class Product"
# 3 option of the first task "class Product"
# which works in conjunction with # the second task "class ShoppingCart" below

class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def total_price_for_product(self, quantity):
        return int(self.price * quantity)


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
        return total


product1 = Product("beer", 38)
product2 = Product("milk", 44.5)
product3 = Product('bar', 19.99)
product4 = Product('sausage', 30)
product5 = Product('pasta', 36)
product6 = Product('tomato', 7.7)

cart = ShoppingCart()
cart.add_product_to_cart(Product("beer", 38), 8)
cart.add_product_to_cart(Product("milk", 44.5), 1)
cart.add_product_to_cart(Product('bar', 19.99), 2)
cart.add_product_to_cart(Product('sausage', 30), 0)
cart.add_product_to_cart(Product('pasta', 36), 3)
cart.add_product_to_cart(Product('tomato', 7.7), 7)

print(f'Total price for all products = {cart.total_price_for_all()} UAH')


