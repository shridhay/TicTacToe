class T:
    def __init__(self):
        self.count = 0
        board = [[None] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                board[i][j] = True
                self.dfs(board)
                board[i][j] = None
                
    def __str__(self):
        return str(self.count)
    
    def dfs(self, board, tile=False):
        if self.tie(board) or self.win(board):
            self.count += 1
            return
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = tile
                    self.dfs(board, not(tile))
                    board[i][j] = None    
        return 
          
    def win(self, board):
        for i in range(3):
            if all(tile is True for tile in board[i]) or all(tile is False for tile in board[i]):
                return True
            if all(board[j][i] is True for j in range(3)) or all(board[j][i] is False for j in range(3)):
                return True
        if all(board[i][i] is True for i in range(3)) or all(board[i][i] is False for i in range(3)):
            return True
        if all(board[i][2-i] is True for i in range(3)) or all(board[i][2-i] is False for i in range(3)):
            return True
        return False
    
    def tie(self, board):
        return all(all(board[i][j] is not None for i in range(3)) for j in range(3))

print(T())
