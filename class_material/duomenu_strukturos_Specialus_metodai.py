# squares = []
# for number in range(10):
#     squares.append(number * number)
# print(squares)
#
# numbers = range(10)
# squares = [number * number for number in numbers]
# print(squares)
#
# numbers = range(10)
# squares = [number * number for number in range(10)]
# print(squares)
# print([number ** 2 for number in range(10)]) # PAVYZDYS
#
# names = ["Albert", "Alma", "Joseph", "Zoro"]
# print([name for name in names if name.startswith("A")])
#
# squares = {i: i * i for i in range(10)}
# print(squares)
#
#
# values = ["a", "b", "c"]
# for count, value in enumerate(values):
#     print(count, value)
#
#
# map/filter
# def print_word():
#     print('Hello word')
# def return_word(word):
#     return(word)
#
# print_word()
#
#
"""
1. Raskite visus skaičius nuo 1 iki 1000, kurie dalijasi iš 6.
"""
# def found_numbers():
#     return [number for number in range(1,1001) if number % 6 == 0]
#
# print(found_numbers())
#
#
#
#
#
# x = range(1, 1000)
# for y in x:
#     if y % 6 == 0:
#         print(y)
"""
2. Raskite visus skaičius iš 1-1000, kuriuose yra 9.
"""
# def find_numbers_that_has_9():
#     return [number for number in range(1, 1001) if '9' in str(number)]
#
# print(find_numbers_that_has_9())
"""
3. Sukurkite string iš daugybės žodžių: Apskaičiuokite, kiek žodžių turi raidę e.
"""
# sentence = 'Welcome to the coding world of confusion'
# splitted_sentence = sentence.split()
# words_with_e = [word for word in splitted_sentence if 'e' in word]
# print(len(words_with_e))
#
#
#
# word_count = 0
# for word in splitted_sentence:
#     if 'e' in word:
#         word_count += 1
# print(word_count)
"""
4. Naudodami tą patį string, kaip ir ankstesniame pratime: apskaičiuokite raidžių, kurios turi daugiau
nei 5 simbolius, skaičių.
"""
# words_with_more_then_five_elements = [word for word in splitted_sentence if len(word) > 5]
# print(len(words_with_more_then_five_elements))




# for word in splitted_sentence:
#     if len(word) > 5:
#         words_with_more_then_five_elements += 1
#
# print(words_with_more_then_five_elements)
"""
5. Parašykite programą, kuri patikrintų, ar duotas skaičius yra tobulasis kvadratas.
"""

# given_number = int(input('Type your number: '))
# if given_number ** 0.5 == int(given_number ** 0.5):
#     print(f'{given_number} has a square root')
# else:
#     print(f'{given_number} doesnt have a square root')


"""
1. Lentynoje sudeti batai:
[8.90, 4,90, 13,20, 8,80, 14,00, 12,00]
a) Paskaičiuokite kiek eurų liks žmogui, jei jis šiuo metu pirks dvejus pigiausius batus;
b) kokius dvejus batus jam nupirkti, jei jis turi 20 eurų ir nori, kad jam liktų kuo mažiau eurų;
"""

# shoes_price = [8.90, 4.90, 13.20, 8.80, 14.00, 12.00]
