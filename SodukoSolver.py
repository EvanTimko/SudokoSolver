# main function
def solver(duko):
    # determines if the puzzle is already solved
    find = findZero(duko)
    if find:
        row, col = find# here we are setting the row and col, since find is i, j
    else: #happens when there is no more zero in the board
        return True
    # a loop which never ends, recursion
    for i in range(1, 10):
        if check(duko, i, (row, col)): # we check to see if the the i varaible has the same value in the row or column
            duko[row][col] = i

            if solver(duko): #calling itself recursively until it solves the board

                return True

            duko[row][col] = 0 # we set to zero because we do not want to place an incorrect number by acident

    return False#return false to the previous recursion to tell it to try another value

# checks for any of the same number in the row or column
def check(duko, num, pos):
    # check row
    for i in range(len(duko)):
        if duko[pos[0]][i] == num and pos[1] != i:
            return False
    # check column
    for i in range(len(duko)):
        if duko[i][pos[1]] == num and pos[0] != i:
            return False
    # check the box
    boxX = pos[1] // 3
    boxY = pos[0] // 3

    for i in range(boxY * 3, boxY * 3 + 3):
        for j in range(boxX * 3, boxX * 3 + 3):
            if duko[i][j] == num and (i, j) != pos:
                return False
    return True

# locate the first zero and then find the next and the next until none remain
def findZero(duko):
    for i in range(len(duko)):  # row search
        for j in range(len(duko[0])):  # col search
            if duko[i][j] == 0:
                return i, j  # row, col
    return None # if no more zeros exist 

# easier way to view the output
def printnice(duko):
    # loop is used for easier clariety what is the final output
    for i in range(len(duko)):
        #prints when on a row wich 3 gos into evenly
        if i % 3 == 0 and i != 0:
            print("------+-------+-------")
        for j in range(len(duko[0])):
            #prints when on a column which 3 gos into evenly
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            #prints when on a column wich 3 gos into evenly
            if j == 8:
                print(duko[i][j], end="\n")
            #prints when other condition are not met
            else:
                print(str(duko[i][j])+" ", end="")

#this is the board
#0 is empty spaces
#if you want to try it out just replace the numbers 
#with what you want to try
board = [[0, 3, 8, 0, 7, 9, 0, 0, 0],
         [0, 7, 4, 0, 8, 0, 6, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 5, 0],
         [2, 0, 9, 0, 0, 0, 0, 0, 0],
         [0, 6, 0, 0, 0, 0, 0, 3, 0],
         [0, 0, 7, 0, 9, 6, 0, 0, 5],
         [0, 0, 0, 4, 1, 0, 0, 2, 0],
         [0, 0, 0, 7, 0, 0, 0, 1, 0],
         [4, 0, 0, 0, 0, 0, 7, 0, 0]]

#call starts the program
solver(board)
#call prints out the board in a similair way as a soduko book
printnice(board)

