__author__ = 'prem aseem jain'

from random import randint
from flask import Flask,jsonify,request,make_response
app = Flask(__name__)



# Author : Aseem Jain
board = [ [None,None,None],[None,None,None],[None,None,None]]
player = 1


@app.route("/getboard")
def printBoard() :
    return jsonify({"board":board})


@app.route("/input",methods=["POST"])
def inputBoard() :
    input = request.json
    row = input["row"]
    col = input["col"]
    if row > 2 or col > 2 :
        return jsonify({"message":"invalid input","accept":False})
    if board[row][col] <> None :
        return jsonify({"message":"already occupied","accept":False})
    board[row][col] = "X"
    return jsonify({"message":input,"accept":True})


def inputBoard1(sign,row,column) :
    if row > 2 or column > 2 :
        print " invalid input try again "
        return False
    if board[row][column] <> None :
        print " Cell is already occupied"
        return False
    board[row][column] = sign
    return True

def validateRow():
    for row in board :
        if row[0] <> None :
            if row[0] == row[1] and row[0] == row[2] :
                print "Game Over Row victory" , row
                return True
    return False


def validateDiagonal() :
    if board[0][0] <> None :
        if board[0][0] == board[1][1] and board[0][0] == board[2][2] :
                print "Game Over Diagonal Victory"
                return True
    if board[0][2] <> None :
        if board[0][2] == board[1][1] and board[0][2] == board[2][0] :
                print "Game Over Diagonal Victory"
                return True
    return False

def validateColumn(num) :
    if board[0][num] <> None :
            if board[0][num] == board[1][num] and board[0][num] == board[2][num] :
                print "Game Over Column victory"
                return True
    return False

@app.route("/result")
def validateBoard():
    if validateRow() or validateDiagonal() or validateColumn(0) or validateColumn(1) or validateColumn(2) or valiateDraw() :
        print "Thanks for playing "
        return jsonify({"result":True})

    return jsonify({"result":False})

def valiateDraw() :
    for x in range(0,3):
        for y in range(0,3):
            if board[x][y] == None :
                # print "Game is a Tie ;-) "
                return False
    print "Game is a Tie ;-) "
    return True

print "welcome to Tic Tack game ... "

def takeInput(ply):

    if ply == 1 : s = 'X'
    else : s = '0'
    print "player {} with sign {} take your turn and select coordinate".format(ply,s)
    r = int(raw_input("Enter Row ... "))
    c = int(raw_input("Enter Column ... "))

    return inputBoard(s,r,c)


# counter = 1
# while not validateBoard() :
#
#     if counter % 2 == 0 :
#         ply = 2
#     else :
#         ply = 1
#
#     if takeInput(ply) :
#         counter = counter + 1
#     printBoard()


if __name__ == "__main__":
    app.run()





