from MMGame import MMGame
from MultipleDenominationsSim import MultipleDenominationsSim
from utils import plot_win_probabilities, plot_turn_count_distribution
from math import comb
c,k = 5, 5
ans = 0
for m in range(c):
    for n in range(m+1):
        ans += 2 * (m+k-n) / (3 ** (m+k-n)) * comb(m+k-n-1, n) * comb(m+k-2*n-1, k-n-1)
for m in range(k):
    for n in range(min(c, m+1)):
        temp = (m+c-n) / (3 ** (m+c-n)) * comb(m+c-n-1, n) * comb(m+c-2*n-1, c-n-1)
        ans += 2 * temp
        if m == k-1: ans -= temp
print(ans * 4/3)

player_mms = 100
denominations = [-5, 2, 3]
sim = MultipleDenominationsSim(player_mms, denominations)
sim.run_sim(logging=True)

"""player_mms = [5, 5]
coin_weights = [0.5, 0.5]
num_trials = 100000

game = MMGame(player_mms, coin_weights)
player_win_probabilities, tie_probability, turn_counts = game.run_trials(num_trials)
print(f'Win probabilities: {player_win_probabilities}')
print(f'Tie probability: {tie_probability}')
print(f'E[turns]: {sum(turn_counts) / num_trials}')"""

# plot_win_probabilities(len(player_mms), player_win_probabilities)
# plot_turn_count_distribution(num_trials, turn_counts)

