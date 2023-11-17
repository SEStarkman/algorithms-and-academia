import random

def simulate_coin_flip(n):
    longest_streak = 0
    current_streak = 1
    last_flip = None
    heads_count = 0
    tails_count = 0

    for _ in range(n):
        flip = random.choice(['Heads', 'Tails'])
        if flip == 'Heads':
            heads_count += 1
        else:
            tails_count += 1

        if flip == last_flip:
            current_streak += 1
        else:
            longest_streak = max(longest_streak, current_streak)
            current_streak = 1

        last_flip = flip

    # Check for the final streak
    longest_streak = max(longest_streak, current_streak)

    return heads_count, tails_count, longest_streak

# Example usage
n = 100000  # Replace with the number of times you want to flip the coin
heads_count, tails_count, longest_streak = simulate_coin_flip(n)
print(f"After {n} coin flips:")
print(f"Heads: {heads_count}, Tails: {tails_count}")
print(f"Longest streak of either Heads or Tails: {longest_streak}")
print(f"Percentage of Heads: {round(heads_count/n*100, 2)}%, Tails: {round(tails_count/n*100, 2)}%")
