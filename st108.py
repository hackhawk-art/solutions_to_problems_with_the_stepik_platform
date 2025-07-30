import random

class Game:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        total = self.mines
        while total > 0:
            for i in range(len(board)):
                ind = random.randrange(0, self.cols-1)
                if board[i][ind] != 1:
                    board[i][ind] == 1
                    total -= 1
        self.board = board
            
        
    #def distributor(self):
    #    total = self.mines
    #    while total > 0:
    #        for i in self.board:
    #            ind = random.randrange(0, len(i)-1)
    #            if self.board[i][ind] != 1:
    #                self.board[i][ind] == 1
    #                total -= 1 
     #   return self.board
                
        
game = Game(14, 18, 40)
print(game.rows)
print(game.cols)
print(game.board)
        