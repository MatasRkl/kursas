class Darbuotojas:
    def __init__(self, name: str = 'Matas', surname: str = 'Riklius'):
        self.full_name = f'{name} {surname}'
        self.email = f'{name.lower()}.{surname.lower()}@company.com'


darbuotojas = Darbuotojas()

print(darbuotojas.full_name)
print(darbuotojas.email)
