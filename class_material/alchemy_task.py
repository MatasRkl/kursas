"""
Sukurti programą, kuri:

Leistų įvesti darbuotojus: vardą, pavardę, gimimo datą, pareigas, atlyginimą,
nuo kada dirba (data būtų nustatoma automatiškai, pagal dabartinę datą).
Duomenys būtų saugomi duomenų bazėję, panaudojant SQLAlchemy ORM (be SQL užklausų)
Vartotojas galėtų įrašyti, peržiūrėti, ištrinti ir atnaujinti darbuotojus.
"""

from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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

    def add_employee(self, name, surname, birth_date, position, salary):
        new_employee = Employee(name=name, surname=surname, birth_date=birth_date, position=position, salary=salary)
        session.add(new_employee)
        session.commit()

    def view_employees(self):
        employees = session.query(Employee).all()
        for employee in employees:
            print(f'{employee.name} {employee.surname} - {employee.position}')

    def delete_employee(self, id):
        employee = session.query(Employee).filter(Employee.id == id).first()
        session.delete(employee)
        session.commit()

    def update_employee(self, id, **kwargs):
        employee = session.query(Employee).filter(Employee.id == id).first()
        for key, value in kwargs.items():
            setattr(employee, key, value)
        session.commit()


engine = create_engine('sqlite:///database/employees.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
