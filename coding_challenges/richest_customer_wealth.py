def max_wealth(accounts):
    max_wealth = 0
    for i in accounts:
        val = sum(i)
        if val > max_wealth:
            max_wealth = val
    
    return max_wealth


if __name__ == '__main__':
    accounts = [[1,5],[7,3],[3,5]]
    accounts2 = [[2,8,7],[7,1,3],[1,9,5]]
    print(max_wealth(accounts2))