"""
1. Parašykite funkciją, kuri paima du list'us ir prie pirmojo list pirmojo elemento
 prideda antrojo listpirmąjį elementą,
 antrojo sąrašo antrąjį
 elementą, antrojo sąrašo antrąjį elementą ir antrojo sąrašo antrąjį elementą. pirmąjį sąrašą su
  antruoju antrojo sąrašo elementu ir t. t., ir t. t. Grąžinkite True, jei visi elementų deriniai sudaro
   tą patį skaičių. Priešingu atveju grąžinama False.
"""


# def puzzle_pieces(lst1, lst2):
#
#     target_sum = lst1[0] + lst2[0]
#     for i in range(1, len(lst1)):
#         if lst1[i] + lst2[i] != target_sum:
#             return False
#     return True
#
#
# print(puzzle_pieces([5, 6, 8, 9], [6, 7, 9, 5]))


"""
2. Tarp lyginių ir nelyginių skaičių vyksta didelis karas.
 Šiame kare jau žuvo daug skaičių, todėl tavo užduotis - jį nutraukti.
 Jūs turite nustatyti, kurios grupės sumos didesnės: lyginių ar nelyginių. Laimi didesnė grupė.
Sukurkite funkciją, kuri paimtų sveikųjų skaičių sąrašą, atskirai suskaičiuotų lyginių ir nelyginių skaičių sumas,
 tada grąžintų lyginių ir nelyginių skaičių sumų skirtumą skaičių.
"""


# def war_of_numbers(numbers):
#     sum_even = sum(number for number in numbers if number % 2 == 0)
#     sum_odd = sum(number for number in numbers if number % 2 != 0)
#     if sum_even > sum_odd:
#         return sum_even - sum_odd
#     else:
#         return sum_odd - sum_even
#
#
# print(war_of_numbers([5, 9, 7, 8, 6]))


"""
3. Jums duotas bigramų masyvas ir žodžių masyvas. Parašykite funkciją,
 kuri grąžintų True, jei iš šio masyvo galima rasti kiekvieną bigramą bent vieną kartą žodžių masyve.
"""


# def can_find(bigrams, words):
#     for bigram in bigrams:
#         found = False
#         for word in words:
#             if bigram in word:
#                 found = True
#                 break
#         if not found:
#             return False
#     return True
#
#
# print(can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]))

"""
4. Sukurkite funkciją, kuri priima eilučių sąrašą ir grąžina naują sąrašą,
 kuriame yra tik tos eilutės, kurios prasideda balsiu.
"""


# def string_starts_with_vowel(lst1: [str]):
#     vowels = "AEIOUYaeiouy"
#     return [word for word in lst1 if word[0] in vowels]
#
#
# print(string_starts_with_vowel(["Apple", "tiger"]))

"""
5. Sukurkite lambda funkciją, kuri:

priima du argumentus: eilutę ir skaičių.

grąžina naują eilutę, kuri pakartoja pradinę eilutę tiek kartų, kiek kartų pakartotas skaičius.
 Pavyzdžiui, jei įvesties duomenys yra Hello ir 3, funkcija turėtų grąžinti HelloHelloHello.
"""


# def repeator(st, num):
#     return st * num
#
#
# print(repeator("CODE ME ", 5))
#
# """
# Lambda function
# """
#
#
# def multiply(x: int, y: int) -> int:
#     return x * y
#
#
# print(multiply(2, 3))


"""
1. Write a Python program to triple all numbers of a given list of integers. Use Python
"""

# list_of_ints = [5, 9, 8, 7, 5]
# def triple_number():
#     new = []
#     for num in list_of_ints:
#         new.append(num * 3)
#     return new
#
# print(triple_number())

"""
2. Write a Python program to square the elements of a list using map() function.
"""

# numbers_list = [6, 17, 7, 19]
# squared_elements = list(map(lambda x: x ** 2, numbers_list))
# print(squared_elements)

"""
3. Write a Python program to add three given lists using Python map and lambda
"""

# def add_lists(*args: list[int]):
#     result = []
#     [result.append(number) for number in args]
#     one_list = sum(result, [])
#     return one_list
#
# print(add_lists([5, 7, 8], [8, 9, 10], [8, 4, 6]))

"""
4. Write a Python program to add two given lists and find the difference between lists. Use map() function.
"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]


# def find_difference_and_sum(*args: list[int]):
#     sum_list = [sum(number) for number in args]
#     absolute_sum = sum(sum_list)
#
#     difference = max(sum_list) - min(sum_list)
#
#
#     return f'Sum total of 2 lists is {absolute_sum}\nDifference is {difference}'
#
#
# print(find_difference_and_sum(list1, list2))

"""
5. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.
"""

# tuple_int = (5, 8, 7)
# list_int = [5, 8, 3]
#
# def convert_into_str(first_variable, second_variable):
#     first_list = list(first_variable)
#     for i in range(len(first_list)):
#         first_list[i] = str(first_list[i])
#     print(list(first_list))
#
#     for i in range(len(second_variable)):
#         second_variable[i] = str(second_variable[i])
#     print(second_variable)
#
# convert_into_str(tuple_int, list_int)

"""
6. Write a Python program to filter a list of integers using Lambda
"""

# list_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def filter_integers(lst1: list[int]):
#     even = filter(lambda x: x % 2 == 0, lst1)
#     odd = filter(lambda x: x % 2 != 0, lst1)
#     return list(even), list(odd)
#
# print(filter_integers(list_of_integers))

"""
7. Write a Python program to find numbers divisible
by nineteen or thirteen from a list of numbers using Lambda
"""

# list_of_integers = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
#
#
# def find_numbers(lst1: list[int]):
#     divisible_numbers = filter(lambda x: x % 19 == 0 or x % 13 == 0, lst1)
#     return list(divisible_numbers)
#
# print(find_numbers(list_of_integers))

"""
8. Write a Python program to count the even, odd numbers in a given array of integers using Lambda
"""

# list_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def count_even_odd(lst1: list[int]):
#     even_count = 0
#     odd_count = 0
#     even = filter(lambda x: x % 2 == 0, lst1)
#     odd = filter(lambda x: x % 2 != 0, lst1)
#
#     for number in even:
#         even_count += 1
#
#     for number in odd:
#         odd_count += 1
#
#     return f'Even count is {even_count}\nOdd count is {odd_count}'
#
#
# print(count_even_odd(list_of_integers))

from functools import reduce

"""
9. Write a python program that multiplies all the values in a given list of integers.
"""

# my_list = [5, 9, 10]
#
# def multiply(x, y):
#     return x * y
#
# result = reduce(multiply, my_list)
# print(result)

"""
10. Write a python program that finds the maximum value within the given list.
"""

# my_list = [5, 9, 10]
#
# def find_max(lst1, lst2):
#     return max(lst1, lst2)
#
# result = reduce(find_max, my_list)
#
# print(result)

