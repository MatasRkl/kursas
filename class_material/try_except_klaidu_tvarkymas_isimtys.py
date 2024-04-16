"""
1. Sukurkite bent 5 skirtingas funkcijas ir pabandykite apdoroti bent 5 integruotas "Python" išimtis.
"""


# def get_sum_from_three_integers(a: int, b: int, c: int):
#     try:
#         sum = a + b + c
#     except (TypeError):
#         print('not int')
#     else:
#         return sum
#
#
# print(get_sum_from_three_integers('as', 9, 4))


# def print_in_upper(a: str):
#     try:
#         if a == 'valio':
#             raise ValueError("Don't be happy here")
#         return a.upper()
#     except ValueError as e:
#         print(e)
#
# print(print_in_upper('valio'))
#
#
"""
2.Python kalboje, dalijant iš nulio, gauname ZeroDivisionError. Jūsų užduotis - sukurti funkciją, kuri:

Kaip argumentus priima du skaičius.

Mėgina padalyti pirmąjį skaičių iš antrojo.

Jei antrasis skaičius yra nulis, ji turėtų sugauti ZeroDivisionError ir grąžinti pasirinktinį klaidos pranešimą.

Jei dalijimas sėkmingas, turėtų būti grąžinamas rezultatas.

Nepriklausomai nuo to, ar dalijimas pavyko, ar ne, turėtų būti išspausdintas pranešimas "Attempted division".
 Jei įvesties duomenys nėra skaičiai, pateikiamas TypeError pranešimas. Funkcija pagauna šią TypeError ir
  grąžina pasirinktinį klaidos pranešimą.
"""


def divide_two_numbers(dividend: int, divisor: int):
    try:
        quotient = dividend / divisor
        print(f'Result = {quotient}')
    except ZeroDivisionError:
        print('Divisor is zero; Division is impossible')
    except TypeError:
        print('You must type in integers')

    print("Attempted division")


print(divide_two_numbers('5', 0))


"""
3. Sukurkite mini "Python" programą, kuri įvestų du skaičius ir grąžintų jų sumą,
 atimtį, dalybą, daugybą. Tvarkykite visas galimas klaidas.
"""


# def calculator():
#     try:
#         number1 = int(input('Type your first number: '))
#         number2 = int(input('Type your second number: '))
#
#         if not isinstance(number1, int) or not isinstance(number2, int):
#             raise TypeError('not integers')
#
#         if number2 == 0:
#             raise ZeroDivisionError('Divisor is zero; Division is impossible')
#
#
#         n1_n2_sum = number1 + number2
#         print(f'Sum: {n1_n2_sum}')
#         n1_n2_diff = number1 - number2
#         print(f'Dif: {n1_n2_diff}')
#         n1_n2_division = number1 / number2
#         print(f'Answer: {n1_n2_division}')
#         n1_n2_multiply = number1 * number2
#         print(f'Sum: {n1_n2_multiply}')
#     except TypeError as t:
#         print(t)
#     except ZeroDivisionError as e:
#         print(e)
#     except ValueError:
#         print('Dont write both numbers in one input please')
#
#
# calculator()

"""
4. Atnaujinkite ankstesnę užduotį su galimomis raise išimtimis.^^^^^^^^^^^
"""