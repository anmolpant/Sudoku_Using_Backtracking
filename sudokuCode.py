#TO PRINT SUDOKU

def printGrid(A):

    print("\nSOLUTION IS")

    for i in range(9):

        print(" ".join(str(x) for x in A[i]))

#TO FIND ALL EMPTY LOCATIONS MARKED BY '0'
def findEmptyLocation(A,l):

    for row in range(9):

        for col in range(9):

            if(A[row][col]==0):

                l[0]=row

                l[1]=col

                return True

    return False

#CHECKS WHETHER NUMBER ALREADY EXISTS IN ROW
def usedInRow(A,row,num):

    for i in range(9):

        if(A[row][i] == num):

            return True

    return False

#CHECKS WHETHER NUMBER ALREADY EXISTS IN COLUMN
def usedInCol(A,col,num):

    for i in range(9):
 
        if(A[i][col] == num):

            return True

    return False

#CHECKS WHETHER NUMBER ALREADY EXISTS IN MINIGRID
def usedInMiniGrid(A,row,col,num):

    for i in range(3):

        for j in range(3):

            if(A[i+row][j+col] == num):

                return True

    return False

#CHECKS IF A LOCATION IS SAFE

def check(A,row,col,num):

    return not usedInRow(A,row,num) and not usedInCol(A,col,num) and not usedInMiniGrid(A,row - row%3,col - col%3,num)

#MAIN SOLVING FUNCTION

def solveSudoku(A):



    l=[0,0]

    if(not findEmptyLocation(A,l)):

        return True

    row=l[0]

    col=l[1]

    for num in range(1,10):

        if(check(A,row,col,num)):

            A[row][col]=num

            if(solveSudoku(A)):

                return True

            A[row][col] = 0

    return False

sudoku = []

for i in range(9):

    temp = list(map(int,input().split()))

    sudoku.append(temp)
 
#IF SUCCESS THEN PRINT SUDOKU

if(solveSudoku(sudoku)):

    printGrid(sudoku)

else:

    print ("No solution exists")
