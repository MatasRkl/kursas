import logging
"""
1. Sukurkite paprastą programą, kuri registruotų (logs) visus įvesties
 duomenis iš terminalo. Konfigūracijose turi būti rodomi visi papildomi duomenys (laikas, data, lygis ir t. t.).
"""
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%d/%m/%Y %H:%M:%S')


# def get_log():
#     x = input('Type something: ')
#     y = input('Type something more: ')
#     c = input('Type something even more: ')
#
#     return logging.info(f'You typed {x}, {y}, {c}')
#
#
# get_log()

"""
2. Parašykite funkciją, kuri perkeltų visus vieno tipo elementus į list galą: 
move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.
"""

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%d/%m/%Y %H:%M:%S')
#
#
# def move_to_end(data: list[int], specific_data: int):
#     result = [number for number in data if number != specific_data]
#     result.extend([specific_data] * data.count(specific_data))
#     return result
#
#
# my_data = [1, 3, 2, 4, 4, 1]
# my_specific_data = 2
# result = move_to_end(my_data, my_specific_data)
# logging.info(f'Result of move_to_end({my_data}, {my_specific_data}): {result}')


"""
3. Sukurkite 3 funkcijas, kurios yra susijusios viena su kita (viena iškviečiama kitoje),
 ir išbandykite visus logging sunkumo lygius pagal savo projektą.

Funkcijų pavyzdžiai:


def check_engine() -> None:
  pass
 
def start_car() -> None:
  check_engine()...
"""

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#
#
# def check_engine() -> None:
#     logging.info("Checking engine...")
#     logging.error("Engine check failed: Engine malfunction detected.")
#     logging.debug("Engine check complete.")
#
#
# def start_car() -> None:
#     logging.info("Starting the car...")
#     check_engine()
#     logging.info("Car started, but you need to visit service as soon as possible.")
#
#
# def stop_car() -> None:
#     logging.info("Stopping the car...")
#     logging.info("Car stopped successfully.")
#
#
# check_engine()
#
# start_car()
#
# stop_car()
#
# logging.critical("Critical issue: Your engine might die soon!")

"""
4. Sukurkite programą, kuri priima 4 duomenų tipus/struktūras: strings, numbers, list, dict.
 Iteriuokite 10 kartų su įvestimis ir užregistruokite, koks duomenų tipas/struktūra ir kiek kartų buvo įvesta.
  Apdorokite visas galimas klaidas ir jas užregistruokite.
"""

# logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s',
#                     datefmt='%d/%m/%Y %H:%M:%S')
#
#
# def registrate_type(data):
#     try:
#         if isinstance(data, str):
#             return "string"
#         elif isinstance(data, int) or isinstance(data, float):
#             return "number"
#         elif isinstance(data, list):
#             return "list"
#         elif isinstance(data, dict):
#             return "dictionary"
#         else:
#             raise ValueError("wrong data type.")
#     except ValueError as e:
#         logging.error(f"error trying to read: {e}")
#         return None
#
# def main():
#     input_types_count = {"string": 0, "number": 0, "list": 0, "dictionary": 0}
#     for _ in range(10):
#         user_input = input("Įveskite duomenis: ")
#
#         data_type = registrate_type(user_input)
#
#         if data_type:
#             input_types_count[data_type] += 1
#
#     print("got data types and their number: ")
#     for data_type, count in input_types_count.items():
#         print(f"{data_type}: {count}")
#
#
# main()
