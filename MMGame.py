import numpy as np

class MMGame:
    """
        Initializes the game based on the number of M&Ms each player has and their respective coin weights (i.e., probability it comes up heads and M&M is consumed).
        The game ends when at most one player has a nonzero number of M&Ms.

        Arguments:

        - player_mms: List of integers respresenting the number of M&Ms each player has
        - coin_weights: List of floats representing the probability each player's coin turns up heads
    """
    def __init__(self, player_mms, coin_weights):
        assert len(player_mms) == len(coin_weights)
        assert len(player_mms) > 1

        datatype_check = True
        for player_mm in player_mms: datatype_check &= type(player_mm) == int
        for coin_weight in coin_weights: datatype_check &= type(coin_weight) == float

        assert datatype_check

        player_mms = np.array(player_mms)
        coin_weights = np.array(coin_weights)

        assert not np.any(player_mms < 0)
        assert np.all(coin_weights >= 0.0) and np.all(coin_weights <= 1.0)

        self.player_mms = player_mms
        self.coin_weights = coin_weights

    """
        Runs one instance of the game according to the set parameters.
    """
    def run_game(self):
        player_mms = self.player_mms.copy()
        coin_weights = self.coin_weights

        game_turns = 0

        while np.count_nonzero(player_mms) > 1:
            for index, player_mm in enumerate(player_mms):
                if player_mm:
                    player_mms[index] -= np.random.binomial(1, coin_weights[index])
            game_turns += 1

        winner = np.nonzero(player_mms)[0]

        if not len(winner): winner = -1
        else: winner = winner[0]

        return winner, game_turns

    """
        Runs a set number of trials of the game.

        Arguments:

        - trial_count: Integer representing number of trials to run

        Returns:

        - player_win_probabilities: List of floats containing the simulated probabilities of winning for each player
        - tie_probability: Float representing the simulated probability of a tie
        - turn_counts: List of integers containing the number of turns that took place during each trial
    """
    def run_trials(self, trial_count):
        assert type(trial_count) == int
        assert trial_count

        player_win_count = [0]*self.player_mms.shape[0]
        turn_counts = []
        tie_count = 0

        for _ in range(trial_count):
            winner, game_turns = self.run_game()

            if winner == -1: tie_count += 1
            else: player_win_count[winner] += 1

            turn_counts.append(game_turns)

        player_win_probabilities = [player_wins / trial_count for player_wins in player_win_count]
        tie_probability = tie_count / trial_count

        return player_win_probabilities, tie_probability, turn_counts
