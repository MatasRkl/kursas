class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_numbers(self):
        return self.x + self.y

    def substract_numbers(self):
        return self.x - self.y

    def multiply_numbers(self):
        return self.x * self.y


calculator = Calculator(5, 9)

print(calculator.add_numbers())
print(calculator.substract_numbers())
print(calculator.multiply_numbers())
