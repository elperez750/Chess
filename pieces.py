import pygame


SIZE = (900, 700)
SCREEN = pygame.display.set_mode(SIZE)

cellSize = 70
white_king_pos = (5, 1)

black_king_pos = (5, 8)
class Piece:
   
   
    def __init__(self, color, piece_type, image):
        self.color = color
        self.piece_type = piece_type
        self.image = image
        self.killed = 0
        

    def black_pawn_movement(self, start, end, board):
        valid_moves = [(start[0], start[1]-1), (start[0], start[1]-2)]
        valid_kill_move = [(start[0]-1, start[1]-1), (start[0]+1, start[1]-1)]
        move_piece = True
        
        if end in valid_kill_move and board.is_empty(end[0], end[1]) == False:
            #print(board.background_board[end[1]-1][end[0]-1].piece_type)
            
            if board.background_board[end[1]-1][end[0]-1].color == "white":
                self.kill_piece(end[0], end[1], board)
                
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

  


    def generate_valid_moves_rook(self, start, finish, board):
        if board.is_empty(finish[0], finish[1]) == False and board.background_board[finish[1]-1][finish[0]-1].color == self.color:
            return False
       
        else:
            if (start == finish):
                if board.is_empty(finish[0], finish[1]) == False and board.background_board[finish[1]-1][finish[0]-1].color != self.color and (self.check(finish[0], finish[1], self.color, board) != False):
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

    def generate_valid_moves_knight(self, start, finish, board):
        if abs(abs(start[0]-finish[0])- abs(start[1]-finish[1])) == 1:
            if board.is_empty(finish[0], finish[1]) == False and board.background_board[finish[1]-1][finish[0]-1].color == self.color:
                return False
            if board.is_empty(finish[0], finish[1]) == False and board.background_board[finish[1]-1][finish[0]-1].color != self.color:
                self.kill_piece(finish[0], finish[1], board)
                return True
            if (abs(start[0]-finish[0]) == 0) or (abs(start[1]-finish[1]) == 0):
                return False
            if board.is_empty(finish[0], finish[1]):
                return True
            
        else:
            return False
        
    
    def generate_valid_moves_queen(self, start, finish, board):
        if start[0] == finish[0] or start[1] == finish[1]:
            return self.generate_valid_moves_rook(start, finish, board)
        else:
            return self.generate_valid_moves_bishop(start, finish, board)
        

    def generate_valid_moves_king(self, start, finish, board, color):
        valid_moves = [(1,1), (1,0), (0, 1)]
        if (((abs(start[0]-finish[0])), abs(start[1]-finish[1]))) in valid_moves:
            if color == "black":
                board.black_king_pos = (finish[0], finish[1])
            else:
                board.white_king_pos = (finish[0], finish[1])

            if start[0] == finish[0] or start[1] == finish[1]:
                return self.generate_valid_moves_rook(start, finish, board)
            else:
                return self.generate_valid_moves_bishop(start, finish, board)
        else:

            return False

    
        

    def generate_valid_moves_bishop(self, start, finish, board):
        if board.is_empty(finish[0], finish[1]) == False and board.background_board[finish[1]-1][finish[0]-1].color == self.color:
            return False
        else:
            if (start == finish):
                if (board.is_empty(finish[0], finish[1]) == False) and (board.background_board[finish[1]-1][finish[0]-1].color != self.color) and (self.check(finish[0], finish[1], self.color, board) != False):
                    self.kill_piece(finish[0], finish[1], board)
                    return True
                else:
                    return True

            if abs(start[0]-finish[0]) == abs(start[1]-finish[1]):
                if (start[0] < finish[0]) and (start[1] > finish[1]):
                    start[0] += 1
                    start[1] -= 1
                if (start[0] > finish[0]) and (start[1] < finish[1]):
                    start[0] -= 1
                    start[1] += 1
                if (start[0] > finish[0]) and (start[1] > finish[1]):
                    start[0] -=1
                    start[1] -= 1
                if (start[0] < finish[0]) and (start[1] < finish[1]):
                    start[0] += 1
                    start[1] += 1
            else:
                return False

            
            if board.is_empty(start[0], start[1]) == False and (start != finish):
                return False
        
        return self.generate_valid_moves_bishop(start, finish, board)

            
    def checkmate(self, x, y, color, board):
        all_possible_moves = [(x+1, y), (x-1, y), (x, y-1), (x, y+1), (x+1, y-1), (x-1, y-1), (x-1, y+1), (x+1, y+1)]
        answer = []
        for x, y in all_possible_moves:
            if ((x > 8 or y > 8)) or ((x < 1 or y < 1)):
                answer.append(False)
            else:
                if board.is_empty(x, y) == False:
                    if board.background_board[y-1][x-1].color == color:
                        answer.append(False)
                else:
                    answer.append(self.check(x, y, color, board))

        return answer

    def check(self, x, y, color, board):
        horizontal = self.check_horizontal_and_vertical(x, y, color, board)
        diagonal = self.diagonal(x, y, color, board)
        l_shape = self.check_knight_kills(x, y, color, board)
        print(horizontal)
        print("pie")
        print(diagonal)
        print("s")
        print(l_shape)
        return (horizontal and diagonal and l_shape) == True
       

     


    def diagonal(self, x, y, color, board):
        original_x = x
        original_y = y

        for i in range(9):
            if x == 8 or y == 1: 
                
                  
                break
            

            x += 1
            y -= 1
            
            print(x, y)
          
            if board.is_empty(x, y) == False:
                if board.background_board[y-1][x-1].color == color:
                    break
                
                if board.background_board[y-1][x-1].color != color:
                    if board.background_board[y-1][x-1].piece_type == "b":
                        return False
                    if board.background_board[y-1][x-1].piece_type == "q":
                        return False
                    if (x, y) == (original_x+1, original_y-1):
                        if board.background_board[y-1][x-1].piece_type == "k":
                            return False
                        if board.background_board[y-1][x-1].piece_type == "p" and color != "white":
                            return False
                    else:
                        break
            if board.is_empty(x, y):
                continue
        
        x = original_x
        y = original_y

        for i in range(9):
            if y == 1 or x == 1:
                
                break
               

            x -= 1
            y -= 1
            
            print(x, y)
          
            if board.is_empty(x, y) == False:
                if board.background_board[y-1][x-1].color == color:
                        break
                if board.background_board[y-1][x-1].color != color:
                    if board.background_board[y-1][x-1].piece_type == "b":
                        return False
                    if board.background_board[y-1][x-1].piece_type == "q":
                        return False
                    if (x, y) == (original_x-1, original_y-1):
                        if board.background_board[y-1][x-1].piece_type == "k":
                            return False
                        if board.background_board[y-1][x-1].piece_type == "p" and color != "white":
                            return False
                    else:
                        break
            if board.is_empty(x, y):
                continue
        

        x = original_x
        y = original_y

        for i in range(9):
            if x == 1 or y == 8:
                
                break
                

            x -= 1
            y += 1
            
            print(x, y)
           
            if board.is_empty(x, y) == False:
                if board.background_board[y-1][x-1].color == color:
                    break
                        
                    
                if board.background_board[y-1][x-1].color != color:
                    if board.background_board[y-1][x-1].piece_type == "b":
                        return False
                    if board.background_board[y-1][x-1].piece_type == "q":
                        return False
                    if (x, y) == (original_x-1, original_y+1):
                        if board.background_board[y-1][x-1].piece_type == "k":
                            return False
                        if board.background_board[y-1][x-1].piece_type == "p" and color != "black":
                            return False
                    else:
                        break
            if board.is_empty(x, y):
                   
                continue


        x = original_x
        y = original_y


        for i in range(9):
            if y == 8 or x == 8:
                break
            x += 1
            y += 1
            
            print(x, y)
        
            if board.is_empty(x, y) == False:
                if board.background_board[y-1][x-1].color == color:
                    break
                
                if board.background_board[y-1][x-1].color != color:
                    if board.background_board[y-1][x-1].piece_type == "b":
                        return False
                    if board.background_board[y-1][x-1].piece_type == "q":
                        return False
                    if (x, y) == (original_x+1, original_y+1):
                        if board.background_board[y-1][x-1].piece_type == "k":
                            return False
                        if board.background_board[y-1][x-1].piece_type == "p" and color != "black":
                            return False
                    else:
                        break
            if board.is_empty(x, y):
                continue

        print("diagnol")
        return True


    def check_horizontal_and_vertical(self, x, y, color, board):
        print((x, y))

    
            
       
        for square in range(x+1, 9):
            print(square, y)
            print(board.is_empty(6, 8))
            if board.is_empty(square, y) == False:
                if board.background_board[y-1][square-1].color == color:
                    break
                    
    
                if board.background_board[y-1][square-1].color != color:
                    if board.background_board[y-1][square-1].piece_type == "r":
                        return False
                    if board.background_board[y-1][square-1].piece_type == "q":
                        return False
                    if (square, y) == (x+1, y):
                        if board.background_board[y-1][x].piece_type == "k":
                            return False
                    else:
                        break

            if board.is_empty(square, y):
                if (square, y) == (8, y):
                    print("out of range")
                    break
                else:
                    continue
                    
       
        
        for square in reversed(range(1, x)):
            
            if board.is_empty(square, y) == False:
                if board.background_board[y-1][square-1].color == color:
                    break
                    
                if board.background_board[y-1][square-1].color != color:
                    if board.background_board[y-1][square-1].piece_type == "r":
                        return False
                    if board.background_board[y-1][square-1].piece_type == "q":
                        return False
                    if (square, y) == (x-1, y):
                        if board.background_board[y-1][x-2].piece_type == "k":
                            return False
                    else:
                        break
            if board.is_empty(square, y):
                if (square, y) == (1, y):
                    print("out of range")
                    break
                else:
                    continue
                
        
       
        for square in reversed(range(1, y)):
            

            if board.is_empty(x, square) == False:
                if board.background_board[square-1][x-1].color == color:
                    break
                    
                if board.background_board[square-1][x-1].color != color:
                    if board.background_board[square-1][x-1].piece_type == "r":
                        return False
                    if board.background_board[square-1][x-1].piece_type == "q":
                        return False
                    if (x, square) == (x, y-1):
                        if board.background_board[y-2][x-1].piece_type == "k":
                            return False
                    else:
                        break

            if board.is_empty(square, x):
                if (x, square) == (x, 1):
                
                    print("out of range")
                    break
                else:
                    continue

        
       
        for square in range(y+1, 9):
            if board.is_empty(x, square) == False:
                if board.background_board[square-1][x-1].color == color:
                    break
                
                if board.background_board[square-1][x-1].color != color:
                    if board.background_board[square-1][x-1].piece_type == "r":
                        return False
                    if board.background_board[square-1][x-1].piece_type == "q":
                        return False
                    if (x, square) == (x, y+1):
                        if board.background_board[y][x-1].piece_type == "k":
                            return False
                    else:
                        break

            if board.is_empty(square, x):
                if (x, square) == (x, 8):
                    print("Out of range")
                    break
                else:
                    continue
        
       
        return True

    def check_knight_kills(self, x, y, color, board):
        valid_kills = [(x-1, y-2), (x+1, y-2), (x-2, y-1), (x+2, y-1), (x-2, y+1), (x+2, y+1), (x-1, y+2), (x+1, y+2)]
        for x, y in valid_kills:
            print((x, y))
            print("askjdnfjadsilunfiasdoubf")
            if ((x > 8 or y > 8)) or ((x < 1 or y < 1)):
                continue
            else:
                if board.is_empty(x, y) == False:
                    if board.background_board[y-1][x-1].piece_type == "kn" and board.background_board[y-1][x-1].color != color:
                        return False
                else:
                    continue

        return True

    def kill_piece(self, x, y, board):
        if board.is_empty(x, y) == False:
            if (self.color == "white" and board.background_board[y-1][x-1].color == "black") or (self.color == "black" and board.background_board[y-1][x-1].color == "white"):
                board.background_board[y-1][x-1].killed += 1
                board.background_board[y-1][x-1] = 0
                board.board[y-1][x-1] = 0
                

    
    def white_pawn_movement(self, start, end, board):
        
        valid_moves = [(start[0], start[1]+1), (start[0], start[1]+2)]
        valid_kill_move = [(start[0]+1, start[1]+1), (start[0]-1, start[1]+1)]
        move_piece = True
        
        if end in valid_kill_move and board.is_empty(end[0], end[1]) == False:
            #print(board.background_board[end[1]-1][end[0]-1].piece_type)
            
            if board.background_board[end[1]-1][end[0]-1].color == "black":
                 self.kill_piece(end[0], end[1], board)
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

        
  
    