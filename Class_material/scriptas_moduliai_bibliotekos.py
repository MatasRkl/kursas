"""
1. Reikia parašyti funckiją, kuri turėtų du variable – vienas yra listas,
 kitas – iš kokio skaičiaus reikia kad dalintusi. Reikia grazinti visus skaicius kurie dalinasi is duoto skaiciaus.
"""


# def numbers_divide(lst, x):
#     return [number for number in lst if number % x == 0]
#
#
# print(numbers_divide([5, 10, 18], 5))

"""
2. Parašyti funciją, į kurią padavus skaičių atspausdintų tokia
 tvarka kaip parodyta žemiau. Funkcija turi priimti 2 variable – nuo kurio iki kurio skaiciaus.: 

1 
22 
333 
4444 
55555 
Pvz jei nuo 3 iki 5, spausdina: 
333 
4444 
55555 
"""


# def print_numbers(first_number, second_number):
#     output = ('')
#     while first_number <= second_number:
#         output += str(first_number) * first_number +'\n'
#         first_number += 1
#     return output
#
#
# print(print_numbers(4, 9))

"""
3. Write a Program to extract each digit from an integer in the reverse order. 
For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits. 
"""


# def reverse(few_digits_number):
#      reversed_number = ' '.join(str(few_digits_number)[::-1])
#      return reversed_number
#
#
# print(reverse(5897))


"""
1. Sukurkite paprastą skaičiavimo programą kaip skriptą ir kaip modulį.
"""

# from functions.add_sub_multi import add, subtract, multiply
#
# num1 = 10
# num2 = 20
#
# print(add(num1, num2))
# print(subtract(num1, num2))
# print(multiply(num1, num2))

"""
2. Sukurkite programą su 3 skirtingais moduliais:

Pirma, atlikti pagrindines užduotis su string

antra, pagrindinius uždavinius su list.

trečias, pagrindiniai uždaviniai su float/ int

Importuokite juos kaip modulius į main.py modulį ir parodykite skaičiavimus.
"""

# from functions import integer_float_functions, list_functions, string_functions
#
# x = 10
# y = 5
# print(integer_float_functions.add(x, y))
# print(integer_float_functions.multiply(x, y))
# print(integer_float_functions.subtract(x, y))
# print(integer_float_functions.divide(x, 0))
#
# text = 'I have a giant yacht in Miami'
#
# print(string_functions.reverse(text))
# print(string_functions.count_vowels(text))
# print(string_functions.caps_on_words(text))
#
# my_list = [87, 1000, 567]
#
# print(list_functions.sort_list(my_list))
# print(list_functions.find_max(my_list))
# print(list_functions.find_min(my_list))

"""
3.Sukurkite modulį ir importuokite bet kurį pasirinktą PIP paketą. Tada sukurkite funkciją, kuri jį naudotų.
 Importuokite tą funkciją į main.py modulį ir ją naudokite.
"""

# from functions.pip_functions import get_joke
#
# x = input('Do you wanna hear a joke: ')
#
# if x == 'Yes':
#     get_joke()
# else:
#     print('Thats sad')


"""
4. "Python" modulis os suteikia galimybę naudotis
 nuo operacinės sistemos priklausančiomis funkcijomis, pvz., skaityti arba rašyti į failų sistemą. Jūsų užduotis yra:

Importuoti os modulį.

Sukurti funkciją, kuri išvardytų visus dabartiniame kataloge esančius failus.

Sukurti funkciją, kuri sukuria naują katalogą.

Sukurti funkciją, kuri pervadina failą.

Sukurkite funkciją, kuri perkelia failą iš vieno katalogo į kitą.

Sukurkite funkciją, kuri ištrina failą.
"""

# import os

# os.listdir(...)
# os.mkdir(...)
# os.mknod(...)
# os.rename(...)
# os.path.exists(...)
# os.path.join(...)
# os.remove(...)


# def name_all_files(): #leksikografine tvarka isrusiuoja
#     return os.listdir()
#
# #ab
# #aaab
#
# print(name_all_files())


# def create_new_catalog():
#     os.mkdir('C:/Users/Mano/Desktop/Betkas')
#
#
# create_new_catalog()


# def rename_file():
#     os.rename('C:/Users/Mano/Desktop/Betkas', 'C:/Users/Mano/Desktop/viskas')
#
# rename_file()


# def move_file():
#     os.rename('C:/Users/Mano/Desktop/viskas', 'C:/Users/Mano/Desktop/testas/viskas')
#
# move_file()


# def delete_file():
#     os.remove('C:/Users/Mano/Desktop/halou.txt')
#
# delete_file()
