"""
1. Write a Python program to create a generator
that generates the squares of numbers up to a given number.
"""


def generate_squares(num):
    for number in range(1, num+1):
        yield number**2


squares_generator = generate_squares(5)
for squares in squares_generator:
    print(squares)

"""
2.Write a Python program to create a generator that yields "n" random
numbers between a low and high number that are inputs.
"""

# from random import randint
#
#
# def yield_random_number(a: int, n: int, times: int):
#     for _ in range(times):
#         yield random.randint(a, n)
#
#
# num_1 = int(input('First number: '))
# num_2 = int(input('Second number: '))
#
# random_number = yield_random_number(num_1, num_2, 5)
# for number in random_number:
#     print(number)

"""
3. Write a Python program to create a generator that iterates over a string
"""

# def string_iterator(input_string):
#     for char in input_string:
#         yield char
#
#
# input_string = input("Enter a string: ")
# char_generator = string_iterator(input_string)
#
# print("Characters in the string:")
# for char in char_generator:
#     print(char)

"""
4. Write a Python program to create a Fibonacci series generator.
"""


# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
#
# num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
#
# fibonacci_gen = fibonacci_generator()
#
# print("Fibonacci series:")
# for _ in range(num_terms):
#     print(next(fibonacci_gen))

"""
5. Write a Python program to create a generator
from a list that yields item from the list if it is a number.
"""

# data = ['hello', 5, 'dont', 10, 'fail', 53, 'me']
#
# def save_int(data: list):
#     for item in data:
#         if isinstance(item, int):
#             yield item
#
#
# saver = save_int(data)
# for item in saver:
#     print(item)

"""
6. Create a list of tuples, each representing
 a person's information.
Each tuple contains the following information:
(name: str, age: int, city: str, salary: float).
Your task is to create Python generators
 to perform the following tasks:

Filtering Generator: Create a generator function that
filters the people who are below a certain age threshold.
Mapping Generator: Create a generator function
that maps the names of people to uppercase.
Aggregation Generator: Create a generator function that
calculates the average salary of the selected group.
"""

people_info = [
    ("Alice", 30, "New York", 50000.0),
    ("Bob", 25, "Los Angeles", 60000.0),
    ("Charlie", 35, "Chicago", 70000.0),
    ("David", 40, "Houston", 80000.0),
    ("Eve", 22, "Miami", 55000.0)
]


def filter_below_age(people, age_threshold):
    for person in people:
        if person[1] < age_threshold:
            yield person


def map_to_uppercase(people):
    for person in people:
        yield (person[0].upper(),) + person[1:]


def calculate_average_salary(people):
    total_salary = 0
    count = 0
    for person in people:
        total_salary += person[3]
        count += 1
    if count > 0:
        yield total_salary / count


age_threshold = 30
filtered_gen = filter_below_age(people_info, age_threshold)
uppercase_gen = map_to_uppercase(people_info)
average_salary_gen = calculate_average_salary(people_info)

print("People below age", age_threshold, ":")
for person in filtered_gen:
    print(person)

print("\nNames mapped to uppercase:")
for person in uppercase_gen:
    print(person)

print("\nAverage salary of selected group:")
for average_salary in average_salary_gen:
    print(average_salary)
