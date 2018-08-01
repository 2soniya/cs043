# Tic Tac Toe - Object Oriented Version
# Author: Soniya Gaikwad
# Date: July 30, 2018
# Description: In this program, it allows 2 players to play against each other in a game of Tic Tac Toe.
# What works: This is a fully functioning game of Tic Tac Toe.
# What doesn't work: N/A

import random


class Board:
    """
    This is the Board Class that represents the Tic Tac Toe board.
    """

    def __init__(self, board):
        self.board = board

    def drawBoard(self):
        """
        This method draws the board.
        :return:
        """

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    def makeMove(self, letter, move):
        """
        This method updates the board based on the given move.
        :param letter:
        :param move:
        :return:
        """
        self.board[move] = letter

    def isWinner(self, le):
        """
        This method returns True if the player has won, else False.
        :param le: This is the letter.
        :return:
        """
        bo = self.board
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal

    def getBoardCopy(self):
        """
        This method makes a copy of the board list.
        :return:
        """

        dupeBoard = []
        for i in self.board:
            dupeBoard.append(i)

        return Board(dupeBoard)

    def isSpaceFree(self, move):
        """
        This method checks if the space is free.
        :param move: The location where the player chooses to make their move.
        :return:
        """
        return self.board[move] == ' '

    def isBoardFull(self):
        """
        This method will return True if every space on the board has been taken, otherwise it will return False.
        :return:
        """
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True


class Player:
    """
    This is the Player Class that represents player.
    """

    def __init__(self, board):
        self.board = board

    def inputPlayerLetter(self):
        """
        This method allows the player to choose which they want to be and returns the ordered player list.
        :return: Returns a list with the player's letter as the first item, and the second player's letter as the second.
        """
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()

        # the first element in the tuple is the player 1's letter, the second is the player 2's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst(self):
        """
        This method will randomly choose who goes first.
        :return:
        """
        if random.randint(0, 1) == 0:
            return 'Player 1'
        else:
            return 'Player 2'

    def playAgain(self):
        """
        This method will ask whether the players want to play again.
        :return: Returns True if the players want to play again, otherwise returns False.
        """
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def getPlayerMove(self):
        """
        This method lets the player type in their move.
        :return:
        """
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.board.isSpaceFree(int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)


print('Welcome to Tic Tac Toe!')

while True:
    # Initializes the board and player.
    tic_tac_toe_board = Board([' '] * 10)
    player = Player(tic_tac_toe_board)

    # Gets the players' chosen letter.
    playerLetter1, playerLetter2 = player.inputPlayerLetter()
    # Chooses which player gets to go first, randomly.
    
    turn = player.whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Player 1':
            # Player 1's turn.
            tic_tac_toe_board.drawBoard()
            print('It is your turn ' + turn + ".", end=" ")
            move = player.getPlayerMove()
            tic_tac_toe_board.makeMove(playerLetter1, move)

            if tic_tac_toe_board.isWinner(playerLetter1):
                tic_tac_toe_board.drawBoard()
                print('Hooray! Player 1 has won the game!')
                gameIsPlaying = False
            else:
                if tic_tac_toe_board.isBoardFull():
                    tic_tac_toe_board.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player 2's turn.
            tic_tac_toe_board.drawBoard()
            print('It is your turn ' + turn + ".", end=" ")
            move = player.getPlayerMove()
            tic_tac_toe_board.makeMove(playerLetter2, move)

            if tic_tac_toe_board.isWinner(playerLetter2):
                tic_tac_toe_board.drawBoard()
                print('Player 2 has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if tic_tac_toe_board.isBoardFull():
                    tic_tac_toe_board.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not player.playAgain():
        break
