# Minesweeper on grid

# main function that takes a grid (nested list) input
def minesweeper(grid):
    # check that the required coordinate exists within the grid
    def check(row, column):
        if -1 < row < total_rows:
            if -1 < column < total_columns:
                return True
            else:
                return False 
        else:
            return False
    
    # if you find a mine, increase every neighbouring digit by 1.
    def minefound(row, column):
        # iterate for rows
        for x in neighbors:
            # iterate for columns
            for y in neighbors:
                # get boolean value from check function. This takes care of cases where the coordinate values are not part of the grid.
                if check(row + x, column + y): 
                    # if neighbor is not a mine, add 1
                    if grid[row + x][column + y] != "#":
                        grid[row + x][column + y] += 1
        
    # find number of total rows and columns in grid. Store values in the variables required for the check function.
    total_rows = len(grid)
    total_columns = len(grid[0]) # assuming grid is not ragged.

    # I could make this a nested list to map out every neighbouring coordinate, or I could iterate over the same list twice. Once for the x-coordinate, once for the y-coordinate. 
    neighbors = [-1, 0, 1]

    # make every blank 0 so that you can use it as a counter
    count1 = 0 
    for list in grid:
        count2 = 0  
        for letter in list:
            if letter == "-":
                grid[count1][count2] = 0
            count2 += 1
        count1 +=1

    # look for mines. 
    row = 0
    for list in grid:
        column = 0
        for letter in list:
            if letter == "#":
                minefound(row, column)
            column += 1
        row += 1

    # cast all integers as strings, as required in the task description
    count1 = 0 
    for list in grid:
        count2 = 0  
        for letter in list:
            if letter == "-":
                grid[count1][count2] = str(grid[count1][count2])
            count2 += 1
        count1 +=1

    # return result as a nested list 
    return grid

# testing
mines = [["-", "-", "#", "-", "-"],
         ["-", "-", "-", "-", "-"],
         ["-", "#", "#", "-", "-"],
         ["-", "-", "-", "-", "-"],
         ["-", "-", "#", "-", "#"]
         ]

# it works :)
print(minesweeper(mines))  