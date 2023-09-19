# The solution for Hunting Grounds, a 2D prefix sum table problem
# 2D because the classic version is just a 1D prefix sum array
# The prefix sum table we construct is a sum of all the elements to the up and left from a point at each point

# Example grid:
#  1  2  3  4
#  5  6  7  8
#  9 10 11 12
# 13 14 15 16
# Example prefix sum table:
#  1  3  6 10
#  6 14 24 36
# 15 33 54 78
# 28 60 96 136
# We will actually pad our table with zeros on the left and top
# This is also why I made the input 1 indexed :)
# 0  0  0  0  0
# 0  1  3  6 10
# 0  6 14 24 36
# 0 15 33 54 78
# 0 28 60 96 136

def run():

    # read in input
    n, q = tuple(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(n)]
    queries = [tuple(map(int, input().split())) for _ in range(q)]

    # construct the prefix sum table, padded with a row and column of 0s
    ps_table = [[0]*(len(grid[0])+1)]
    for row in grid:
        ps_row = [0]
        for i, v in enumerate(row):
            # for squares a b
            #             c d
            # in our prefix sum table, we are constructing d by
            # c, b, the grid spot at d and subtracting a
            # a is the overlap between c and b
            ps_row.append(row[i] + ps_row[-1] + ps_table[-1][i+1] - ps_table[-1][i])
        ps_table.append(ps_row)

    # answer the queries using the prefix sum table
    # for a query containing the grid spots in *s the sum is:
    # h - g - f + e from the prefix sum table
    # 0  e  0  g  0
    # 0  1  *  * 10
    # 0  6  *  * 36
    # 0  f  *  h 78
    # 0 28 60 96 136
    for y1, x1, y2, x2 in queries:
        e, f, g, h = ps_table[y1-1][x1-1], ps_table[y2][x1-1], ps_table[y1-1][x2], ps_table[y2][x2]
        value = h - g - f + e
        print(value)

if __name__ == "__main__":
    run()