"""
1. Parašykite funkciją, kuri paima du list'us ir prie pirmojo list pirmojo elemento
 prideda antrojo listpirmąjį elementą,
 antrojo sąrašo antrąjį
 elementą, antrojo sąrašo antrąjį elementą ir antrojo sąrašo antrąjį elementą. pirmąjį sąrašą su
  antruoju antrojo sąrašo elementu ir t. t., ir t. t. Grąžinkite True, jei visi elementų deriniai sudaro
   tą patį skaičių. Priešingu atveju grąžinama False.
"""


def puzzle_pieces(lst1, lst2):

    target_sum = lst1[0] + lst2[0]
    for i in range(1, len(lst1)):
        if lst1[i] + lst2[i] != target_sum:
            return False
    return True


print(puzzle_pieces([5, 6, 8, 9], [6, 7, 9, 5]))


"""
2. Tarp lyginių ir nelyginių skaičių vyksta didelis karas.
 Šiame kare jau žuvo daug skaičių, todėl tavo užduotis - jį nutraukti.
 Jūs turite nustatyti, kurios grupės sumos didesnės: lyginių ar nelyginių. Laimi didesnė grupė.
Sukurkite funkciją, kuri paimtų sveikųjų skaičių sąrašą, atskirai suskaičiuotų lyginių ir nelyginių skaičių sumas,
 tada grąžintų lyginių ir nelyginių skaičių sumų skirtumą skaičių.
"""


def war_of_numbers(numbers):
    sum_even = sum(number for number in numbers if number % 2 == 0)
    sum_odd = sum(number for number in numbers if number % 2 != 0)
    if sum_even > sum_odd:
        return sum_even - sum_odd
    else:
        return sum_odd - sum_even


print(war_of_numbers([5, 9, 7, 8, 6]))


"""
3. Jums duotas bigramų masyvas ir žodžių masyvas. Parašykite funkciją,
 kuri grąžintų True, jei iš šio masyvo galima rasti kiekvieną bigramą bent vieną kartą žodžių masyve.
"""


def can_find(bigrams, words):
    for bigram in bigrams:
        found = False
        for word in words:
            if bigram in word:
                found = True
                break
        if not found:
            return False
    return True


print(can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]))

"""
4. Sukurkite funkciją, kuri priima eilučių sąrašą ir grąžina naują sąrašą,
 kuriame yra tik tos eilutės, kurios prasideda balsiu.
"""


def string_starts_with_vowel(lst1: [str]):
    vowels = "AEIOUYaeiouy"
    return [word for word in lst1 if word[0] in vowels]


print(string_starts_with_vowel(["Apple", "tiger"]))

"""
5. Sukurkite lambda funkciją, kuri:

priima du argumentus: eilutę ir skaičių.

grąžina naują eilutę, kuri pakartoja pradinę eilutę tiek kartų, kiek kartų pakartotas skaičius.
 Pavyzdžiui, jei įvesties duomenys yra Hello ir 3, funkcija turėtų grąžinti HelloHelloHello.
"""


def repeator(st, num):
    return st * num


print(repeator("CODE ME ", 5))

"""
Lambda function
"""


def multiply(x: int, y: int) -> int:
    return x * y


print(multiply(2, 3))
