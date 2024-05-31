
#Shahar Shitrit 316528900
#kelly Deitch 207081241

import turtle

def main():

    changeCursorToPen()
    turtle.speed(0)
    drawBoard()

    i = 0

    matrix =[['0','0','0'],['0','0','0'],['0','0','0']]
    flag = True

    while(i < 9 and flag == True):
        if flag == True:
            rowX, colX = getRowCol('X')
            xTurn(rowX, colX)
            matrix[rowX - 1][colX - 1] = 'X'
            flag = statCheck(matrix, 'X')
            if flag == False:
                print("X winner")

        i = i + 1
        if i == 9:
            print("It is a tie! Nobody win!")

        if flag == True:
           rowO, colO = getRowCol('O')
           circleTurn(rowO, colO)
           matrix[rowO - 1][colO - 1] = 'O'
           flag = statCheck(matrix, 'O')
           if flag == False:
               print("O winner")

        i = i + 1
        if i == 9:
            print("It is a tie! Nobody win!")


    turtle.done()


def drawLine(start_x,end_x, start_y,end_y): #Draw line with coordinates
    turtle.penup()
    turtle.goto(start_x,start_y)
    turtle.pendown()
    turtle.goto(end_x, end_y)

def drawWinLine(i,j,direction):

    turtle.pensize(10)
    turtle.pencolor('purple')

    if direction == 'H':#Horizontal
        if i == 0:
            drawLine(-225,225,150,150)
        if i == 1:
            drawLine(-225,225,0,0)
        if i == 2:
            drawLine(-225,225,-150,-150)

    if direction == 'V':#Vertical
        if j == 0:
            drawLine(-150, -150, 225, -225)
        if j == 1:
            drawLine(0, 0, 225, -225)
        if j == 2:
            drawLine(150, 150, 225, -225)

    if direction == 'DL':#Diagonal from top left board
        drawLine(-225, 225, 225, -225)

    if direction == 'DR':#Diagonal from top right board
        drawLine(225,-225,225,-225)

def move(x,y):# Move turtle without drawing line

    turtle.penup()
    turtle.goto(x,y)

def drawBoard(): # Draw the TIC-TAC-TOE game board.

    turtle.pensize(5)

    drawLine(-225, 225, -75, -75)
    move(225, 75)
    drawLine(225, -225, 75, 75)
    move(-75, 225)
    drawLine(-75, -75, 225, -225)
    move(75, -225)
    drawLine(75, 75, -225, 225)

def changeCursorToPen(): #Change the turtule cursor to look like a pen , to give a feeling that this is a real game.

    shape = ((0, 0), (6, 10), (25, 30), (30, 25), (10, 6))# the coordinates of each corner
    turtle.register_shape('pen', shape) # registering the new shap
    turtle.shape('pen')# changing the shape to 'pen'

def drawX(x, y):# Draw X sign

    #Draw side one
    move(x + 20 , y -20)
    turtle.pendown()
    turtle.setheading(-45)
    turtle.forward(155)

    #Draw side two
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(110)
    turtle.setheading(225)
    turtle.pendown()
    turtle.forward(155)

def xTurn(row,col):# Recognize in which cell we will draw the X

    turtle.pensize(5)
    turtle.pencolor('blue')

    if row == 1:
        if col == 1:
            drawX(-225, 225)
        if col == 2:
            drawX(-75, 225)
        if col == 3:
            drawX(75, 225)

    if row == 2:
        if col == 1:
            drawX(-225, 75)
        if col == 2:
            drawX(-75, 75)
        if col == 3:
            drawX(75, 75)

    if row == 3:
        if col == 1:
            drawX(-225, -75)
        if col == 2:
            drawX(-75, -75)
        if col == 3:
            drawX(75, -75)

def drawCircle(x,y): # draw a circle in a specific coordination

    turtle.penup()
    turtle.goto(x+75,y-130)
    turtle.setheading(365)
    turtle.pendown()
    turtle.circle(55)

def circleTurn(row, col): # Recognize in which cell we will draw the circle

    turtle.pensize(5)
    turtle.pencolor('red')

    if row == 1:
        if col == 1:
            drawCircle(-225, 225)
        if col == 2:
            drawCircle(-75, 225)
        if col == 3:
            drawCircle(75, 225)

    if row == 2:
        if col == 1:
            drawCircle(-225, 75)
        if col == 2:
            drawCircle(-75, 75)
        if col == 3:
            drawCircle(75, 75)

    if row == 3:
        if col == 1:
            drawCircle(-225, -75)
        if col == 2:
            drawCircle(-75, -75)
        if col == 3:
            drawCircle(75, -75)

def getRowCol(shape): # Ask from user in which row & col to put the shape.

    row = int(input(shape + ' turn Enter the row: '))
    col = int(input(shape + ' turn Enter the col: '))

    return row , col

def statCheck(matrix , shape): #check if some of the players win the game

    #check the horizontal and verticl shape location
    for i in range(len(matrix)):
        countHorizontal = 0
        countVertical = 0
        for j in range(len(matrix[i])):
            if(matrix[i][j] == shape):
                countHorizontal = countHorizontal + 1
                if countHorizontal == 3:
                    drawWinLine(i,j,'H')
                    return False
            if(matrix[j][i] == shape):
                countVertical = countVertical + 1
                if countVertical == 3:
                    drawWinLine(j, i, 'V')
                    return False

    countDiagonalL = 0
    countDiagonalR = 0
    j = 2
    # check the horizontal and verticl shape location
    for i in range(len(matrix)):
        if(matrix[i][i] == shape):
            countDiagonalL = countDiagonalL + 1
            if countDiagonalL == 3:
                drawWinLine(i,j,'DL')
                return False
        if(matrix[i][j] == shape):
            countDiagonalR = countDiagonalR + 1
            j = j - 1
            if countDiagonalR == 3:
                drawWinLine(i, i, 'DR')
                return False







    return True


main()

