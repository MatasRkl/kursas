from class_material.classes.db_class import DB

db = DB()
db.create_connection_if_not_exist()

tables = [
    'CREATE TABLE IF NOT EXISTS engine (engine_id Integer PRIMARY KEY AUTOINCREMENT,'
    ' engine_type char,  cc_displacement char, Power_BHP integer, Torque_Nm integer, Fuel_type char);',
    'CREATE TABLE IF NOT EXISTS model_type (model_type_id Integer PRIMARY KEY AUTOINCREMENT,'
    ' Make char, Seating_capacity integer, Fuel_tank_capacity_L integer);',
    'CREATE TABLE IF NOT EXISTS Model (model_id Integer PRIMARY KEY AUTOINCREMENT,'
    ' Car_name char, Mileag_km integer, Model char); ',
    'CREATE TABLE IF NOT EXISTS Market(market_id Integer PRIMARY KEY AUTOINCREMENT,'
    ' Price integer, Make_year integer, Color char, Mileage_run integer, No_of_owners integer);']

# for table in tables:
#     db.execute_sql_query(table)


db.delete_row_from_db('Model', 'model_id = 1')

# db.add_data_model(model_id=1, Car_name='Audi', Mileag_km=228300, Model='A3')
# db.add_data_market(market_id=2, Price=2000, Make_year=1999, Color='Red', Mileage_run=156789, No_of_owners=2)
# query = "SELECT * FROM Model"
# result = db.get_data_from_db(query)
# for row in result:
#     print(row)


# db.execute_sql_query(tables)
db.close_connection()


'''
INSERT INTO Model (model_id, car_name, Mile_ag_km, Model ) VALUES (1, zapas, 15, zapas2000)
'''