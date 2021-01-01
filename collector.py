def collector(coins, mags, n):
    """
    Finds a path that maximizes points
    Args:
        coins (List[List[int]]): 1 at coins[i][j] if there's a coin at (i,j), else 0
        mags (List[List[int]]): 1 at mags[i][j] if there's a magnifier at (i,j), else 0
        n (int): dimensions of the nxn board
    """
    parent = dict()
    memo = dict()

    def dp(i,j,m):

        if (i,j,m) in memo:
            return memo[(i,j,m)]

        if i == n-1 and j == n-1:
            if coins[i][j] == 1:
                memo[(i,j,m)] = 2**m
                return 2**m
            else:
                memo[(i,j,m)] = 0
                return 0

        right = 0
        n_right = None
        down = 0
        n_down = None
        #right case
        if j+1 < n:
            if mags[i][j] == 1:
                right = dp(i,j+1,m+1)
                n_right = (i,j+1,m+1)
            else:
                if coins[i][j] == 1:
                    right = dp(i,j+1,m) + 2**m
                else:
                    right = dp(i,j+1,m)
                n_right = (i,j+1,m)

        #down case
        if i+1 < n:
            if coins[i][j] == 1:
                down = dp(i+1,j,0) + 2**m
            else:
                down = dp(i+1,j,0)
            n_down = (i+1,j,0)

        if right >= down and n_right != None:
            parent[(i,j,m)] = n_right
            memo[(i,j,m)] = right
        else:
            parent[(i,j,m)] = n_down
            memo[(i,j,m)] = down
        return memo[(i,j,m)]

    dp(0,0,mags[0][0])
    optpath = []
    curr = (0,0,mags[0][0])
    optpath.append((curr[0],curr[1]))
    while(curr[0]!= n-1 or curr[1]!= n-1):
        curr = parent[curr]
        optpath.append((curr[0],curr[1]))
    return optpath
