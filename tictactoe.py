import random

class Player():
	
	def __init__(self,name,symbol,dimension):

		self.pid = random.randint(1,100000)
		self.name = name
		self.wins = 0
		self.loss = 0
		self.drawn = 0
		self.symbol = symbol;
		self.row_sum = [0]*dimension
		self.col_sum = [0]*dimension
		self.diag_sum = 0
		self.reverse_diag_sum = 0

	def get_player_id(self):
		return self.pid

	def get_player_name(self):
		return self.name

	def get_player_stats(self):
		print("Id : ",self.pid)
		print("Name : ",self.name)
		print("Wins : ",self.wins)
		print("Loss : ",self.loss)
		print("Drawn : ",self.drawn)
		print("Wining %: ",self.wins/(self.wins+self.loss+self.drawn))

class Board():
	
	def __init__(self,dimension):
		
		self.board = []
		self.board_dimension = dimension
		self.winner = None

	def initialize_board(self):

		for i in range(self.board_dimension):
			temp = []
			for j in range(self.board_dimension):
				temp.append(0)
			self.board.append(temp)

	def make_move(self,player_obj,row,col):
		
		if row>=self.board_dimension or col>=self.board_dimension or row<0 or col<0 or self.board[row][col] != 0:
			print("Invalid Move")
			return False
		else:
			
			self.board[row][col] = player_obj.symbol

			player_obj.row_sum[row] += abs(player_obj.symbol)
			player_obj.col_sum[col] += abs(player_obj.symbol)	

			if row == col:
				player_obj.diag_sum += abs(player_obj.symbol)

			if col == self.board_dimension - row - 1:
				player_obj.reverse_diag_sum += abs(player_obj.symbol)

			if player_obj.row_sum[row] == self.board_dimension or player_obj.col_sum[col] == self.board_dimension:
				self.winner = player_obj

			if player_obj.diag_sum == self.board_dimension or player_obj.reverse_diag_sum == self.board_dimension:
				self.winner = player_obj
			return True

	def get_winner(self):
		return self.winner

	def paint_board(self):

		for i in range(self.board_dimension):
			for j in range(self.board_dimension):
				s = " "
				if self.board[i][j] == 1:
					s = "O"
				elif self.board[i][j] == -1:
					s = "X"
				print("|",s,"|",end="")
			print()
			# print("-"*self.board_dimension**2)
			# print()


class Game():
	
	def __init__(self,player1_name,player2_name,dimension):
		
		self.player1 = Player(player1_name,1,dimension)
		self.player2 = Player(player2_name,-1,dimension)
		self.board = Board(dimension)

	def play(self,start_player):

		self.board.initialize_board()
		winner_obj = None
		num_moves = 0
		curr_chance = start_player
		status = True

		while winner_obj is None and num_moves < self.board.board_dimension**2:
			# print(curr_chance)
			self.board.paint_board()

			row = int(input("Enter row:"))
			col = int(input("Enter col:"))
			
			if curr_chance == 1:
				status = self.board.make_move(self.player1,row,col)
				if status == True:
					num_moves += 1
					curr_chance = 2
				else:
					curr_chance = 1	

			if curr_chance == 2:
				status = self.board.make_move(self.player2,row,col)
				if status == True:
					num_moves += 1
					curr_chance = 1
				else:
					curr_chance = 2

			winner_obj = self.board.get_winner()

		self.board.paint_board()	

		print("Result ",self.player1.name, " vs ", self.player2.name)
		
		if 	winner_obj is None:
			self.player1.drawn += 1
			self.player2.drawn += 1
			print("Match drawn")
			print()
			self.player1.get_player_stats()
			print()
			self.player2.get_player_stats()
			print()

		else:
			if winner_obj.pid == self.player1.pid:
				self.player1.wins += 1
				self.player2.loss += 1
			else:
				self.player2.wins += 1
				self.player1.loss += 1

			print("Winner: ",winner_obj.name)
			print()
			self.player1.get_player_stats()
			print()
			self.player2.get_player_stats()
			print()

	
def main():

	player1_name = input("Enter player1 name: ")
	player2_name = input("Enter player2 name: ")
	dimension = int(input("Enter board dimension: "))
	
	game = Game(player1_name,player2_name,dimension)

	first_player = int(input("Enter 1 to start with player1 or 2 to start with player2"))

	game.play(first_player)


if __name__ == '__main__':
    main()

