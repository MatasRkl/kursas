class Book:
    def __init__(self, name: str, author: str):
        self.name = f'{name}'
        self.author = f'{author}'

    def get_title(self):
        return f'Pavadinimas: {self.name}'

    def get_author(self):
        return f'Autorius: {self.author}'


PP = Book('Pride and Prejudice', 'Jane Austen (PP)')
H = Book('Hamletas', 'Viljamas Šekspyras (H)')
WP = Book('Karas ir taika', 'Levas Tolstojus (WP)')

print(PP.name)
print(PP.author)
print(PP.get_title())
print(PP.get_author())

print(H.name)
print(H.author)
print(H.get_title())
print(H.get_author())

print(WP.name)
print(WP.author)
print(WP.get_title())
print(WP.get_author())
