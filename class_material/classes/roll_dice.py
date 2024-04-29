import random

class RollDice:
    def __init__(self):
        pass


    def roll_the_dice(self):
        rolls = []
        roll_number = 1
        while roll_number <= 10:
            dice_number = int(input(f'Type how many dices you want for roll {roll_number} (max 5): '))
            while dice_number > 5:
                print('MAX number of dices is 5!!')
                dice_number = int(input(f'Type how many dices you want for roll {roll_number} (max 5): '))
            dice_sides = int(input(f'Type how many sides do those dices have for roll {roll_number} (1-100): '))
            while dice_sides > 100:
                print('MAX number of dice sides is 100!!')
                dice_sides = int(input(f'Type how many sides do those dices have for roll {roll_number} (1-100): '))
            rolls.append([random.randint(1, dice_sides) for _ in range(dice_number)])
            roll_number += 1
        return rolls


dice_game = RollDice()
results = dice_game.roll_the_dice()

roll_number = 1
for result in results:
    print(f"Roll {roll_number}: {result}")
    roll_number += 1