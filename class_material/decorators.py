"""
1. Parašykite dekoratorių kuris riboja
parametrų kiekį (tarkime, ne daugiau negu 2 parametrai funkcijai)
"""

# def limiting_decorator(func):
#     def wrapper(*args, **kwargs):
#         if len(args) > 2:
#             return 'Arguments max count is 2'
#         return func(*args, **kwargs)
#     return wrapper
#
# @limiting_decorator
# def add(*args):
#     return sum(args)
#
# print(add(5, 10))

"""
2. Parašykite dekoratorių, kuris leidžia į funkciją įrašyti tik string tipo parametrus.
"""

# def string_decorator(func):
#     def wrapper(*args):
#         for a in args:
#             if type(a) != str:
#                 return 'Only string please'
#         return func(*args)
#     return wrapper
#
# @string_decorator
# def split_string(text):
#     return text.split()
#
# print(split_string('Hey, ho'))

"""
3. import requests  # importuojame requests
from time import time  # importuojame time modulį

start_time = time()  # fiksuojame starto laiką
r = requests.get('http://www.cnn.com')  # sukuriame http užklausą
print(r.status_code)  # spausdiname status code (200 = OK, 404 = Not Found, ir t.t. galima pasiguglinti http status codes)
end_time = time()  # fiksuojame pabaigos laiką
print(end_time - start_time)  # atspausdiname laiką, per kurį gaovme atsakymą


Parašykite dekoratorių, bet kokios funkcijos vykdymo laikui fiksuoti. Galite patobulinti, pvz funkcijos (vardas),
su tokiais ir tokiais argumentais vykdymo laikas - XX s.
Ištestuokite, su funkcija, grąžinančia svetainės atsako kodą ir su funkcija,
išrenkančia pirminius skaičius užduotame diapazone.
"""

# import requests
# from time import time
# from functools import wraps
#
# def speed_test(fn):
#     wraps(fn)
#     def wrapper(*args, **kwargs):
#         start_time = time()
#         fn(*args, **kwargs)
#         end_time = time()
#         runtime = end_time - start_time
#         print(f"Function's '{fn.__name__}', with given parameters {args} runtime: {round(runtime, 2)}s")
#     return wrapper
#
#
# @speed_test
# def get_status(website):
#     r = requests.get(website)
#     print(r.status_code)
#
#
# get_status('http://python.org')
#
# @speed_test
# def prime_finder(given_range):
#     final_list = []
#     for num in range(given_range):
#         if num > 1:
#             for i in range(2,num):
#                 if (num % i) == 0:
#                     break
#         else:
#             final_list.append(num)
#     return final_list
#
# prime_finder(10000)
