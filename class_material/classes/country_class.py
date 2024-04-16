class Country:
    def __init__(self, name: str, population: int, hall_area: int):
        self.name = name
        self.population = population
        self.hall_area = hall_area
        self.is_big = True if population > 20000000 or hall_area > 3000000 else False

    def compare_pd(self, other_country):
        this_density = self.population / self.hall_area
        other_density = other_country.population / other_country.hall_area
        if this_density > other_density:
            print(f'{self.name} has a larger population density than {other_country.name}')
        else:
            print(f'{self.name} has a smaller population density than {other_country.name}')


belgium = Country('Belgium', 5000000, 456789)

france = Country('France', 68373433, 643801)
print(france.name)
print(france.is_big)

belgium.compare_pd(france)