from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
from alchemy_task import Employee
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///database/employees.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

employee = Employee()


# employee.add_employee("Matas", "Riklius", datetime(1999, 04, 28), "Developer", 50000)
# employee.add_employee("Reyna", "Volkswagen", datetime(1985, 8, 20), "Manager", 60000)
#
# print("Employees:")
# employee.view_employees()

# employee.delete_employee(1)

employee.update_employee(5, salary=50000)

