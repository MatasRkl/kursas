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