import random

MAX_SCORE = 50

# generate a random roll from min to max
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


def players():
    while True:
        players = input("Enter number of players (1-4): ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                break
            else:
                print("Must be between 2 - 4 players.")
        else:
            print("Invalid, try again.")
    return players


def main():
    player_score = [0 for _ in range(players())]
    
    # max() returns highest value inside list
    while max(player_score) < MAX_SCORE:
        for player_idx in range(len(player_score)):
            print(f"\nPlayer {player_idx + 1}'s turn has just started!")
            print(f"Your total score is: {player_score[player_idx]}.\n")
            current_score = 0

            while True:
                should_roll = input("Would you like to roll? (enter for yes) ")
                if should_roll.lower() != "":
                    break

                value = roll()
                if value == 1:
                    print("You rolled a 1! Turn done!")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print(f"You roll a {value}!")
                print("Your score is: ", current_score)

            player_score[player_idx] += current_score
            print("Your total score is: ", player_score[player_idx])

    max_score = max(player_score)
    winning_idx = player_score.index(max_score)
    print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)

# execute main
main()