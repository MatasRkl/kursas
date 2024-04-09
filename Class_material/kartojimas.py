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
