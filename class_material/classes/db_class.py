from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import Column, Integer, String

class DB:
    def __init__(self, url):
        self.url = url
        self.engine = create_engine(url)
        self.meta = MetaData()

    def __connect_to_db(self):
        return self.engine.connect()

    def __execute_query(self, sql_query):
        with self.__connect_to_db() as connection:
            result = connection.execute(sql_query)
            return result.fetchall()

    def create_table(self, table_name, columns):
        table = Table(table_name, self.meta, *columns)

        with self.__connect_to_db() as connection:
            table.create(connection)
        print(f"Table '{table_name}' was created")


db = DB("postgresql://Mano:matouse@localhost/cars")