import copy
import numpy as np

sample = ['005080302',
          '420000500',
          '600004000',
          '000300900',
          '300026000',
          '000000070',
          '000070680',
          '098000004',
          '000500000']
f = lambda x : list(map(int, x))
sample = np.array(list(map(f, sample)))

def checkRow(sudoku, x, y, i):
    return not (i in sudoku[y])

def checkColumn(sudoku, x, y, i):
    column = sudoku[:,x]
    return not (i in column)

def checkSquare(sudoku, x, y, i):
    X = (x//3) *3
    Y = (y//3) *3
    square = sudoku[Y:(Y+3), X:(X+3)]
    return not (i in square)

def check(sudoku, x, y, i):
    return checkRow(sudoku, x, y,i) and checkColumn(sudoku, x, y,i) and checkSquare(sudoku, x, y,i)

def printSudoku(sudoku):
    print('-'*25)
    c = 0
    cc = 0
    for i in sudoku:
        print('|', end=' ')
        for j in i:
            print(j, end = ' ')
            c += 1
            if c % 3 == 0 and c % 9 != 0:
                print('| ', end = '')
        cc += 1
        print('|', end = '')
        if cc % 3 == 0:
            print('')
            print('-' * 25, end = '')
        print(' ', end = '\n')
        
def checkLast(sudoku, i):
    return check(sudoku, 8, 8, i)
        
def solve(sudoku, i):
    sudoku = copy.deepcopy(sudoku)
    if i == 81:
        printSudoku(sudoku)
    else:
        y = i // 9
        x = i % 9
        if sudoku[y][x] != 0:
            solve(sudoku, i+1)
        else:
            l = [1,2,3,4,5,6,7,8,9]
            for j in l:
                if check(sudoku, x,y,j):
                    sudoku[y][x] = j
                    solve(sudoku, i+1)

solve(sample, 0)
