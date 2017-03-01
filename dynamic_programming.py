def rod_cutting(n, prices, memo={}):
    if n <= 0:
        return 0

    if n not in memo:
        memo[n] = max(prices[i] + rod_cutting(n-i-1, prices, memo) for i in range(n))

    return memo[n]


if __name__ == '__main__':
    prices = [3, 5, 8, 9, 10, 17, 17, 20]
    print(rod_cutting(8, prices))
