#import re
R, C, T = [int(i) for i in input().strip().split()]

grid = []

for i in range(R):
    grid.append(list(input().strip()))

"""print(R,C,T,"Before grid")

#for g_value in grid:
#    print(g_value) """

g_or = list(grid)

for _ in range(2,T+1):

    if _ % 2 == 0 :

        for i,row in enumerate(grid):

            grid[i] = ['E' if val == 'O' else 'O' for val in row ]


    else:

        for i, row in enumerate(grid):
            while 'E' in row:

                e_index = row.index('E')
                grid[i][e_index] = '.'
                if e_index-1 > -1 and grid[i][e_index-1] != 'E':
                    grid[i][e_index-1] = '.'
                if e_index+1 < C and grid[i][e_index+1] != 'E':
                    grid[i][e_index+1] = '.'
                if i-1 > -1 and grid[i-1][e_index] != 'E':
                    grid[i-1][e_index] = '.'
                if i+1 < R - 1 and grid[i+1][e_index] != 'E':
                    grid[i+1][e_index] = '.'

    if _ == T and _ % 2 == 0 :

        for i,row in enumerate(grid):

            grid[i] = ['O' if val == 'E' else 'O' for val in row ]

    if g_or == grid:
        e_b = _
        break

print("Final out put: ")
for g_value in grid:
    print("".join(g_value))

print(e_b, ": this is break point")