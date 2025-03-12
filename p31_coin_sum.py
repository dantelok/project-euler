def coin_sum(coins, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        # 1 - 200
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]
            print('coin {}: dp[{}]: {}'.format(coin, i, dp[i]))

    return dp[target]


coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200
print(coin_sum(coins, target))

