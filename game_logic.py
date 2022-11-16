from collections import Counter
from random import randint


class GameLogic:
    @staticmethod
    def roll_dice():
        return tuple([randint(1, 6) for _ in range(6)])

    @staticmethod
    def calculate_score(dice):
        """
        dice is a tuple of integers that represent the user's selected dice pulled out from current roll
        """
        fives = Counter(dice)[5]
        ones = Counter(dice)[1]
        return fives * 50 + ones * 100
