import numpy as np
import matplotlib.pyplot as plt

def plot_win_probabilities(num_players, player_win_probabilities):
    _, ax = plt.subplots()

    ax.bar([str(index) for index in range(num_players)], player_win_probabilities)
    ax.set_ylabel('Probability')
    ax.set_title('Simulated win probability by player id')

    plt.show()
    return

def plot_turn_count_distribution(num_trials, turn_counts):
    histogram, _ = np.histogram(turn_counts, bins=max(turn_counts) - min(turn_counts) + 1) 
    histogram = np.divide(histogram, num_trials)

    _, ax = plt.subplots()
    
    ax.bar(range(min(turn_counts), max(turn_counts)+1), histogram)
    ax.set_ylabel('Probability mass')
    ax.set_title('Simulated PMF of turns until game ending')

    plt.show()  
    return

def plot_game_history(datapoints):
    _, ax = plt.plot(range(1, datapoints+1), datapoints)

    ax.set_xlabel('Number of turns')
    ax.set_ylabel('Number of M&Ms')
    ax.set_title('History of M&Ms by turn')
    plt.show()
    return