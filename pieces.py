import pygame

SIZE = (900, 700)
SCREEN = pygame.display.set_mode(SIZE)

cellSize = 70
class Piece:

    def __init__(self, color, piece_type, image):
        self.color = color
        self.piece_type = piece_type
        self.image = image
        self.turn = "black"

    def black_pawn_movement(self, start, end, board):
        valid_moves = [(start[0], start[1]-1), (start[0], start[1]-2)]
        valid_kill_move = [(start[0]-1, start[1]-1), (start[0]+1, start[1]-1)]
        move_piece = True
        
        if end in valid_kill_move and board.is_empty(end[0], end[1]) == False:
            #print(board.background_board[end[1]-1][end[0]-1].piece_type)
            
            if board.background_board[end[1]-1][end[0]-1].color == "white":
                board.background_board[end[1]-1][end[0]-1] = 0
                board.board[end[1]-1][end[0]-1] = 0
            else:
                pass
                
           
        else:
            if end in valid_moves and board.is_empty(end[0], end[1]) == False:
                move_piece = False
            if (start[1] == 7) and (end in valid_moves):
                pass
            elif (start[1] < 7) and (end in valid_moves[:1]):
                pass
            else:
                move_piece = False

        return move_piece

    def generate_valid_moves_bishop(self, start, finish, board):
        if board.is_empty(finish[0], finish[1]) == False and board.background_board[finish[1]-1][finish[0]-1].color == self.color:
            return False

    def generate_valid_moves_rook(self, start, finish, board):
        if board.is_empty(finish[0], finish[1]) == False and board.background_board[finish[1]-1][finish[0]-1].color == self.color:
            return False
       
        else:
          
            if start == finish:
                if board.is_empty(finish[0], finish[1]) == False and board.background_board[finish[1]-1][finish[0]-1].color != self.color:
                    self.kill_piece(finish[0], finish[1], board)
                    return True
                else:
                    return True
                
            

            if start[1] == finish[1]:#moving horizontally
                if start[0] < finish[0]:
                    start[0] += 1
                if start[0] > finish[0]:
                    start[0] -= 1

            if start[0] == finish[0]:
                if start[1] < finish[1]: #going down
                    start[1] += 1
                if start[1] > finish[1]: #going up
                    start[1] -= 1

                
            

            if board.is_empty(start[0], start[1]) == False and (start != finish):
                return False
            

            return self.generate_valid_moves_rook(start, finish, board)

    
    def kill_piece(self, x, y, board):
        if board.is_empty(x, y) == False:
            if (self.color == "white" and board.background_board[y-1][x-1].color == "black") or (self.color == "black" and board.background_board[y-1][x-1].color == "white"):
                board.background_board[y-1][x-1] = 0
                board.board[y-1][x-1] = 0
            

    
    def white_pawn_movement(self, start, end, board):
        
        valid_moves = [(start[0], start[1]+1), (start[0], start[1]+2)]
        valid_kill_move = [(start[0]+1, start[1]+1), (start[0]-1, start[1]+1)]
        move_piece = True
        
        if end in valid_kill_move and board.is_empty(end[0], end[1]) == False:
            #print(board.background_board[end[1]-1][end[0]-1].piece_type)
            
            if board.background_board[end[1]-1][end[0]-1].color == "black":
                board.background_board[end[1]-1][end[0]-1] = 0
                board.board[end[1]-1][end[0]-1] = 0
            else:
                move_piece = False
        else:
            if end in valid_moves and board.is_empty(end[0], end[1]) == False:
                move_piece = False
            if (start[1] == 2) and (end in valid_moves):
                pass
            elif (start[1] > 2) and (end in valid_moves[:1]):
                pass
            else:
                move_piece = False

        return move_piece

        
  
    