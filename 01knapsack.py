def knapsack(wt, val, W):
    n = len(wt)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):

            if wt[i-1] <= w:
                include = val[i-1] + dp[i-1][w-wt[i-1]]
                exclude = dp[i-1][w]
                dp[i][w] = max(include, exclude)

            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]


wt = [1, 2, 3]
val = [10, 15, 40]
W = 4

print("Maximum Profit:", knapsack(wt, val, W))