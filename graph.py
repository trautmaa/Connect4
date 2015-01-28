from graphics import *
from connect4 import *

#colors:
background = 'black'
boardColor = 'white'
userPieceColor = 'blue'
computerPieceColor = 'red'


def main():
	window = GraphWin("Connect 4",900, 650)
	window.setCoords(-10.0, -7.0, 80.0, 80.0)
	window.setBackground(background)

#draw board
	for i in range(8):#draw verts
		p1 = Point(0 + (10 * i),0)
		p2 = Point(1 + (10 * i),60)
		vert1 = Rectangle(p1, p2)
		vert1.setFill(boardColor)
		vert1.draw(window)
	for i in range(7):#draw horizontals
		p1 = Point(0,0 + (10 * i))
		p2 = Point(71,1 + (10 * i))
		hor1 = Rectangle(p1, p2)
		hor1.setFill(boardColor)
		hor1.draw(window)

#create reference points indicating boundaries of squares
	vert1, vert2, vert3, vert4, vert5, vert6, vert7, vert8 = 1, 11, 21, 31, 41, 51, 61, 71

#list of graphics:
	graphList = []

#supports
	p1, p2, p3, p4 = Point(0,0), Point(0,-5), Point(2,-4), Point(1,0)
	support1 = Polygon(p1, p2, p3, p4)
	graphList.append(support1)

	p1, p2, p3, p4 = Point(71,0), Point(71,-5), Point(69,-4), Point(70,0)
	support2 = Polygon(p1, p2, p3, p4)
	graphList.append(support2)

#title
	p1 = Point(35,70)
	title = Text(p1, 'Connect 4')
	title.setFace('arial')
	title.setSize(30)
	title.setFill('yellow')
	title.draw(window)

#quit button:
	qbuttonp1, qbuttonp2 = Point(-5,66), Point(5,74)
	qbutton = Rectangle(qbuttonp1, qbuttonp2)
	qbuttoncenter = Point((qbuttonp1.getX() + qbuttonp2.getX()) / 2, (qbuttonp1.getY() + qbuttonp2.getY()) / 2)
	qbutton.setFill('red')
	qbutton.draw(window)

	qbuttontext = Text(qbuttoncenter, 'Quit')
	qbuttontext.setFace('arial')
	qbuttontext.setSize(25)
	qbuttontext.draw(window)

#user Wins!
	userwinstext = Text(Point(70,70), 'User Wins!')
	userwinstext.setFace('arial')
	userwinstext.setSize(25)
	userwinstext.setFill('blue')

#computer Wins!
	compwinstext = Text(Point(70,70), 'Computer Wins!')
	compwinstext.setFace('arial')
	compwinstext.setSize(25)
	compwinstext.setFill('red')

#userColor
	p1 = Point(17,70)
	useris = Text(p1, 'User is:')
	useris.setFace('arial')
	useris.setSize(20)
	graphList.append(useris)

#userColor cirlce
	userCirc = Circle(Point(23,70),2)
	userCirc.setFill('blue')
	userCirc.draw(window)

#compColor
	p1 = Point(52,70)
	useris = Text(p1, 'Comp is:')
	useris.setFace('arial')
	useris.setSize(20)
	graphList.append(useris)

#compColor cirlce
	compCirc = Circle(Point(58,70),2)
	compCirc.setFill('red')
	compCirc.draw(window)

#draw graphList
	for item in graphList:
		item.setFill(boardColor)
		item.draw(window)


#----------------------------------------------------gameplay starts
	board = boardObject()
	pieceList = []
	while True:
		p = window.getMouse()
		if (qbuttonp1.getX() <= p.getX() <= qbuttonp2.getX()) and (qbuttonp1.getY() <= p.getY() <= qbuttonp2.getY()):
			break
		elif vert1 <= p.getX() <= vert2:
			column = 1
		elif vert2 <= p.getX() <= vert3:
			column = 2
		elif vert3 <= p.getX() <= vert4:
			column = 3
		elif vert4 <= p.getX() <= vert5:
			column = 4
		elif vert5 <= p.getX() <= vert6:
			column = 5
		elif vert6 <= p.getX() <= vert7:
			column = 6
		elif vert7 <= p.getX() <= vert8:
			column = 7
		destinationPoint = Point((column * 10 - 5), (board.getTallestOpen(column)) * 10 - 5)
		board.makeUserMove(column)
		piece1 = Circle(destinationPoint, 4)
		piece1.setFill(userPieceColor)
		piece1.draw(window)
		if board.gameOver():
			userwinstext.draw(window)
			connection = Line(pointLocation(board.whichFour()[0]), pointLocation(board.whichFour()[3]))
			connection.setFill('yellow')
			connection.draw(window)
			window.getMouse()
			break		
		column = board.makeCompMove()
		if board.getTallestOpen(column) != False:
			destinationPoint = Point((column * 10 - 5), (board.getTallestOpen(column) - 1) * 10 - 5)
		else:
			destinationPoint = Point((column * 10 - 5), (6) * 10 - 5)
		piece2 = Circle(destinationPoint, 4)
		piece2.setFill(computerPieceColor)
		piece2.draw(window)
		if board.gameOver():
			compwinstext.draw(window)
			connection = Line(pointLocation(board.whichFour()[0]), pointLocation(board.whichFour()[3]))
			connection.setFill('yellow')
			connection.draw(window)
			window.getMouse()
			break

#create pieces
class piece:
	def __init__(self):
		self.type = Circle
		self.centerPoint = Point(0,0)
		self.color = 'black'
	def initialize(self, center, playerChoice):
		self.centerPoint = center
		if playerChoice == 'user':
			self.color = userPieceColor
		else:
			self.color = computerPieceColor
		return 


if __name__ == '__main__':
	main()