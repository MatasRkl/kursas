from datetime import datetime, timedelta
from transport_class import Transport


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

    @staticmethod
    def calculate_total_fare(passengers: int, distance: int, fare_per_km_per_passenger: float):

        total_fare = passengers * distance * fare_per_km_per_passenger

        return total_fare


bus = Bus(100, 'ASD567', 'Gas', 0, '2024-05-09',
          'B, C', 10, '2024-05-09', 30)

print(bus.check_next_month_expirations())
print(bus.calculate_travel_costs(500, 2.5))
print(bus.count_buses(130))
print(bus.calculate_total_fare(20, 600, 0.1))
