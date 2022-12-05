import pygame
from board import Board, SCREEN
import button


pygame.init()
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
global turn 
turn = 0

SIZE = (900, 700)

PIECE_SIZE = 75
pygame.display.set_caption("Chess Game")



    
# The clock will be used to control how fast the SCREEN updates
clock = pygame.time.Clock()

cellSize = 70       

board = Board()
game_paused = False

font = pygame.font.Font("Libre_Baskerville/LibreBaskerville-Bold.ttf", 80)
font_two = pygame.font.Font("Libre_Baskerville/LibreBaskerville-Bold.ttf", 10)
font_three = pygame.font.Font("Libre_Baskerville/LibreBaskerville-Bold.ttf", 25)


resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()
question_img = pygame.image.load('images/question.png').convert_alpha()
about_img = pygame.image.load('images/about.png').convert_alpha()
#create button instances
resume_button = button.Button(450,145,resume_img, 1)
quit_button = button.Button(480, 270, quit_img, 1)
about_button = button.Button(560, 380, about_img, 0.09)
question_button = button.Button(560, 450, question_img, 0.09)
back_button = button.Button(470, 525, back_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  SCREEN.blit(img, (x, y))

rules = """The Pieces
    Pawns - They can move one square forward or two squares on their first move and can capture by moving one square diagonally forwards. Can be promoted if they reach the far end of the board.
    Knights - move in an L-shape - one square vertically and two squares horizontally, or one square horizontally and two squares vertically. Can jump over any pieces in its path.
    Bishops - move any number of squares diagonally in a straight line. May not jump over other pieces.
    Rooks - move any number of squares vertically or horizontally in a straight line. May not jump over other pieces.
    The Queen - moves any number of squares vertically, horizontally, or diagonally in a straight line. May not jump over other pieces.
    The King - moves one square in any direction. May not move onto a square threatened by an enemy piece.

Check and Checkmate
    Check - if the king is threatened by an enemy piece, he is in 'check', and must escape from check. This can be done by moving the king, capturing the checking piece, or blocking the checking piece.
    Checkmate - if the king is in check and can't get out of check, he is in checkmate and the game is lost.

Castling
    Castling - move the king two squares towards the rook, and jump the rook to the square on the other side of the king.
    You cannot castle if...
    You have previously moved your king or rook.
    There are pieces between your king and rook.
    Your king in check.
    Your king would be in check at the end of the move.
    Your king would cross a square that is threatened by an enemy piece.

En Passant
    En Passant - if you have a pawn on the fifth rank, and your opponent moves an adjacent pawn two squares, you can capture the pawn as if it had only moved one square.
    You cannot capture en passant if...
    Your pawn is not on the fifth rank.
    The enemy pawn did not move two squares on the previous move.

"""

description = """
        My name is Elliott Perez and I am a first year student at Everett Community College. This was a project that was completed for my Stem 298 class and the goal of this project was to become more proficient in Python and Pygame. I am pursuing Computer Science as my major and I hope to transfer to Washington State University in the fall of 2023. 
"""
def display_text(surface, text, pos, font, color):
    collection = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    x,y = pos
    for lines in collection:
        for words in lines:
            word_surface = font.render(words, True, color)
            word_width , word_height = word_surface.get_size()
            if x + word_width >= 1100:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x,y))
            x += word_width + space
        x = pos[0]
        y += word_height

def question():
    
    question_text = font.render("How to play", True, (43, 48, 58))
    while True:
        SCREEN.fill((186, 193, 184))
        SCREEN.blit(question_text, pygame.Rect(cellSize*4.5, cellSize*0, cellSize, cellSize))
        display_text(SCREEN, rules, (0, 150), font_two, (43, 48, 58))
        if back_button.draw(SCREEN):
            menu()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()

def about():
    about_text = font.render("About", True, (43, 48, 58))
    while True:
        SCREEN.fill((186, 193, 184))
        SCREEN.blit(about_text, pygame.Rect(cellSize*5.5, cellSize*0, cellSize, cellSize))
        display_text(SCREEN, description, (20, 130), font_three, (43, 48, 58))
        if back_button.draw(SCREEN):
            menu()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()


def menu():
    while True:
        SCREEN.fill((186, 193, 184))
        SCREEN.blit(font_three.render("Help", True, (43, 48, 58)), pygame.Rect(cellSize*7, cellSize*6.5, cellSize, cellSize))
        SCREEN.blit(font_three.render("About", True, (43, 48, 58)), pygame.Rect(cellSize*6.70, cellSize*5.5, cellSize, cellSize))
            #check menu state
        if board.menu_state == "main":
        #draw pause screen buttons
            if resume_button.draw(SCREEN):
                main()
            if question_button.draw(SCREEN):
                question()
            if about_button.draw(SCREEN):
                about()
            if quit_button.draw(SCREEN):
                pygame.quit()
        #check if the options menu is open
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()



def main():
    
    board.draw_board(SCREEN)
    pygame.display.update()
    selected = ()
    moves = []
    carryOn = True
    

    while carryOn:
        
        board.draw_board(SCREEN)
        
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: 
                carryOn = False # Flag that we are done so we can exit the while loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if board.promotion == True:
                    moves.append(board.coordinate_to_replace)
                    x, y = board.get_square_under_mouse()
                    if (board.color_to_blit == "black" and x == 13) or (board.color_to_blit == "white" and x == 14):
                        moves.append((x, y))
                        board.replace_values(board.coordinate_to_replace, x, y)
                        selected = ()
                        moves = []
                    else:
                        pass
                                    
                if board.promotion == False:
                
                    piece, x, y = board.get_square_under_mouse()
                    
                    
                    if (x, y) == (14, 0) or (x, y) == (15, 0):
                        menu()
                    if (x, y) == (15, 9):
                        about()
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
                                    board.update_boards([moves][0], check, piece, board)
                        
                                else:
                                    if piece.color == "white" and (board.turn % 2 == 1):
                                        if piece.piece_type == "r":
                                            print("rook")
                                            check = piece.generate_valid_moves_rook(list(moves[0]), list(moves[1]), board)
                                            print(check)
                                        elif piece.piece_type == "b":
                                            check = piece.generate_valid_moves_bishop(list(moves[0]), list(moves[1]), board)
                                        elif piece.piece_type == "kn":
                                            check = piece.generate_valid_moves_knight(list(moves[0]), list(moves[1]), board)
                                        elif piece.piece_type == "q":
                                            check = piece.generate_valid_moves_queen(list(moves[0]), list(moves[1]), board)                                
                                        elif piece.piece_type == "k":
                                            check = piece.generate_valid_moves_king(list(moves[0]), list(moves[1]), board, piece.color)                          
                                        else:
                                            check = piece.white_pawn_movement((first_click, second_click), (x, y), board)
                                        if y == 8 and piece.piece_type == "p":
                                            board.promotion = True
                                            board.color_to_blit = "white"
                                            board.coordinate_to_replace = (x, y)
                                            
                                        if check == False:
                                            pass
                                    
                                        else:
                                            board.update_boards([moves][0], check, piece, board)
                                             
                                    
                                    if piece.color == "black" and (board.turn % 2 == 0):
                                        if piece.piece_type == "r":
                                            
                                            check = piece.generate_valid_moves_rook(list(moves[0]), list(moves[1]), board)
                                    
                                        elif piece.piece_type == "b":
                                            check = piece.generate_valid_moves_bishop(list(moves[0]), list(moves[1]), board)
                                        elif piece.piece_type == "kn":
                                            check = piece.generate_valid_moves_knight(list(moves[0]), list(moves[1]), board)
                                        elif piece.piece_type == "q":
                                            check = piece.generate_valid_moves_queen(list(moves[0]), list(moves[1]), board)                                
                                        elif piece.piece_type == "k":
                                            check = piece.generate_valid_moves_king(list(moves[0]), list(moves[1]), board, piece.color)                          
                                            print(check)
                                            print("")
                                        else:
                                            check = piece.black_pawn_movement((first_click, second_click), (x, y), board)
                                        
                                        if y == 1 and piece.piece_type == "p":
                                            board.promotion = True
                                            board.color_to_blit = "black"
                                            board.coordinate_to_replace = (x, y)

                                            
                                            
                                        if check == False:
                                            pass
                                        else:
                                            board.update_boards([moves][0], check, piece, board)
                                            
                                


                                selected = ()
                                moves = []
                                
                                            

                        pygame.display.update()
                
        # --- Limit to 60 frames per second
        clock.tick(60)
    
#Once we have exited the main program loop we can stop the game engine:
    pygame.quit()
main()
