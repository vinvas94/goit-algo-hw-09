import timeit

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount %= coin
    return result

def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]  
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    
    # Check for an impossible solution
    if dp[amount] == float('inf'):
        raise ValueError("It is impossible to find a solution for this amount with the given denominations.")
    
    # Restore the number of coins used
    while amount > 0:
        coin = coin_used[amount]
        if coin == -1:
            raise ValueError(f"Impossible to find minimum coins for amount {amount}.")
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


def compare_algorithms(amount):
    # Limit large amounts for dynamic programming
    if amount > 100000:
        print(f"Amount {amount} is too large for dynamic programming.")
        return
    
    # Measure time for greedy algorithm
    greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=100)
    print(f"Greedy algorithm execution time: {greedy_time} seconds for 100 executions")
    
    # Measure time for dynamic programming algorithm
    dp_time = timeit.timeit(lambda: find_min_coins(amount), number=100)
    print(f"Dynamic programming algorithm execution time: {dp_time} seconds for 100 executions")

if __name__ == "__main__":
    amounts_to_test = [100, 500, 1000, 10000, 123, 997, 2501, 12345, 999731] 
    for amount in amounts_to_test:
        print(f"Measuring execution time for amount: {amount}")
        compare_algorithms(amount)
        print("\n")
