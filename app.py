import random


player_1_name = input("Player 1 name")
player_2_name = input("Player 2 name")


def main():
    player_1 = 0
    player_1_wins = 0
    player_2 = 0
    player_2_wins = 0
    rounds = 1

    while rounds <= 5:
        print("Round " + str(rounds))
        player_1 = roll_dice()
        player_2 = roll_dice()
        print(player_1_name + " rolled a: " + str(player_1))
        print(player_2_name + " rolled a: " + str(player_2))

        if player_1 == player_2:
            print("This round is a draw!\n")

        elif player_1 > player_2:
            player_1_wins = player_1_wins + 1
            print(player_1_name + " wins this round!\n")

        else:
            player_2_wins = player_2_wins + 1
            print(player_2_name + " wins this round!\n")

        rounds = rounds + 1

    if player_1_wins == player_2_wins:
        print("Game is a draw!")

    elif player_1_wins > player_2_wins:
        print(player_1_name + " wins the game! Rounds won: " + str(player_1_wins))

    else:
        print(player_2_name + " wins the game! Rounds won: " + str(player_2_wins))


def roll_dice():
    rollDice = random.randint(1, 6)
    return rollDice


main()
