"""
❗ Visose užduotyse turi būti nurodyti tipų anotacijos❗
1. Patys sukurkite bent 5 skirtingas funkcijas ir jas išbandykite.
"""

#
# def get_sum_from_three_integers(a: int, b: int, c: int):
#     return a + b + c
#
#
# print(get_sum_from_three_integers(8, 9, 4))
#
#
# def print_in_upper(a: str):
#     return a.upper()
#
#
# print(print_in_upper('Hello everybody'))
#
#
# def get_square(a: int):
#     return a * a
#
#
# print(get_square(8))
#
#
# def get_perfect_square(a: int):
#     return a ** 0.5
#
#
# print(get_perfect_square(25))
#
#
# def get_average(a: int, b: int):
#     return (a + b) / 2
#
#
# print(get_average(8, 6))

"""
2. Sukurkite funkciją, kuri prie kiekvieno list nario prideda string galūnę.
"""


# def add_at_the_end_of_element(lst, end_element):
#     return [word + end_element for word in lst]
#
#
# print(add_at_the_end_of_element(['hello', 'bye'], 'ano'))


"""
3. Sukurkite mini python programą, kuri kaip įvestį paimtų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą.
"""


# def calculator():
#     number1 = int(input('Type your first number: '))
#     number2 = int(input('Type your second number: '))
#
#     n1_n2_sum = number1 + number2
#     n1_n2_diff = number1 - number2
#     n1_n2_division = number1 / number2
#     n1_n2_multiply = number1 * number2
#
#     return n1_n2_sum, n1_n2_diff, n1_n2_division, n1_n2_multiply
#
# print(calculator())

"""
4. Sukurkite funkciją, kuri grąžintų tik unikalius simbolius turinčias string reikšmes.
"""


# def get_words_with_unique_simbols(lst: list[str]):
#     unique_words = [word for word in lst if len(set(word)) == len(word)]
#     return unique_words
#
#
# print(get_words_with_unique_simbols(['boy', 'girl', 'teenager']))


"""
5. Parašykite programą, apibrėžiančią funkciją extract_email_addresses(), kuri priima tekstą kaip įvestį
 ir iš teksto ištraukia visus el. pašto adresus.
"""


# def extract_email_addresses(long_text: str):
#     divided_text = long_text.split()
#     email_adresses = [word for word in divided_text if '@' in word and '.' in word]
#     return email_adresses
#
# text_input = str(input('Type you text: '))
# extracted_emails = extract_email_addresses(text_input)
# print(extracted_emails)

"""
Sukurkite žaidimą bulius/karvė. Žaidimo taisykles:
1. Yra sugeneruojami random pagalba 4 skaiciai (nuo 0000 iki 9999).
2. Tada paprasoma konsoleje suvesti kiek bandymų spėti turime. (Tarkim vartotojas suves 3 kartus)
3. Vartotojo prasoma meginsti atspeti skaiciu (pvz vartotojas speja 0123).
4. Sistema skaiciuoja kiek skaiciu yra karvių, ir kiek yra bulių. Karve yra toks skaicius, kuris yra teisingas,
 bet stovi ne savo vietoje, bulius – ir teisingas, ir teisingoje vietoje. Jei visi buliai – zaidimo pabaiga.
5. Jei skaicius neatspetas per nustatyta bandymu skaiciu – zaidimas pralostas.
 
Pvz kompiuris sugeneruoja 0839.
Vartotojas speja 3 kartus:
0914 -> 1 bulius,1 karve,
0849 -> 3 buliai, 1 karve,
0839 -> 4 buliai, game over.
"""

# import random
#
#
# def generate_random_number():
#     return str(random.randint(0, 9999)).zfill(4)
#
#
# def count_bulls_and_cows(secret_number, guess):
#     bulls = sum(secret_digit == guess_digit for secret_digit, guess_digit in zip(secret_number, guess))
#
#     secret_set = set(secret_number)
#     guess_set = set(guess)
#
#     cows = sum(min(secret_number.count(digit), guess.count(digit)) for digit in secret_set & guess_set) - bulls
#
#     return bulls, cows
#
#
# the_number = generate_random_number()
# max_guesses = int(input('Type your max guess count: '))
# attempts = 0
#
# while attempts < max_guesses:
#     guess = str(input('Type your guess that has !!4 digits!!: '))
#
#     bulls, _ = count_bulls_and_cows(the_number, guess)
#     print(f"Bulls: {bulls}")
#
#     if bulls == 4:
#         print('CORRECT')
#         break
#
#     attempts += 1
#
# if attempts == max_guesses:
#     print('You wasted your guesses')

"""
1. Write a Python program to find if a given string starts
with a given character using Lambda. Output:True or False
"""

# find_out = lambda sentence, char: True if sentence[0] == char else False
#
# print(find_out("If we go, we go", 'i'))

"""
2. Write a Python program to create a lambda function that adds 15 to
a given number passed in as an argument,
also create a lambda function that multiplies argument x with argument y and print the result.
"""

# add = lambda a: a + 15
# print(add(10))
#
# multiply = lambda a, b: a * b
# print(multiply(5, 6))

"""
3. Write a Python program to square and cube every number in a given list of integers using Lambda.
"""

# my_list = [5, 7, 9]
# squared_cubed_list = list(map(lambda x: (x ** 2, x ** 3), my_list))
# print(squared_cubed_list)

"""
4. Write a Python program to extract year, month, date and time using Lambda. Sample Output:
"""

# from datetime import datetime
#
# sample_datetime = datetime.now()
#
# extract_info = lambda dt: (dt.year, dt.month, dt.day, dt.time())
#
# year, month, day, time = extract_info(sample_datetime)
#
# print("Year:", year)
# print("Month:", month)
# print("Date:", day)
# print("Time:", time)

"""
5. Write a Python program to sort a list of tuples using Lambda
"""

# sorting_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# sorted_list = sorted(sorting_list, key = lambda x: x[1])
# print(sorted_list)

"""
6. Write a Python program to sort a list of dictionaries buy color value using Lambda.
"""

# list_of_dicts = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#                  {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
#                  {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
#
# sorted_list_of_dicts = sorted(list_of_dicts, key = lambda x: x['color'])
# print(sorted_list_of_dicts)

"""
7. Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.
"""

# lists_in_list = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
#
# sorted_lists = sorted(lists_in_list, key = lambda x: sum(x))
# print(sorted_lists)