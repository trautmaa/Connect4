#connect4
#by Alex Trautman
#Final project for CS 111-03

import random
import sys
from graphics import *

#definitions:

firstColumn = [0,1,8,15,22,29,36]
secondColumn = [0,2,9,16,23,30,37]
thirdColumn = [0,3,10,17,24,31,38]
fourthColumn = [0,4,11,18,25,32,39]
fifthColumn = [0,5,12,19,26,33,40]
sixthColumn = [0,6,13,20,27,34,41]
seventhColumn = [0,7,14,21,28,35,42]
listOfColumns = [0,firstColumn,secondColumn,thirdColumn,fourthColumn,fifthColumn,sixthColumn,seventhColumn]
rowList = [6,5,4,3,2,1]
#board = ['O'] * 43

class boardObject:
	def __init__(self):
		self.board = ['O'] * 43
		self.turn = 'user'
		self.userColor = 'y'
		self.computerColor = 'x'
		self.winner = 'none'

    #addPiece takes board, playerColor, column and returns a new board with a piece of pc added in the top place in the column specified
	#returns False if there is no more room left in the row
	def addPiece(self, pc, column):
		if legalMove(self.board, column):
			for i in rowList:
				if self.board[listOfColumns[column][i]] == 'O':
					self.board[listOfColumns[column][i]] = pc
					return
		else:
			return False

	#getTallestOpen tells what height is the tallest open slot of a given column
	def getTallestOpen(self, column):
		if legalMove(self.board, column):
			for i in rowList:
				if self.board[listOfColumns[column][i]] == 'O':
					return 7 - i
		else:
			return False

	def gameOver(self):
		if fourInARow(self.board, self.computerColor):
			self.winner = 'Computer Wins!'
			return True
		if fourInARow(self.board, self.userColor):
			self.winner = 'User Wins!'
			return True

	def shareWinner(self):
		return self.winner

	def switchTurns(self):
		if self.turn == 'user':
			self.turn = 'computer'
		else:
			self.turn = 'user'

	def drawBoard(self):
		b = self.board
		print b[1] + " | " + b[2] + " | " + b[3] + " | " + b[4] + " | " + b[5] + " | " + b[6] + " | " + b[7]
		print b[8] + " | " + b[9] + " | " + b[10] + " | " + b[11] + " | " + b[12] + " | " + b[13] + " | " + b[14]
		print b[15] + " | " + b[16] + " | " + b[17] + " | " + b[18] + " | " + b[19] + " | " + b[20] + " | " + b[21]
		print b[22] + " | " + b[23] + " | " + b[24] + " | " + b[25] + " | " + b[26] + " | " + b[27] + " | " + b[28]
		print b[29] + " | " + b[30] + " | " + b[31] + " | " + b[32] + " | " + b[33] + " | " + b[34] + " | " + b[35]
		print b[36] + " | " + b[37] + " | " + b[38] + " | " + b[39] + " | " + b[40] + " | " + b[41] + " | " + b[42]
		print '--------------------------'

	def makeUserMove(self, column):
		'''self.drawBoard()
		column = raw_input('Enter a column to play (1-7). q to quit')'''
		if column == 'q':
			sys.exit()
		'''column = int(column)'''
		if column in [1,2,3,4,5,6,7]:
			self.addPiece(self.userColor, column)
		else:
			sys.exit()

	def makeCompMove(self):
		column = self.compColumnChoice()
		self.addPiece(self.computerColor, self.compColumnChoice())
		return column

	def whichFour(self):
		board = self.board
		for j in [1,2,3,4]:
			for i in [1,2,3,4,5,6]:
				if (board[listOfColumns[j][i]] == board[listOfColumns[j + 1][i]]\
				== board[listOfColumns[j + 2][i]] == board[listOfColumns[j + 3][i]] != 'O'):
					num = listOfColumns[j][i]
					indexList = [num, num + 1, num + 2, num + 3]
					return indexList
		for j in [1,2,3,4,5,6,7]:
			for i in [1,2,3]:
				if (board[listOfColumns[j][i]] == board[listOfColumns[j][i + 1]]\
				== board[listOfColumns[j][i + 2]] == board[listOfColumns[j][i + 3]] != 'O'):
					num = listOfColumns[j][i]
					indexList = [num, num + 7, num + 14, num + 21]
					return indexList
		for j in [1,2,3,4]:
			for i in [1,2,3]:
				if (board[listOfColumns[j][i]] == board[listOfColumns[j + 1][i + 1]]\
				== board[listOfColumns[j + 2][i + 2]] == board[listOfColumns[j + 3][i + 3]] != 'O'):
					num = listOfColumns[j][i]
					indexList = [num, num + 8, num + 16, num + 24]
					return indexList
			for i in [1,2,3]:
				if (board[listOfColumns[j + 3][i]] == board[listOfColumns[j + 2][i + 1]]\
				== board[listOfColumns[j + 1][i + 2]] == board[listOfColumns[j][i + 3]] != 'O'):
					num = listOfColumns[j][i]
					indexList = [num, num + 6, num + 12, num + 18]
					return indexList

#this is the AI:
#it returns the column that the computer will play
	def compColumnChoice(self):
		while True:
			for column in [1,2,3,4,5,6,7]: #looks to win the game
				board1 = copyBoard(self.board)
				if legalMove(board1, column):
					addPiece(board1, self.computerColor, column)
					if fourInARow(board1, self.computerColor):
						return column
			for column in [1,2,3,4,5,6,7]: #looks to block user's win
				board1 = copyBoard(self.board)
				if legalMove(board1, column):
					addPiece(board1, self.userColor, column)
					if fourInARow(board1, self.userColor):
						return column						
			for column in [1,2,3,4,5,6,7]: # looks to make three in a row
				board1 = copyBoard(self.board)
				if legalMove(board1, column):
					addPiece(board1, self.computerColor, column)
					if threeInARow(board1, self.computerColor):
						return column
			for column in [1,2,3,4,5,6,7]: # looks to make two in a row
				board1 = copyBoard(self.board)
				if legalMove(board1, column):
					addPiece(board1, self.computerColor, column)
					if twoInARow(board1, self.computerColor):
						return column
			for column in [1,2,3,4,5,6,7]: # looks to block user's three in a row
				board1 = copyBoard(self.board)
				if legalMove(board1, column):
					addPiece(board1, self.userColor, column)
					if threeInARow(board1, self.userColor):
						return column
			for column in [1,2,3,4,5,6,7]: # looks to block user's two in a row
				board1 = copyBoard(self.board)
				if legalMove(board1, column):
					addPiece(board1, self.userColor, column)
					if twoInARow(board1, self.userColor):
						return column
			random = random.choice([1,2,3,4,5,6,7]) # if nothing else works, makes a random move
			while True:
				board1 = copyBoard(self.board)
				if legalMove(board1, column):
					return column

#getPlayerMove prompts player for a move. it uses legalMove to check if the column is full yet
def getPlayerMove(board, playerColor):
	drawBoard(board)
	column = input('Choose a column (1-7)')
	while True:
		if legalMove(board, column):
			for i in rowList:
				if board[listOfColumns[column][i]] == 'O': #this for loop checks each postion
				#from the bottom up to see if the spot is empty. if True, it fills the spot with pc
					board[listOfColumns[column][i]] = playerColor
					return board
		else:
			column = input('Choose a column (1-7)')

#legalMove makes sure the top position in the column doesn't have a piece in it yet
def legalMove(board, column):
	if board[column] == 'O':
		return True
	else:
		return False

#addPiece takes board, playerColor, column and returns a new board with a piece of pc added in the top place in the column specified
#returns False if there is no more room left in the row
def addPiece(board, pc, column):
	if legalMove(board, column):
		for i in rowList:
			if board[listOfColumns[column][i]] == 'O':
				board[listOfColumns[column][i]] = pc
				return
	else:
		return False

def copyBoard(board):
	return board[:]

#this function puts a piece of playerColor to the topmost empty slot in given column
#and returns the new board
#def dropInColumn(board, column, playerColor):


#fourInARow checks if the given player has won the given board. b refers to board,
#pc refers to playerColor
def fourInARow(b, pc):
	return checkHorizontals(b, pc) or checkVerticals(b, pc) or checkDiagonals(b, pc)

def threeInARow(b, pc):
	return checkHorizontalsFor3(b, pc) or checkVerticalsFor3(b, pc) or checkDiagonalsFor3(b, pc)

def twoInARow(b, pc):
	return checkHorizontalsFor2(b, pc) or checkVerticalsFor2(b, pc) or checkDiagonalsFor2(b, pc)

#checkHorizontals, checkVerticals, checkDiagonals check if playerColor (pc) has a win 
#in any of the possible slots in the 6x7 board
def checkHorizontals(board, pc):
	for j in [1,2,3,4]:
		for i in [1,2,3,4,5,6]:
			if (board[listOfColumns[j][i]] == pc and
			board[listOfColumns[j + 1][i]] == pc and
			board[listOfColumns[j + 2][i]] == pc and
			board[listOfColumns[j + 3][i]] == pc):
				return True

def checkVerticals(board, pc):
	for j in [1,2,3,4,5,6,7]:
		for i in [1,2,3]:
			if (board[listOfColumns[j][i]] == pc and
			board[listOfColumns[j][i + 1]] == pc and
			board[listOfColumns[j][i + 2]] == pc and
			board[listOfColumns[j][i + 3]] == pc):
				return True

def checkDiagonals(board, pc):
	for j in [1,2,3,4]:
		for i in [1,2,3]:
			if (board[listOfColumns[j][i]] == pc and
			board[listOfColumns[j + 1][i + 1]] == pc and
			board[listOfColumns[j + 2][i + 2]] == pc and
			board[listOfColumns[j + 3][i + 3]] == pc):
				return True
		for i in [1,2,3]:
			if (board[listOfColumns[j + 3][i]] == pc and
			board[listOfColumns[j + 2][i + 1]] == pc and
			board[listOfColumns[j + 1][i + 2]] == pc and
			board[listOfColumns[j][i + 3]] == pc):
				return True

def checkHorizontalsFor3(board, pc):
	for j in [1,2,3,4,5]:
		for i in [1,2,3,4,5,6]:
			if (board[listOfColumns[j][i]] == pc and
			board[listOfColumns[j + 1][i]] == pc and
			board[listOfColumns[j + 2][i]] == pc):
				return True

def checkVerticalsFor3(board, pc):
	for j in [1,2,3,4,5,6,7]:
		for i in [1,2,3,4]:
			if (board[listOfColumns[j][i]] == pc and
			board[listOfColumns[j][i + 1]] == pc and
			board[listOfColumns[j][i + 2]] == pc):
				return True

def checkDiagonalsFor3(board, pc):
	for j in [1,2,3,4,5]:
		for i in [1,2,3,4]:
			if (board[listOfColumns[j][i]] == pc and
			board[listOfColumns[j + 1][i + 1]] == pc and
			board[listOfColumns[j + 2][i + 2]] == pc):
				return True
		for i in [1,2,3,4]:
			if (board[listOfColumns[j + 2][i]] == pc and
			board[listOfColumns[j + 1][i + 1]] == pc and
			board[listOfColumns[j][i + 2]] == pc):
				return True

def checkHorizontalsFor2(board, pc):
	for j in [1,2,3,4,5,6]:
		for i in [1,2,3,4,5,6]:
			if (board[listOfColumns[j][i]] == pc and
			board[listOfColumns[j + 1][i]] == pc):
				return True

def checkVerticalsFor2(board, pc):
	for j in [1,2,3,4,5,6,7]:
		for i in [1,2,3,4,5]:
			if (board[listOfColumns[j][i]] == pc and
			board[listOfColumns[j][i + 1]] == pc):
				return True

def checkDiagonalsFor2(board, pc):
	for j in [1,2,3,4,5,6]:
		for i in [1,2,3,4,5]:
			if (board[listOfColumns[j][i]] == pc and
			board[listOfColumns[j + 1][i + 1]] == pc):
				return True
		for i in [1,2,3,4,5]:
			if (board[listOfColumns[j + 1][i]] == pc and
			board[listOfColumns[j][i + 1]] == pc):
				return True

def pointLocation(num):
	column = num % 7
	if 0 < num < 8:
		row = 6
	elif 7 < num < 15:
		row = 5
	elif 14 < num < 22:
		row = 4
	elif 21 < num < 29:
		row = 3
	elif 28 < num < 36:
		row = 2
	elif 35 < num < 43:
		row = 1
	width = column * 10 - 5
	height = row * 10 - 5
	#print width
	#print height
	return Point(width, height)

def main():
	pass

if __name__ == '__main__':
	main()
