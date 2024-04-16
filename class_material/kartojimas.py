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

# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
#
# def remove_from_list():
#     for number in roll_number[:]:
#         if number not in sample_dict.values():
#             roll_number.remove(number)
#     return roll_number
#
#
# print(remove_from_list())

"""
Sukurti klasę, kurioje atributas butu "text".
 
Sukurti metodus, kurie:
1. Suskaičiuotų kiek yra žodžių tekste;
2. Metoda, kuris gražintų visus žodžius, kurie būtų nurodyti metodo kintamajame. 
Pvz nurodytos raidės 'ams', turi išrinkti visus žodžius, kurie turis šias raides.
3. Išrinktų visus žožius, kurių ilgis didesnis arba lygus nurodytam metode;
 
Prasau pagalvoti ar Jūsų sprendime nėra kodo dubliavimo ir pagalvokite kaip jo išvengti.
"""


# class Text_Slicer:
#     def __init__(self, text: str):
#         self.text = text
#
#     def split(self):
#         return self.text.split()
#
#     def count_words(self):
#         return len(self.split())
#
#     def filter_words(self, words: list[str]):
#         found_words = []
#         for word in self.split():
#             if word in words:
#                 found_words.append(word)
#         return found_words
#
#     def get_words_by_length(self, length: int):
#         found_words = []
#         for word in self.split():
#             if len(word) >= length:
#                 found_words.append(word)
#         return found_words
#
#
# text = Text_Slicer('I went to the shop and bought some happy drinks')
#
# print(text.count_words())
# print(text.filter_words(['went', 'to']))
# print(text.get_words_by_length(5))

"""
Automobilių parkas. Susideda iš: 

Lengvųjų automobilių; 

Keleivių pervežimo automobiliai; 

Krovinių pervežimo automobiliai. 

 
Autobusai turimi atributai: 

Keleivių vietų skaičius 

Skaičiuojamas kilometražas per metus (tam, kad suskaičiuoti kokie yra kintami kaštai vienam kilometrai) 

Automobilio numeris; 

Kuro tipas; 

Pastovūs kaštai (draudimas, techninės apžiūros ir t.t.) Eurai per metus; 

Techninės apžiūros datos; 

Vairuotojo (priklauso nuo teisių kategorijų) teisių kategorijos; 

Kuro sąnaudos 100km. 

Draudimo data 

Reikalingi metodai: 

Metodas, kuris paskaičiuotų ar sekantį mėnesį reikia atlikti technine apžiūra, ar reikia draudimo; 

Paskaičiuoti kokie bus kaštai nuvažiavus atstumą X. Reikia įvertinti pastovius kaštus, kuro kainą; 

Metodas, kiek reikia autobusų norint pervežti N keleivių; 

Paskaičiuotų kokia būtų bendra samata pervežus N keleivių ir nuvažiavus X kilometrų. 

 
Lengvųjų turimi atributai: 

Skaičiuojamas kilometražas per metus (tam, kad suskaičiuoti kokie yra kintami kaštai vienam kilometrai) 

Automobilio numeris; 

Kuro tipas; 

Pastovūs kaštai (draudimas, techninės apžiūros ir t.t.) Eurai per metus; 

Techninės apžiūros datos; 

Vairuotojo (priklauso nuo teisių kategorijų) teisių kategorijos; 

Kuro sąnaudos 100km. 

Draudimo data 

Reikalingi metodai: 

Metodas, kuris paskaičiuotų ar sekantį mėnesį reikia atlikti technine apžiūra, ar reikia draudimo; 

Paskaičiuoti kokie bus kaštai nuvažiavus atstumą X. Reikia įvertinti pastovius kaštus, kuro kainą; 

 
Krovininiai automobiliai: 

Skaičiuojamas kilometražas per metus (tam, kad suskaičiuoti kokie yra kintami kaštai vienam kilometrai) 

Pervežimas svoris 

Yra galimybė prikabinti priekabą ar ne; 

Priekabos pervežiamas svoris 

Automobilio numeris; 

Kuro tipas; 

Pastovūs kaštai (draudimas, techninės apžiūros ir t.t.) Eurai per metus; 

Techninės apžiūros datos; 

Vairuotojo (priklauso nuo teisių kategorijų) teisių kategorijos; 

Kuro sąnaudos 100km. 

Draudimo data 

Reikalingi metodai: 

Metodas, kuris paskaičiuotų ar sekantį mėnesį reikia atlikti technine apžiūra, ar reikia draudimo; 

Paskaičiuoti kokie bus kaštai nuvažiavus atstumą X. Reikia įvertinti pastovius kaštus, kuro kainą; 

Paskaičiuoti kiek reisų reikia padaryti ir ar reikia prikabinti priekabą (tarkim reikia pervežti 30,
 automobilio pervežamas svoris yra 12 tonų, priekabos pervežamas svoris 5 tonos. Tokiu
  atveju reikia vieną karta vežti be priekabos, o antra su priekaba. Bet jei reikia pervežti tarkime 36 tonos,
   priekabos kabinti neverta, nes vistiek reikia daryti tris reisus); 

 
Vairuotojas, kuris turi atributus: 

Atostogų laikas 

Turima teisių kategorija (D sukvežimiai be priekabos, E su priekaba) 

Darbo užmokestis vienam kilometrui; 

 
Prie sukvežimių: 
pridėkime metodą, kuris vertintų vairuotoją ir pagal turimą kategoriją įvertintų ar gali vairuoti mašina su priekaba. 
Visiems automobiliams turi būti patikrinimas ar vairuotojas gali dirbti (ne atostogauja) 
"""
from datetime import datetime, timedelta


class Transport:
    def __init__(self, range_per_year: int, plate_number: str, fuel_type: str,
                 expenses: int, inspection: str, driving_categories: str, fuel_consumption: int,
                 insurance_date: str):
        self.insurance_date = insurance_date
        self.fuel_consumption = fuel_consumption
        self.driving_categories = driving_categories
        self.inspection = inspection
        self.expenses = expenses
        self.fuel_type = fuel_type
        self.plate_number = plate_number
        self.range_per_year = range_per_year


class Bus(Transport):
    def __init__(self, range_per_year: int, plate_number: str, fuel_type: str, expenses: int, inspection: str,
                 driving_categories: str, fuel_consumption: int, insurance_date: str, passenger_seats: int):
        super().__init__(range_per_year, plate_number, fuel_type, expenses, inspection, driving_categories,
                         fuel_consumption, insurance_date)
        self.passenger_seats = passenger_seats

    def check_next_month_expirations(self):
        insurance_expiry = datetime.strptime(self.insurance_date, "%Y-%m-%d")
        current_date = datetime.now()

        if current_date + timedelta(days=30) >= insurance_expiry:
            return "You will need to do bus inspection or get insurance"
        else:
            return "None is needed"

    def calculate_travel_costs(self, distance: int, fuel_price: float):
        fuel_consumption_per_100_km = self.fuel_consumption

        fuel_consumed = (fuel_consumption_per_100_km / 100) * distance

        fuel_cost = fuel_consumed * fuel_price

        fixed_costs = self.expenses

        total_cost = fuel_cost + fixed_costs

        return total_cost

    def count_buses(self, passengers: int):
        buses_needed = passengers / self.passenger_seats
        return print(f'You well need {buses_needed} to export these passengers')

    def calculate_total_fare(self, passengers: int, distance: int, fare_per_km_per_passenger: float):

        total_fare = passengers * distance * fare_per_km_per_passenger

        return total_fare


bus = Bus(100, 'ASD567', 'Gas', 0, '2024-05-09',
          'B, C', 10, '2024-05-09', 30)

print(bus.check_next_month_expirations())
print(bus.calculate_travel_costs(500, 2.5))
print(bus.count_buses(130))
print(bus.calculate_total_fare(20, 600, 0.1))


class Car(Transport):
    def __init__(self, range_per_year: int, plate_number: str, fuel_type: str, expenses: int, inspection: str,
                 driving_categories: str, fuel_consumption: int, insurance_date: str):
        super().__init__(range_per_year, plate_number, fuel_type, expenses, inspection, driving_categories,
                         fuel_consumption, insurance_date)

    def check_next_month_expirations(self):
        insurance_expiry = datetime.strptime(self.insurance_date, "%Y-%m-%d")
        current_date = datetime.now()

        if current_date + timedelta(days=30) >= insurance_expiry:
            return "You will need to do bus inspection or get insurance"
        else:
            return "None is needed"

    def calculate_travel_costs(self, distance: int, fuel_price: float):
        fuel_consumption_per_100_km = self.fuel_consumption

        fuel_consumed = (fuel_consumption_per_100_km / 100) * distance

        fuel_cost = fuel_consumed * fuel_price

        fixed_costs = self.expenses

        total_cost = fuel_cost + fixed_costs

        return total_cost


class Truck(Transport):
    def __init__(self, range_per_year: int, plate_number: str, fuel_type: str, expenses: int, inspection: str,
                 driving_categories: str, fuel_consumption: int, insurance_date: str, load_capacity: int,
                 trailer_function: str):
        super().__init__(range_per_year, plate_number, fuel_type, expenses, inspection, driving_categories,
                         fuel_consumption, insurance_date)
        self.trailer_function = trailer_function
        self.load_capacity = load_capacity

    def check_next_month_expirations(self):
        insurance_expiry = datetime.strptime(self.insurance_date, "%Y-%m-%d")
        current_date = datetime.now()

        if current_date + timedelta(days=30) >= insurance_expiry:
            return "You will need to do bus inspection or get insurance"
        else:
            return "None is needed"

    def calculate_travel_costs(self, distance: int, fuel_price: float):
        fuel_consumption_per_100_km = self.fuel_consumption

        fuel_consumed = (fuel_consumption_per_100_km / 100) * distance

        fuel_cost = fuel_consumed * fuel_price

        fixed_costs = self.expenses

        total_cost = fuel_cost + fixed_costs

        return total_cost
