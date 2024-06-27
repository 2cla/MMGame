import numpy as np

class MMGame:
    def __init__(self, player_mms, coin_weights):
        assert len(player_mms) == len(coin_weights)
        assert len(player_mms) > 1

        datatype_check = True
        for player_mm in player_mms: datatype_check &= type(player_mm) == int
        for coin_weight in coin_weights: datatype_check &= type(coin_weight) == float

        player_mms = np.array(player_mms)
        coin_weights = np.array(coin_weights)

        assert not np.any(player_mms < 0)
        assert np.all(coin_weights >= 0.0) and np.all(coin_weights <= 1.0)

        self.player_mms = player_mms
        self.coin_weights = coin_weights

    def run_game(self):
        player_mms = self.player_mms.copy()
        coin_weights = self.coin_weights.copy()

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

    def run_trials(self, trial_count):
        player_win_count = [0]*self.player_mms.shape[0]
        total_turns = 0
        tie_count = 0

        for _ in range(trial_count):
            winner, game_turns = self.run_game()

            if winner == -1: tie_count += 1
            else: player_win_count[winner] += 1

            total_turns += game_turns

        player_win_probabilities = [player_wins / trial_count for player_wins in player_win_count]
        tie_probability = tie_count / trial_count
        expected_turns = total_turns / trial_count

        return player_win_probabilities, tie_probability, expected_turns
