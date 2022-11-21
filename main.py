import pygame
from board import Board, SCREEN

pygame.init()
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)


SIZE = (900, 700)

PIECE_SIZE = 75
pygame.display.set_caption("Chess Game")



 
# The clock will be used to control how fast the SCREEN updates
clock = pygame.time.Clock()

cellSize = 70

board = Board()
def main():

    board.draw_board(SCREEN)
    pygame.display.update()
    selected = ()
    moves = []
    carryOn = True
    turn = 0 
    while carryOn:
        
        # --- Main event loop
        board.draw_board(SCREEN)
        
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we can exit the while loop
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                piece, x, y = board.get_square_under_mouse()
            
                if (board.is_empty(x, y) == True) and len(moves) == 0:
                    pass
                else:
                    
                    board.draw_red_rectangle(x, y)
                    pygame.display.update() 
                    selected = (x, y)

                    moves.append(selected)
                    
                    first_click = moves[0][0]
                    second_click = moves[0][1]
                    if first_click is None or second_click is None:
                        moves = []
                        selected = ()
                    else:
                        piece = board.background_board[second_click-1][first_click-1]
                        
                        if len(moves) == 2:
                            if moves[0] == moves[1]:
                                check = True
                                board.update_boards([moves][0], check)
                    
                            else:
                                if piece.color == "white" and (turn % 2 == 1):
                                    if piece.piece_type == "r":
                                        check = piece.generate_valid_moves_rook(list(moves[0]), list(moves[1]), board)
                                    elif piece.piece_type == "b":
                                        check = piece.generate_valid_moves_bishop(list(moves[0]), list(moves[1]), board)
                                    elif piece.piece_type == "kn":
                                        check = piece.generate_valid_moves_knight(list(moves[0]), list(moves[1]), board)
                                    else:
                                        check = piece.white_pawn_movement((first_click, second_click), (x, y), board)
                                    
                                    if check == False:
                                        pass
                                    else:
                                    
                                        board.update_boards([moves][0], check)
                                        turn +=1
                                
                                if piece.color == "black" and (turn % 2 == 0):
                                    if piece.piece_type == "r":
                                        
                                        check = piece.generate_valid_moves_rook(list(moves[0]), list(moves[1]), board)
                                
                                    elif piece.piece_type == "b":
                                        check = piece.generate_valid_moves_bishop(list(moves[0]), list(moves[1]), board)
                                    elif piece.piece_type == "kn":
                                        check = piece.generate_valid_moves_knight(list(moves[0]), list(moves[1]), board)
                                    else:
                                        check = piece.black_pawn_movement((first_click, second_click), (x, y), board)
                                    
                                    
                                    if check == False:
                                        pass
                                    else:
                                        board.update_boards([moves][0], check)
                                        turn += 1
                            


                            selected = ()
                            moves = []
                                
                            

                    pygame.display.update()
                
        # --- Limit to 60 frames per second
        clock.tick(60)
    
#Once we have exited the main program loop we can stop the game engine:
    pygame.quit()
main()
