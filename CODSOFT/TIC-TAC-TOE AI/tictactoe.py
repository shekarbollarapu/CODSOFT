
import random


def gameBoard(board):
    for row in board:
        print("|".join(row))
        
def boardFull(board):
    if board is None:
        return False
    return not any(' ' in row for row in board)

def winningPlayer(board, player):
    win_states = (
        (0,1,2),(3,4,5),(6,7,8),#Horizontal_positions
        (0,3,6),(1,4,7),(2,5,8),#Vertical_positions
        (0,4,8),(2,4,6)#diagonal_positions
    )

    for state in win_states:
        if all(board[i] == player for i in state):
            return True
    return False
    
def getScore(board):
    if winningPlayer(board , "X"):
        return 1
    elif winningPlayer(board , "O"):
        return -1
    else:
        return 0

def alphaBeta(board, depth, alpha, beta, is_maximizing):
    if winningPlayer(board, "X"):
        return (1, None)
    elif winningPlayer(board, "O"):
        return (-1, None)
    elif boardFull(board):
        return (0,None)
    if is_maximizing:
        best_score = -1000
        best_move = None
        for i in range(9):
            if board[i] == " ":
                board[i]="X"
                score,_ = alphaBeta(board, depth -1, alpha, beta, False)
                board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        if best_move is None:
            return (best_score, -1)
        else:
            return (best_score, best_move)
    else:
        best_score = 1000
        best_move = None
        for i in range(9):
            if board[i] == " ":
                board[i]="O"
                score,_ = alphaBeta(board, depth -1, alpha, beta, True)
                board[i] = " "
                if score < best_score:
                    best_score = score
                    best_move = i
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        if best_move is None:
            return (best_score, -1)
        else:
            return (best_score, best_move)

def computerMove(board):
    _, best_move = alphaBeta(board, 9, -1000, 1000, True)
    if best_move is not None:
        board[best_move] = "X"
    return board

def playerMove(board):
    while True:
        move = int(input("Enter a move (0-8): "))
        if board[move] == " ":
            board[move] = "O"
            break
        else:
            print("Invalid move! Try again...")
    return board

def play():
    board = [' ']*9
    print("Have great Fun!!")
    print("Layout of the game")
    print("You are playing as 'O' whereas AI will be 'X' ")

    while True:
        gameBoard([board[i:i+3] for i in range(0,9,3)])
        board = playerMove(board)
        if winningPlayer(board, "O"):
            gameBoard([board[i:i+3] for i in range(0,9,3)])
            print("Congrats!! You won!")
            break
        elif boardFull(board):
            gameBoard([board[i:i+3] for i in range(0,9,3)])
            print("Its's Tie...")
            break
        
        board = computerMove(board)
        
        if winningPlayer(board, "X"):
            gameBoard([board[i:i+3] for i in range(0,9,3)])
            print("Sorry... You Lost..")
            break
        elif boardFull(board):
            gameBoard([board[i:i+3] for i in range(0,9,3)])
            print("Its's Tie...")
            break

play()
        
        


