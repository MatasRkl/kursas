class Record:
    def __init__(self, type_1: str, sum_1: float):
        self.sum_1 = sum_1
        self.type_1 = type_1

    def __str__(self):
        return f'{self.type_1}: {self.sum_1}'


class Budget:
    def __init__(self):
        self.journal = []

    def add_income_record(self, sum_1):
        income = Record('Income', sum_1)
        self.journal.append(income)

    def add_expenses_record(self, sum_1):
        expenses = Record('Expenses', sum_1)
        self.journal.append(expenses)

    def get_balance(self):
        balance = 0
        for record in self.journal:
            if record.type_1 == 'Income':
                balance += record.sum_1
            if record.type_1 == 'Expenses':
                balance -= record.sum_1

        print(balance)

    def show_report(self):
        for record in self.journal:
            if record.type_1 == 'Income':
                print(f'Incomes: {record}')
            if record.type_1 == 'Expenses':
                print(f'Expenses: {record}')


budget = Budget()

while True:
    choice = int(input('1 - Give income, \n2 - Give expenses, \n3 - Get balance, \n4 - Show report, \n5 - Exit: '))
    if choice == 1:
        sum_1 = float(input('Type income sum: '))
        budget.add_income_record(sum_1)
    elif choice == 2:
        sum_1 = float(input('Type expenses sum: '))
        budget.add_expenses_record(sum_1)
    elif choice == 3:
        budget.get_balance()
    elif choice == 4:
        budget.show_report()
    elif choice == 5:
        break
