from game_logic import GameLogic


dice_roller = GameLogic.roll_dice


def play():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    choice = input("> ")
    if choice == "y":
        start_game()
    else:
        print("OK. Maybe another time")


def start_game():
    round_num = 1
    max_round = 2
    total_points = 0
    while round_num <= max_round:
        round_result = do_round(round_num)
        print(f"You banked {round_result} points in round {round_num}")
        total_points += round_result
        print(f"Total score is {total_points} points")
        round_num += 1
    print(f"Thanks for playing. You earned {total_points} points")


def do_round(round_num):
    print(f"Starting round {round_num}")
    while True:
        roll = do_roll()
        if GameLogic.calculate_score(roll) == 0:
            print("***** Zilch!!! Round over *****")
            return 0
        keepers = confirm_keepers()
        return GameLogic.calculate_score(keepers)


def confirm_keepers():
    print("Enter dice to keep")
    keeper_string = input("> ")
    values = [int(value) for value in keeper_string]
    return tuple(values)


def do_roll():
    print(f"Rolling 6 dice...")
    roll = dice_roller()
    print(roll)
    return roll


if __name__ == '__main__':
    play()
