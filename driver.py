from MMGame import MMGame

player_mms = [5, 5]
coin_weights = [0.5, 0.5]

game = MMGame(player_mms, coin_weights)
player_win_probabilities, tie_probability, expected_turns = game.run_trials(10000)
print(f"Win probabilities: {player_win_probabilities}")
print(f"Tie probability: {tie_probability}")
print(f"E[turns]: {expected_turns}")