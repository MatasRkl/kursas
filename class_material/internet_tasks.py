"""
1. Write a program that prints out all the elements of the list that are less than 5.
"""

# my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# user_number = int(input('Enter you number: '))
# def taker(lst: list[int]):
#     result = [number for number in lst if number < user_number]
#     return result
#
# print(taker(my_list))

"""
2. Create a program that asks the user for a number and then prints out a list of
all the divisors of that number. (If you don’t know what a divisor is,
it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

# user_number = int(input('Type your number: '))
#
# def find_numbers():
#     new_list = []
#     for number in range(1, 100000):
#         if number % user_number == 0:
#             new_list.append(number)
#     return new_list
#
# print(find_numbers())

"""
3. Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

def main():
    player1 = input('Player 1: rock, paper, scissors? ')
    player2 = input('Player 2: rock, paper, scissors? ')

    if player1 == 'rock' and player2 == 'paper':
        print('Player 2 WON')

main()
