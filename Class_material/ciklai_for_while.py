"""
CIKLAI WHILE FOR
"""
# a = 5
# b = 5
# if a == b:
#     print(a + b)
#
# import time
#
# i = 10
# while i > 5:
#     print(i)
#     i += 1
#     time.sleep(1)
#     if i == 15:
#         break
# else:
#     print('Good evening')
#
# for i in range(10):
#     if i == 8:
#         break
#     if i == 5:
#         continue
#     print(i)
#
#
#
"""
ctrl+d = dubliuoja eilute
ctrl+shift+rodykle= nesa eilute
ctrl+click=nuvedimas i funkcija
"""
#
#
#
"""
1.Sukurkite kintamuosius, kuriuose reprezentuotų vartotojo vardą ir slaptažodį. Pradėkite begalinį ciklą,
 leidžiantį įvesti vartotojo vardą ir slaptažodį. Jei duomenys teisingi, sustabdykite begalinį ciklą ir
  išspausdinkite pasisveikinimo pranešimą.
"""
#
# name = 'Matas'
# password = 'Gerasoras2024'
#
# while True:
#     name_input = input('Type your username: ')
#     password_input = input('Type your password: ')
#     if name_input == name and password_input == password:
#         print(f'Welcome back {name_input}')
#         break
"""
2.Leiskite naudotojui įvesti 10 sveikųjų skaičių, tada spausdinkite šių įvestų skaičių sumą ir vidurkį.
"""
#
# input_numbers = []
# for i in range(10):
#     number = int(input('Type your number: '))
#     input_numbers.append(number)
#
# print(sum(input_numbers))
# print(sum(input_numbers) / len(input_numbers))
#
"""
3.Sugeneruokite dict iš 10 skaitmenų (keys): 1,2,3...10. Kiekvienam key turėtų būti priskirta atsitiktinio
 sveikojo skaičiaus vertė nuo 1 iki 100.
"""
# import random
# numbers_dict = {}
# for i in range(1, 11):
#     numbers_dict[i] = random.randint(1, 100)
# print(numbers_dict)
"""
4.Sukurkite PIN kodo nulaužimo programą. Tarkime, PIN kodą sudaro 4 atsitiktiniai skaitmenys. Reikšmę galite
 saugoti kintamajame. Tada sukurkite ciklą, einantį per visas galimas kombinacijas, kol rasite tą, kurią įvedėte.
"""
#
# import random
#
# pin = str(random.randint(0, 9999)).zfill(4)
# print('Pin code:', pin)
# attempts = 0
# while True:
#     attempts = attempts + 1
#     if str(random.randint(0, 9999)).zfill(4) == pin:
#         print('Correct pin: ', pin)
#         print('Attempts: ', attempts)
#         break
"""
5.Sukurkite programą, kuri leistų naudotojui įvesti skaičių seriją ir apskaičiuotų visų skaičių vidurkį. Programa
 taip pat turėtų išspausdinti visų skaičių list'a ir vidurkį.
"""
# number_list = []
# for i in range(5):
#      number = int(input('Type your number: '))
#      number_list.append(number)
#
# print(number_list)
# print(sum(number_list) / len(number_list))

number_list = []
any_numbers = input('Write numbers separated by spaces: ')
for x in any_numbers.split():
    number_list.append(int(x))

print(number_list)
print(sum(number_list) / len(number_list))


# numbers_list = list(map(int, any_numbers.split()))
# print(numbers_list)
