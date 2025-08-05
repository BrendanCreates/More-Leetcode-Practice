"""

Sprial matrix

Description: Given an mxn matrix reutnr all elements of the matrix in sprial order

Constraints: m == matrix.length, n == matrix[i].length, 1 <= m, n <= 10 (doesnt have to be square, m is rows and n is cols), -100 <= matrix[i][j] <= 100

"""

"""

Approaches: 

first thing we are always doing is going right along the first row front to back, then we go a row below that end point and go to the end, so I think representing this in math terms will express the pattern better

After working it out a little bit it is best to approach creating the "arrows" in a repeatable  pattern which makes the code easier to write, each arrow will be parameterized by the bounds which are  modified in each iteration of the loop and the conditions for the arrows will determine if we evaluate along that arrow or skip it

"""

def sprial_matrix(matrix):
    result = []
    row_min, col_min = 0, 0
    row_max = len(matrix) - 1
    col_max = len(matrix[0]) - 1

    while row_min <= row_max and col_min <= col_max:
        # top
        for i in range(col_min, col_max + 1):
            result.append(matrix[row_min][i])
        row_min += 1

        # right
        for i in range(row_min, row_max + 1):
            result.append(matrix[i][col_max])
        col_max -= 1

        # bottom
        if row_min <= row_max:
            for i in range(col_max, col_min - 1, -1):
                result.append(matrix[row_max][i])
            row_max -= 1

        # left
        if col_min <= col_max:
            for i in range(row_max, row_min - 1, -1):
                result.append(matrix[i][col_min])
            col_min += 1
            
    return result
    
def main():
    matrix = [[1,2],[3,4]]
    print(sprial_matrix(matrix))

if __name__ == "__main__":
    main()