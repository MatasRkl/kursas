import random

class Tank:
    def __init__(self):
        self.x = 5 #coordinates
        self.y = 5 #coordinates
        self.direction = 'north'
        self.shots = {'north': 0, 'east': 0, 'south': 0, 'west': 0}
        self.board = [['_'] * 10 for _ in range(10)]
        self.board[self.y][self.x] = '_'
        self.target_x = random.randint(0, 9)
        self.target_y = random.randint(0, 9)
        self.board[self.target_y][self.target_x] = 'O'


    def display(self):
        display_board = [row[:] for row in self.board]

        tank_symbol = ''
        if self.direction == 'north':
            tank_symbol = '^'
        elif self.direction == 'south':
            tank_symbol = 'v'
        elif self.direction == 'east':
            tank_symbol = '>'
        elif self.direction == 'west':
            tank_symbol = '<'

        display_board[len(display_board) - self.y - 1][self.x] = tank_symbol

        for row in display_board:
            print(' '.join(row))


    def forward(self):
        if self.direction == 'north':
            self.y += 1
        elif self.direction == 'south':
            self.y -= 1
        elif self.direction == 'east':
            self.x += 1
        elif self.direction == 'west':
            self.x -= 1

    def turn_left(self):
        if self.direction == 'north':
            self.direction = 'west'
        elif self.direction == 'south':
            self.direction = 'east'
        elif self.direction == 'east':
            self.direction = 'north'
        elif self.direction == 'west':
            self.direction = 'south'

    def turn_right(self):
        if self.direction == 'north':
            self.direction = 'east'
        elif self.direction == 'east':
            self.direction = 'south'
        elif self.direction == 'south':
            self.direction = 'west'
        elif self.direction == 'west':
            self.direction = 'north'

    def back(self):
        if self.direction == 'north':
            self.y -= 1
        elif self.direction == 'south':
            self.y += 1
        elif self.direction == 'east':
            self.x -= 1
        elif self.direction == 'west':
            self.x += 1

    def fire(self):
        self.shots[self.direction] += 1

        if (self.direction == 'north' and self.x == self.target_x and self.y > self.target_y) or \
                (self.direction == 'south' and self.x == self.target_x and self.y < self.target_y) or \
                (self.direction == 'east' and self.y == self.target_y and self.x > self.target_x) or \
                (self.direction == 'west' and self.y == self.target_y and self.x < self.target_x):
            print("Target hit!")

            self.board[self.target_y][self.target_x] = '_'

            self.target_x = random.randint(0, 9)
            self.target_y = random.randint(0, 9)
            self.board[self.target_y][self.target_x] = 'O'
        else:
            print("Missed the target!")


tank_game = Tank()

while True:
    tank_game.display()
    action = input('Type your action (forward, back, turn left, turn right, FIRE, info, end): ')
    if action == 'end':
        break
    elif action == 'forward':
        tank_game.forward()
    elif action == 'turn left':
        tank_game.turn_left()
    elif action == 'turn right':
        tank_game.turn_right()
    elif action == 'back':
        tank_game.back()
    elif action == 'FIRE':
        tank_game.fire()
