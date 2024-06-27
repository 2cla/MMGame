from MMGame import MMGame
from utils import plot_win_probabilities, plot_turn_count_distribution

player_mms = [5, 5]
coin_weights = [0.5, 0.5]
num_trials = 10000

game = MMGame(player_mms, coin_weights)
player_win_probabilities, tie_probability, turn_counts = game.run_trials(num_trials)
print(f'Win probabilities: {player_win_probabilities}')
print(f'Tie probability: {tie_probability}')
print(f'E[turns]: {sum(turn_counts) / num_trials}')

plot_win_probabilities(len(player_mms), player_win_probabilities)
plot_turn_count_distribution(num_trials, turn_counts)