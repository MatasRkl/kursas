"""
1. Sukurkite Calculator klasę su pagrindinėmis funkcijomis: sudėti, dalyti, dauginti,
atimti ir t. t.. Inicijuokite klasę ir parodykite keletą skaičiavimų.
SPRENDIMAS "CLASSES"
"""

"""
2. Darbuotojo klasėje sukurkite egzempliorių atributus fullname (vardas, pavardė) ir email (el. paštas).
 Turint asmens vardą ir pavardę:

Vardą ir pavardę suformuokite paprasčiausiai sujungdami vardą ir pavardę, atskiriamus tarpeliu.

Elektroninį paštą suformuokite sujungdami vardą ir pavardę, tarp jų įterpdami simbolį .
 Pabaigoje įrašydami @company.com. Įsitikinkite, kad visas el. laiškas būtų** rašomas mažosiomis raidėmis**.
 SPRENDIMAS "CLASSES"
"""

"""
3. Sukurkite knygos klasę Book, kuri turi du atributus:

name

author

ir du metodus:

Metodas, pavadintas .get_title(), kuris grąžina: "Pavadinimas: " + egzemplioriaus pavadinimas.

Metodas .get_autor(), kuris grąžina: "Autorius: " + egzempliorius autorius.

ir instancuokite šią klasę sukurdami 3 naujas knygas:

- Pride and Prejudice - Jane Austen (PP)
- Hamletas - Viljamas Šekspyras (H)
- Karas ir taika - Levas Tolstojus (WP)
Naujų egzempliorių pavadinimai turėtų būti atitinkamai PP, H ir WP. Pavyzdžiui, jei, naudodamas šią knygų klasę, instancuočiau šią knygą:

- Haris Poteris - J. K. Rowling (HP)
Gaučiau šiuos atributus ir metodus:

HP.title ➞ "Harry Potter"
HP.author ➞ "J.K. Rowling"
HP.get_title() ➞ "Pavadinimas: Haris Poteris"
HP.get_author() ➞ "Autorius: Rowling"
SPRENDIMAS "CLASSES"
"""

"""
4. Apie šalį galima sakyti, kad ji yra didelė, jei ji yra:

Didelė gyventojų skaičiumi.

Didelė pagal plotą.

Šalies klasę papildykite taip, kad joje būtų atributas is_big. Nustatykite jį į True, jei tenkinamas kuris nors iš šių kriterijų:

Gyventojų skaičius yra didesnis nei 20 mln.

Plotas didesnis nei 3 mln. km².

Taip pat sukurkite metodą, kuris palygintų šalies gyventojų tankį su kitos šalies objektu. Grąžinkite tokio formato eilutę:

{country} has a {smaller / larger} population density than {other_country}
Pavyzdys:

australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

australia.is_big ➞ True
andorra.is_big ➞ False
andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Australia"
"""