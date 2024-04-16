"""
1. Sukurkite keletą savo pavyzdžių, kuriuose parodytumėte ir panaudotumėt keletą OOP paradigmų praktikoje.
"""


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         pass
#
#
# class Tiger(Animal):
#     def speak(self):
#         return f"{self.name} says Rawr!"
#
#
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"
#
#
# tiger = Tiger("Lightning")
# print(tiger.speak())
#
# cat = Cat("Ginger")
# print(cat.speak())
#
#
# class Car:
#     def __init__(self):
#         self.__speed = 0
#
#     def accelerate(self):
#         self.__speed += 10
#
#     def get_speed(self):
#         return self.__speed
#
#     def alert(self):
#         if self.__speed >= 60:
#             print('SLOW DOWN WOOOW')
#
#
# my_car = Car()
# my_car.accelerate()
# my_car.accelerate()
# my_car.accelerate()
# my_car.accelerate()
# my_car.accelerate()
# my_car.accelerate()
# my_car.alert()
# print(my_car.get_speed())

"""
2. 3. Parašykite klasę CoffeeShop, kuri turi tris inicializuotos klasės kintamuosius:

name: str (iš esmės parduotuvės pavadinimas)

meniu : elementų sąrašas (list) (dict tipo), kuriame kiekvienas elementas turi elementą (elemento pavadinimą),
 tipą (ar tai maistas, ar gėrimas) ir kainą.

orders: tuščias list

ir septyni metodai:

add_order: į užsakymų sąrašo pabaigą įtraukia prekės pavadinimą, jei jis yra meniu, priešingu atveju grąžina
 "Šiuo metu šios prekės nėra!".

fulfill_order: jei užsakymų sąrašas nėra tuščias, grąžinama "{prekė} yra paruošta!". Jei užsakymų sąrašas tuščias,
 grąžinkite "Visi užsakymai įvykdyti!".

list_orders: grąžina priimtų užsakymų prekių pavadinimus, priešingu atveju - tuščią sąrašą.

due_amount: grąžina bendrą mokėtiną sumą už priimtus užsakymus.

cheapest_item: grąžina pigiausio meniu elemento pavadinimą.

drinks_only: grąžina tik meniu gėrimų tipo elementų pavadinimus.

food_only: grąžina tik meniu maisto tipo elementų pavadinimus.
"""


# class CoffeeShop:
#     def __init__(self, name, menu):
#         self._name = name
#         self._menu = menu
#         self._orders = []
#
#     def add_order(self, item):
#         if item in self._menu:
#             self._orders.append(item)
#             return f"{item} added to orders."
#         else:
#             return "This is not available"
#
#     def fulfill_order(self):
#         if self._orders:
#             order = self._orders.pop(0)
#             return f"{order} is ready!"
#         else:
#             return "All orders have been fulfilled!"
#
#     def list_orders(self):
#         return self._orders
#
#     def due_amount(self):
#         return sum(self._menu[item]['price'] for item in self._orders)
#
#
# class CheapCoffeeShop(CoffeeShop):
#     def cheapest_item(self):
#         cheapest_price = float('inf')
#         cheapest_item = None
#         for item in self._menu:
#             if self._menu[item]['price'] < cheapest_price:
#                 cheapest_price = self._menu[item]['price']
#                 cheapest_item = item
#         return cheapest_item
#
#     def drinks_only(self):
#         return [item for item in self._menu if self._menu[item]['type'] == 'drink']
#
#     def food_only(self):
#         return [item for item in self._menu if self._menu[item]['type'] == 'food']
#
#
# menu = {
#     'cola': {'type': 'drink', 'price': 3.50},
#     'kebab': {'type': 'food', 'price': 5.00},
#     'tea': {'type': 'drink', 'price': 2.00},
#     'cake': {'type': 'food', 'price': 4.00}
# }
#
# coffee_shop = CoffeeShop("MyCoffeeShop", menu)
# cheap_coffee_shop = CheapCoffeeShop("CheapCoffeeShop", menu)
#
# print(coffee_shop.add_order("cola"))
# print(coffee_shop.add_order("kebab"))
# print(coffee_shop.add_order("pizza"))
# print(coffee_shop.due_amount())
# print(coffee_shop.list_orders())
# print(coffee_shop.fulfill_order())
# print(coffee_shop.fulfill_order())
# print(coffee_shop.fulfill_order())
#
# print(cheap_coffee_shop.cheapest_item())
# print(cheap_coffee_shop.drinks_only())
# print(cheap_coffee_shop.food_only())

