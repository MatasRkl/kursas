from datetime import datetime, timedelta
from transport_class import Transport
from driver_class import Driver


class Truck(Transport):
    def __init__(self, range_per_year: int, plate_number: str, fuel_type: str, expenses: int, inspection: str,
                 driving_categories: str, fuel_consumption: int, insurance_date: str, load_capacity: int,
                 trailer_function: str, trailer_load_capacity: int):
        super().__init__(range_per_year, plate_number, fuel_type, expenses, inspection, driving_categories,
                         fuel_consumption, insurance_date)
        self.trailer_load_capacity = trailer_load_capacity
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

    def count_how_many_trips(self, weight: int):
        total_weight = weight

        if self.trailer_function == "Attachable":
            trips_with_trailer = total_weight // (self.load_capacity + self.trailer_load_capacity)
            remainder = total_weight % (self.load_capacity + self.trailer_load_capacity)
            trips_without_trailer = 1 if remainder > 0 else 0
            total_trips = trips_with_trailer + trips_without_trailer
        else:
            total_trips = total_weight // self.load_capacity
            remainder = total_weight % self.load_capacity
            if remainder > 0:
                total_trips += 1

        return total_trips

    @staticmethod
    def can_driver_drive_truck_with_trailer():
        if 'E' in driver.driving_categories:
            return 'Can'
        else:
            return 'Cant'


driver = Driver('2024-05-10', ['B', 'D', 'E'], 2)

truck = Truck(100, 'ASD567', 'Gas', 0, '2024-05-09',
              'B, C', 10,
              '2024-05-09', 12, 'Attachable',
              5)

print(truck.count_how_many_trips(18))
print(truck.can_driver_drive_truck_with_trailer())
