def coin_change(coins, amount):
    # Sort coins in descending order to use the largest denominations first
    coins.sort(reverse=True)
    
    # Initialize the count of coins used
    coin_count = 0
    
    # Iterate through each coin denomination
    for coin in coins:
        # Use as many of this coin as possible
        if amount >= coin:
            num_coins = amount // coin  # Number of this coin to use
            coin_count += num_coins     # Add to the total coin count
            amount -= num_coins * coin  # Reduce the remaining amount
    
    # Return the total number of coins used
    return coin_count

# Example usage
coins = [1, 5, 10, 25]
amount = 63
print(f"Minimum coins needed: {coin_change(coins, amount)}")
