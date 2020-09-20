play_board = {
	'top-L':' ','top-M':' ','top-R':' ',
	'mid-L':' ','mid-M':' ','mid-R':' ',
	'low-L':' ','low-M':' ','low-R':' '
}#structure of the board created

#now print as a boad using print_board
def print_board(board):
	print board['top-L'] + '|' + board['top-M'] + '|' + board['top-R']
	print '_'+'+'+'_'+'+'+'_'
	print board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R']
	print '_'+'+'+'_'+'+'+'_'
	print board['low-L'] + '|' + board['low-M'] + '|' + board['low-R']
print_board(play_board)

def print_keywords():
	print 'top-L\ttop-M\ttop-R'
	print 'mid-L\tmid-M\tmid-R'
	print 'low-L\tlow-M\tlow-R'

#now we make the game engine function !

def play_game():
	print "Let's start the game.Press ENTER to start or 'K' to see the keywords!"
	start = raw_input('>')
	if 'K' in start :
		print_keywords()
		play_game()
	else:
		turn = 'X'
		for i in range(9):
			print_board(play_board)
			move = raw_input('Your are now player %r.Type your move!\n>'%turn)
			play_board[move] = turn
			if turn == 'X':
				turn = 'O'
			else:
				turn = 'X'
play_game()