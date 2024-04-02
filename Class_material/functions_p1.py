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


def extract_email_addresses(long_text: str):
    divided_text = long_text.split()
    email_adresses = [word for word in divided_text if '@' in word and '.' in word]
    return email_adresses


print(extract_email_addresses('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam at elit nec nisi lobortis luctus. Ut faucibus, lorem@example.com quis hendrerit lacinia, ipsum odio tristique purus, at suscipit quam felis eu purus. Quisque ac lorem vel ante scelerisque suscipit. Nam eu mauris at leo tristique fermentum. Sed varius libero at eros malesuada, sed venenatis justo mattis. Vestibulum@example.net eu dolor non leo lacinia tincidunt. Fusce tristique lacus nec mauris fermentum, at placerat sapien feugiat. Phasellus@example.org finibus vulputate tellus, nec consectetur risus. Curabitur et ligula et ligula pulvinar varius eget eu arcu. Integer at ligula vitae libero facilisis fermentum. Sed@example.co.uk dapibus malesuada orci, id eleifend purus aliquam eu. Donec condimentum, libero eget interdum consequat, odio justo convallis sem, ut ultricies velit velit@example.io eget lacus. In hac habitasse platea dictumst. Maecenas ac libero in velit consequat interdum. Sed eget nisl vel ipsum hendrerit interdum. Fusce id fermentum lacus, ut pulvinar felis. Sed efficitur aliquam nulla, eget convallis neque@example.biz.'))