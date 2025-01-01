import numpy as np
from utils import plot_game_history

class MultipleDenominationsSim:
    """
        Initializes the game based on the number of M&Ms each player has and their respective coin weights (i.e., probability it comes up heads and M&M is consumed).
        The game ends when at most one player has a nonzero number of M&Ms.

        Arguments:

        - player_mms: List of integers respresenting the number of M&Ms each player has
        - denominations: List of list of integers representing the denomination of each player's coins
    """
    def __init__(self, player_mms, denominations):
        datatype_check = True
        datatype_check &= type(player_mms) == int
        datatype_check &= type(denominations) == list[int]

        value_check = True
        value_check &= player_mms > 0
        for denomination in denominations:
            value_check &= denomination > 0

        assert datatype_check
        assert value_check

        self.player_mms = player_mms
        self.denominations = denominations

    """
        Runs one instance of the sim according to the set parameters.

        Arguments:

        - logging: Boolean value for whether to record historical values
    """
    def run_sim(self, logging=False):
        player_mms = self.player_mms
        denominations = self.denominations

        game_turns = 0
        game_logs = []

        while player_mms > 0:
            for denomination in denominations:
                player_mms -= np.random.binomial(1, denomination)
                if player_mms < 0: player_mms = 0
            game_turns += 1
            if logging: game_logs.append(player_mms)

        if logging: plot_game_history(game_logs)

        if logging: return game_turns, game_logs
        else: return game_turns