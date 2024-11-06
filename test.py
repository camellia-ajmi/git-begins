 1. # Tic-Tac-Toe
 2.
 3. import random
 4.
 5. def drawBoard(board):
 6. # This function prints out the board that it was passed.
 7.
 8. # "board" is a list of 10 strings representing the board (ignore
 index 0).
 9. print(board[7] + '|' + board[8] + '|' + board[9])
 10. print('-+-+-')
 11. print(board[4] + '|' + board[5] + '|' + board[6])
 12. print('-+-+-')
 13. print(board[1] + '|' + board[2] + '|' + board[3])