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
        self.points = 200

    def all_shots(self):
        return sum(self.shots.values())

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

        display_board[9 - self.y][self.x] = tank_symbol

        for row in display_board:
            print(' '.join(row))


    def forward(self):
        if self.direction == 'north':
            self.y += 1
            self.points -= 10
        elif self.direction == 'south':
            self.y -= 1
            self.points -= 10
        elif self.direction == 'east':
            self.x += 1
            self.points -= 10
        elif self.direction == 'west':
            self.x -= 1
            self.points -= 10

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
            self.points -= 10
        elif self.direction == 'south':
            self.y += 1
            self.points -= 10
        elif self.direction == 'east':
            self.x -= 1
            self.points -= 10
        elif self.direction == 'west':
            self.x += 1
            self.points -= 10

    def fire(self):
        self.shots[self.direction] += 1
        self.hit_count = 0

        if (self.direction == 'north' and self.x == self.target_x and 9 - self.y > self.target_y) or \
                (self.direction == 'south' and self.x == self.target_x and 9 - self.y < self.target_y) or \
                (self.direction == 'east' and 9 - self.y == self.target_y and self.x < self.target_x) or \
                (self.direction == 'west' and 9 - self.y == self.target_y and self.x > self.target_x):
            print("Target hit!")
            self.hit_count += 1
            self.points += 50
            self.board[self.target_y][self.target_x] = '_'
            self.target_x = random.randint(0, 9)
            self.target_y = random.randint(0, 9)
            self.board[self.target_y][self.target_x] = 'O'
        else:
            print("Missed the target!")

    def info(self):
        print('Tanks is facing: ', self.direction)
        print('Tanks coordinates are: ', self.x, self.y)
        print('Tanks shots in directions: ', self.shots)
        print('All shots: ', self.all_shots())

tank_game = Tank()

while True:
    tank_game.display()
    action = input('Type your action (forward, back, turn left, turn right, FIRE, info, end): ')
    print('Your points: ', tank_game.points)
    if action == 'end':
        print('You destroyed ', tank_game.hit_count, ' targets')
        name = input('Type your name you monster: ')
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
    elif action == 'info':
        tank_game.info()
