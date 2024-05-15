import sqlite3
import os

class DB:
    def __init__(self, file_name="cars.db"):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        self.url = os.path.join(desktop_path, file_name)
        self.cursor = None
        self.connection = None

        if not os.path.exists(self.url):
            self.create_connection_if_not_exist()

    def create_connection_if_not_exist(self):
        self.connection = sqlite3.connect(self.url)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.cursor.close()

    def execute_sql_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def add_data_model(self, **kwargs):
        sql_query = (
            f"Insert into Model (model_id, Car_name, Mileag_km, Model) "
            f'values ("{kwargs["model_id"]}", "{kwargs["Car_name"]}", "{kwargs['Mileag_km']}", "{kwargs['Model']}")'
        )
        self.execute_sql_query(sql_query)

    def add_data_market(self, **kwargs):
        sql_query = (
            f"Insert into Market (market_id, Price, Make_year, Color, Mileage_run, No_of_owners) "
            f'values ("{kwargs["market_id"]}", "{kwargs["Price"]}", "{kwargs['Make_year']}", "{kwargs['Color']}",'
            f'"{kwargs['Mileage_run']}", "{kwargs['No_of_owners']}")'
        )
        self.execute_sql_query(sql_query)

    def add_data_engine(self, **kwargs):
        sql_query = (
            f"Insert into engine (engine_id, engine_type, cc_displacement, Power_BHP, Torque_Nm, Fuel_type) "
            f'values ("{kwargs["engine_id"]}", "{kwargs["engine_type"]}",'
            f' "{kwargs['cc_displacement']}", "{kwargs['Power_BHP']}",'
            f'"{kwargs['Torque_Nm']}", "{kwargs['Fuel_type']}")'
        )
        self.execute_sql_query(sql_query)

    def add_data_model_type(self, **kwargs):
        sql_query = (
            f"Insert into model_type (model_type_id, Make, Seating_capacity, Fuel_tank_capacity_L) "
            f'values ("{kwargs["model_type_id"]}", "{kwargs["Make"]}",'
            f' "{kwargs['Seating_capacity']}", "{kwargs['Fuel_tank_capacity_L']}"'
        )
        self.execute_sql_query(sql_query)

    def get_data_from_db(self, query):
        self.execute_sql_query(query)
        data = self.cursor.fetchall()
        return data

    def delete_row_from_db(self, table, condition):
        sql_query = f"DELETE FROM {table} WHERE {condition}"
        self.execute_sql_query(sql_query)


    def drop_tables_if_exist(self, table):
        sql_query = f"Drop table if exists {table}"
        self.execute_sql_query(sql_query)