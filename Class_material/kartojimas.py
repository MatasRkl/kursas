# def calculate_dict(data: dict, necessary_key: list, deleting_key):
#     """
#     Sukurti funkcija, kuri priimtu tris variable – dicta, reikalingus key (list), istrinamus key (listas)
#     :return:
#     """
#     result_n = {}
#     new_data = data.copy()
#     for key in data:
#         if key in necessary_key:
#             result_n[key] = data[key]
#         if key in deleted_keys:
#             del new_data[key]
#
#     return result_n, new_data
#
#
# numbers = {
#     1: 'vienas',
#     2: 'du',
#     3: 'trys',
#     4: 'keturi',
# }
#
# needed_keys = [1, 2]
# deleted_keys = [3]

"""
Kartojimas: Parasyti funckija, kuri priimtu du vairabe
 – lista kartotini. Grazinti turi lista, kuriame buvo listai su kartotiniu nariu skaiciumis. Pvz.
"""
# import math
#
#
# def group_out(data, times):
#     value = math.ceil(len(data)/times)
#     result = []
#     for i in range(value):
#         first_index, second_index = i * times, i * times + times
#         result.append(data[first_index:second_index])
#     print(result)
#
#
# data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# kartotinis = 2
#
# print(group_out(data_list, kartotinis))

"""
1:	Write a Python program to find the most common elements and their counts in a specified text.
Original string: lkseropewdssafsdfafkpwe
Most common three characters of the said string:
[('s', 4), ('e', 3), ('f', 3)]
"""


# def find_most_common():
#     common = {}
#     org_string = 'lkseropewdssafsdfafkpwe'
#     for letter in org_string:
#         if letter in common:
#             common[letter] += 1
#         else:
#             common[letter] = 1
#     most_common = max(common, key = common.get)
#     return most_common, common
#
#
# print(find_most_common())

"""
2. Exercise 2: Create a list by picking an odd-index items from the first list and even index items from the second
Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from
 the list l1 and even index elements from the list l2.
Given:
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
Expected Output:
Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]
Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
"""
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
#
#
# def get_odd_indexes():
#     odd_elements_l1 = []
#     for i in range(1, len(l1), 2):
#         odd_elements_l1.append(l1[i])
#     return odd_elements_l1
#
#
# def get_even_indexes():
#     even_elements_l2 = []
#     for i in range(0, len(l2), 2):
#         even_elements_l2.append(l2[i])
#     return even_elements_l2
#
#
# l3 = get_even_indexes() + get_even_indexes()
#
# print(get_odd_indexes())
# print(get_even_indexes())
# print(l3)

"""
Exercise 3: Create a Python set such that it shows the element from both lists in a pair
Given:

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
Expected Output:

Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)
"""
# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]
#
#
# def group_up():
#     result_set = set(zip(first_list, second_list))
#     sorted_result_set = sorted(result_set)
#     return sorted_result_set
#
#
# print(group_up())

"""
Exercise 4: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not,
delete it from the list
Given:

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
Expected Outcome:

After removing unwanted elements from list [47, 69, 76, 97]
"""

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

def remove_from_list():
    for number in roll_number[:]:
        if number not in sample_dict.values():
            roll_number.remove(number)
    return roll_number


print(remove_from_list())