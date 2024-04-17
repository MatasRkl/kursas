from datetime import datetime, timedelta
from transport_class import Transport


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
