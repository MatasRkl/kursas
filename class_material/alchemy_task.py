"""
Sukurti programą, kuri:

Leistų įvesti darbuotojus: vardą, pavardę, gimimo datą, pareigas, atlyginimą,
nuo kada dirba (data būtų nustatoma automatiškai, pagal dabartinę datą).
Duomenys būtų saugomi duomenų bazėję, panaudojant SQLAlchemy ORM (be SQL užklausų)
Vartotojas galėtų įrašyti, peržiūrėti, ištrinti ir atnaujinti darbuotojus.
"""

from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    birth_date = Column(Date)
    position = Column(String)
    salary = Column(Integer)
    start_date = Column(Date, default=datetime.now)

engine = create_engine('sqlite:///database/employees.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_employee(name, surname, birth_date, position, salary):
    new_employee = Employee(name=name, surname=surname, birth_date=birth_date, position=position, salary=salary)
    session.add(new_employee)
    session.commit()

def view_employees():
    employees = session.query(Employee).all()
    for employee in employees:
        print(f'{employee.name} {employee.surname} - {employee.position}')

def delete_employee(id):
    employee = session.query(Employee).filter(Employee.id == id).first()
    session.delete(employee)
    session.commit()

def update_employee(id, **kwargs):
    employee = session.query(Employee).filter(Employee.id == id).first()
    for key, value in kwargs.items():
        setattr(employee, key, value)
    session.commit()

add_employee("John", "Doe", datetime(1990, 5, 15), "Developer", 50000)
add_employee("Jane", "Smith", datetime(1985, 8, 20), "Manager", 60000)

print("Employees:")
view_employees()

delete_employee(1)

print("\nAfter deleting an employee:")
view_employees()

update_employee(2, position="Senior Manager")

print("\nAfter updating an employee:")
view_employees()
