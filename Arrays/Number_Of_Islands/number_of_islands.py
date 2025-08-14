"""

Number of islands

Description: Given an m c n 2D binary grid which represents a map of '1's (land) and '0's (water) return the number of islands.

Constraints: m == grid.length, n == grid[i].length, 1 <= m, n <= 300, grid[i][j] is '0' or '1'

"""

"""

Approaches: 

We will do a DFS since it is easier to right and is written more optimally than BFS for doing a flood fill

"""

def DFS(node, visited, grid):
    # row, col = node to just extract those values
    if node in visited or node[0] < 0 or node[0] >= len(grid) or node[1] < 0 or node[1] >= len(grid[0]):
        return # on each DFS call we check the conditions for which we would skip checking a node, which is ones that are already visitied, or the coordinates are out of bounds
    
    visited.append(node) # if the initial checks are clear we know this is a new node that has never been visited, and has valid coordinates, and we mark it as visited

    if grid[node[0]][node[1]] == '0':
        return # just because the node was valid based on our previous checks doesn't mean we can't still do a return, this one being based on the fact it's a 0, I could combine it with the initial if statement condition and that is a more simple and readable way, but since this isn't being used in an official project I did it like this so that I mark all nodes as visited if they pass the basic check and ignore a visited 0
    
    DFS([node[0] - 1, node[1]], visited, grid) # DFS propagation until all 4 recursive calls return at which point all 1's would be marked as visited that are adjacently connected to the root node and count increases by 1
    DFS([node[0], node[1] + 1], visited, grid)
    DFS([node[0] + 1, node[1]], visited, grid)
    DFS([node[0], node[1] - 1], visited, grid)
    

def num_islands(grid):
    visited = []
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1' and [row, col] not in visited:
                DFS([row, col], visited, grid)
                count += 1
    
    return count


def main():
    grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","0","0","0","0"],
    ["0","1","0","1","1"]
    ]

    print(num_islands(grid))

if __name__ == "__main__":
    main()