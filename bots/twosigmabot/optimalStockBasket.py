"""
Medium

Codewriting

2000

You are picking a series of optimum stocks for your investment portfolio. Thankfully, you have at your disposal a tool called ACME optimizer. For each stock it provides the expected future return in 1 year, as well as the expected risk during the same period. Your goal is to implement a stock picker which will maximize the sum of expected future returns while keeping the total risk within your risk budget (riskBudget).

Example

For stocks = [[-1, 2], [10, 15], [11, 13], [9, 10]] and riskBudget = 30, the output should be
optimalStockBasket(stocks, riskBudget) = 21.

It's a bad idea to pick the first stock because its expected future return is negative.
You can pick no more than two stocks from the remaining three because 15 + 13 + 10 > 30 (i.e. the total risk exceeds the risk budget if you pick all three of them). On the other hand, you can pick any pair of stocks because 15 + 13 ≤ 30, 15 + 10 ≤ 30, 13 + 10 ≤ 30.
To maximize the sum of expected future returns according to ACME optimizer predictions you need to pick the second and third stocks (1-based). The total future return in this case equals 10 + 11 = 21.

KNAPSACK PROBLEM
"""


def optimalStockBasket(stocks, riskBudget):
    stocks = [s for s in stocks if s[0] > 0]
    A = [[0 for _ in range(riskBudget + 1)] for _ in range(len(stocks))]

    for i in range(len(stocks)):
      for j in range(riskBudget + 1):
        if stocks[i][1] > j:
          A[i][j] = A[i-1][j]
        else:
          A[i][j] = max(A[i-1][j], A[i-1][j-stocks[i][1]] + stocks[i][0])
    if A:
      return A[-1][-1]
    else:
      return 0

