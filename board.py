import pygame
from pieces import Piece
SIZE = (900, 700)
SCREEN = pygame.display.set_mode(SIZE)


cellSize = 70
PIECE_SIZE = 75

BLACK_BISHOP = Piece("black", "b", "/Users/elper2/Documents/Python/Chess/images/black_bishop.png")
BLACK_BISHOP_IMAGE = pygame.transform.scale(pygame.image.load(BLACK_BISHOP.image), (PIECE_SIZE, PIECE_SIZE))

WHITE_BISHOP = Piece("white", "b", "/Users/elper2/Documents/Python/Chess/images/white_bishop.png")
WHITE_BISHOP_IMAGE = pygame.transform.scale(pygame.image.load(WHITE_BISHOP.image), (PIECE_SIZE, PIECE_SIZE))


BLACK_KING = Piece("black", "k", "/Users/elper2/Documents/Python/Chess/images/black_king.png")
BLACK_KING_IMAGE = pygame.transform.scale(pygame.image.load(BLACK_KING.image), (PIECE_SIZE, PIECE_SIZE))


WHITE_KING = Piece("white", "k", "/Users/elper2/Documents/Python/Chess/images/white_king.png")
WHITE_KING_IMAGE = pygame.transform.scale(pygame.image.load(WHITE_KING.image), (PIECE_SIZE, PIECE_SIZE))


BLACK_QUEEN = Piece("black", "q", "/Users/elper2/Documents/Python/Chess/images/black_queen.png")
BLACK_QUEEN_IMAGE = pygame.transform.scale(pygame.image.load(BLACK_QUEEN.image), (PIECE_SIZE, PIECE_SIZE))

WHITE_QUEEN = Piece("white", "q", "/Users/elper2/Documents/Python/Chess/images/white_queen.png")
WHITE_QUEEN_IMAGE = pygame.transform.scale(pygame.image.load(WHITE_QUEEN.image), (PIECE_SIZE, PIECE_SIZE))

BLACK_KNIGHT = Piece("black", "kn", "/Users/elper2/Documents/Python/Chess/images/black_knight.png")
BLACK_KNIGHT_IMAGE = pygame.transform.scale(pygame.image.load(BLACK_KNIGHT.image), (PIECE_SIZE, PIECE_SIZE))

WHITE_KNIGHT = Piece("white", "kn", "/Users/elper2/Documents/Python/Chess/images/white_knight.png")
WHITE_KNIGHT_IMAGE = pygame.transform.scale(pygame.image.load(WHITE_KNIGHT.image), (PIECE_SIZE, PIECE_SIZE))

BLACK_PAWN = Piece("black", "p", "/Users/elper2/Documents/Python/Chess/images/black_pawn.png")
BLACK_PAWN_IMAGE = pygame.transform.scale(pygame.image.load(BLACK_PAWN.image), (PIECE_SIZE, PIECE_SIZE))


WHITE_PAWN = Piece("white", "p", "/Users/elper2/Documents/Python/Chess/images/white_pawn.png")
WHITE_PAWN_IMAGE = pygame.transform.scale(pygame.image.load(WHITE_PAWN.image), (PIECE_SIZE, PIECE_SIZE))


BLACK_ROOK = Piece("black", "r", "/Users/elper2/Documents/Python/Chess/images/black_rook.png")
BLACK_ROOK_IMAGE = pygame.transform.scale(pygame.image.load(BLACK_ROOK.image), (PIECE_SIZE, PIECE_SIZE))


WHITE_ROOK = Piece("white", "r", "/Users/elper2/Documents/Python/Chess/images/white_rook.png")
WHITE_ROOK_IMAGE = pygame.transform.scale(pygame.image.load(WHITE_ROOK.image), (PIECE_SIZE, PIECE_SIZE))


class Board:
    def __init__(self):
        self.background_board = [[WHITE_ROOK, WHITE_KNIGHT, WHITE_BISHOP, WHITE_QUEEN, WHITE_KING, WHITE_BISHOP, WHITE_KNIGHT, WHITE_ROOK], [WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN], [BLACK_ROOK, BLACK_KNIGHT, BLACK_BISHOP, BLACK_QUEEN, BLACK_KING, BLACK_BISHOP, BLACK_KNIGHT, BLACK_ROOK]]
        self.board = [[WHITE_ROOK_IMAGE,WHITE_KNIGHT_IMAGE, WHITE_BISHOP_IMAGE,WHITE_QUEEN_IMAGE,WHITE_KING_IMAGE,WHITE_BISHOP_IMAGE,WHITE_KNIGHT_IMAGE,WHITE_ROOK_IMAGE], [WHITE_PAWN_IMAGE,WHITE_PAWN_IMAGE,WHITE_PAWN_IMAGE,WHITE_PAWN_IMAGE,WHITE_PAWN_IMAGE,WHITE_PAWN_IMAGE,WHITE_PAWN_IMAGE,WHITE_PAWN_IMAGE], [0 , 0, 0, 0, 0, 0, 0, 0], [0 , 0, 0, 0, 0, 0, 0, 0], [0 , 0, 0, 0, 0, 0, 0, 0], [0 , 0, 0, 0, 0, 0, 0, 0], [BLACK_PAWN_IMAGE, BLACK_PAWN_IMAGE, BLACK_PAWN_IMAGE, BLACK_PAWN_IMAGE, BLACK_PAWN_IMAGE, BLACK_PAWN_IMAGE, BLACK_PAWN_IMAGE, BLACK_PAWN_IMAGE], [BLACK_ROOK_IMAGE, BLACK_KNIGHT_IMAGE,BLACK_BISHOP_IMAGE,BLACK_QUEEN_IMAGE,BLACK_KING_IMAGE, BLACK_BISHOP_IMAGE,BLACK_KNIGHT_IMAGE, BLACK_ROOK_IMAGE]]
        self.pos = None
    

    def draw_board(self, surface):
        board = pygame.Surface((cellSize * 10, cellSize * 10))
        
        board.fill((12, 124, 89))
        SCREEN.fill((186, 193, 184))
        for row in range(1, 9):
            for col in range((row %2)+1, 9, 2):
                pygame.draw.rect(board, (88, 164, 176), (row*cellSize, col*cellSize, cellSize, cellSize))
            surface.blit(board, board.get_rect())

        outer = [0,9]
        font = pygame.font.SysFont(None, 40)
        font_two = pygame.font.SysFont(None, 17)
    
        p1 = font_two.render("Player 1", True, (43, 48, 58))
        p2 = font_two.render("Player 2", True, (43, 48, 58))
        killed_black_rook = font_two.render(f"{BLACK_ROOK.killed}", True, (43, 48, 58))
        killed_black_knight = font_two.render(f"{BLACK_KNIGHT.killed}", True, (43, 48, 58))
        killed_black_bishop = font_two.render(f"{BLACK_BISHOP.killed}", True, (43, 48, 58))
        killed_black_queen = font_two.render(f"{BLACK_QUEEN.killed}", True, (43, 48, 58))
        killed_black_pawn = font_two.render(f"{BLACK_PAWN.killed}", True, (43, 48, 58))
        

        killed_white_rook = font_two.render(f"{WHITE_ROOK.killed}", True, (43, 48, 58))
        killed_white_knight = font_two.render(f"{WHITE_KNIGHT.killed}", True, (43, 48, 58))
        killed_white_bishop = font_two.render(f"{WHITE_BISHOP.killed}", True, (43, 48, 58))
        killed_white_queen = font_two.render(f"{WHITE_QUEEN.killed}", True, (43, 48, 58))
        killed_white_pawn = font_two.render(f"{WHITE_PAWN.killed}", True, (43, 48, 58))
        
        
        v_coordinates = [8, 7, 6, 5, 4, 3, 2, 1]
        h_coordinates = ["A", "B", "C", "D", "E", "F", "G", "H"]
        for row in outer:
            for col in range(12):
                pygame.draw.rect(board, (186, 193, 184), (row*cellSize, col*cellSize, cellSize, cellSize))
                pygame.draw.rect(board, (186, 193, 184), (col*cellSize, row*cellSize, cellSize, cellSize))
                SCREEN.blit(board, board.get_rect())
               

        for row in outer:
            for col in range(1, 9):
                letter = font.render(h_coordinates[col-1], True, (43, 48, 58))
                number = font.render(str(v_coordinates[col-1]), True, (43, 48, 58))
                if row == 9:
                    surface.blit(number, pygame.Rect(row*cellSize, col*cellSize, cellSize, cellSize))
                    surface.blit(letter, pygame.Rect(col*cellSize, row*cellSize, cellSize, cellSize))
                
 
        
        
        for rows in range(8):
            for cols in range(0, 8):
                if self.board[rows][cols] != 0:
                    surface.blit(self.board[rows][cols], pygame.Rect((cols+1)*cellSize, (rows+1)*cellSize, cellSize, cellSize))
                continue

        surface.blit(p2, pygame.Rect(cellSize*10, cellSize*0, cellSize, cellSize))
        surface.blit(WHITE_ROOK_IMAGE, pygame.Rect(9.5* cellSize, 1* cellSize, cellSize, cellSize))
        surface.blit(killed_white_rook, pygame.Rect(cellSize*10, cellSize*0.97, cellSize, cellSize))
        surface.blit(WHITE_KNIGHT_IMAGE, pygame.Rect(11* cellSize, 1* cellSize, cellSize, cellSize))
        surface.blit(killed_white_knight, pygame.Rect(cellSize*11.5, cellSize*0.97, cellSize, cellSize))
        surface.blit(WHITE_BISHOP_IMAGE, pygame.Rect(9.5* cellSize, 2* cellSize, cellSize, cellSize))
        surface.blit(killed_white_bishop, pygame.Rect(cellSize*10, cellSize*1.97, cellSize, cellSize))
        surface.blit(WHITE_QUEEN_IMAGE, pygame.Rect(11* cellSize, 2* cellSize, cellSize, cellSize))
        surface.blit(killed_white_queen, pygame.Rect(cellSize*11.5, cellSize*1.97, cellSize, cellSize))
        surface.blit(WHITE_PAWN_IMAGE, pygame.Rect(9.5* cellSize, 3* cellSize, cellSize, cellSize))
        surface.blit(killed_white_pawn, pygame.Rect(cellSize*10, cellSize*2.97, cellSize, cellSize))
        surface.blit(p1, pygame.Rect(cellSize*10, cellSize*5, cellSize, cellSize))


        
        surface.blit(BLACK_ROOK_IMAGE, pygame.Rect(9.5* cellSize, 6* cellSize, cellSize, cellSize))
        surface.blit(killed_black_rook, pygame.Rect(cellSize*10, cellSize*5.97, cellSize, cellSize))
        surface.blit(BLACK_KNIGHT_IMAGE, pygame.Rect(11* cellSize, 6* cellSize, cellSize, cellSize))
        surface.blit(killed_black_knight, pygame.Rect(cellSize*11.5, cellSize*5.97, cellSize, cellSize))
        surface.blit(BLACK_BISHOP_IMAGE, pygame.Rect(9.5* cellSize, 7* cellSize, cellSize, cellSize))
        surface.blit(killed_black_bishop, pygame.Rect(cellSize*10, cellSize*6.97, cellSize, cellSize))
        surface.blit(BLACK_QUEEN_IMAGE, pygame.Rect(11* cellSize, 7* cellSize, cellSize, cellSize))
        surface.blit(killed_black_queen, pygame.Rect(cellSize*11.5, cellSize*6.97, cellSize, cellSize))
        surface.blit(BLACK_PAWN_IMAGE, pygame.Rect(9.5* cellSize, 8* cellSize, cellSize, cellSize))
        surface.blit(killed_black_pawn, pygame.Rect(cellSize*10, cellSize*7.97, cellSize, cellSize))
       

    
        
    def get_square_under_mouse(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) 
        
        x, y = [int(v // cellSize) for v in mouse_pos]
        
        try: 
            if (9 > x >= 1) and (9 > y >= 1):
                return(self.background_board[y-1][x-1], x, y)
        except IndexError: 
            return(None, x, y)
        return None, None, None
    
    def draw_red_rectangle(self, x, y):
        if x is None or y is None:
            pass
        else:
            rect = (0 + x * cellSize, 1 + y * cellSize, cellSize, cellSize)
            pygame.draw.rect(SCREEN, (255, 0, 0, 50), rect, 4)

    def update_boards(self, moves, is_valid):
        if is_valid == False:
            first = moves[0][0]
            second = moves[0][1]
            third = moves[0][0]
            fourth = moves[0][1]
        else:
            first = moves[0][0]
            second = moves[0][1]
            third = moves[1][0]
            fourth = moves[1][1]
            
            
            
        self.board[second-1][first-1], self.board[fourth-1][third-1] = self.board[fourth-1][third-1], self.board[second-1][first-1]
        self.background_board[second-1][first-1], self.background_board[fourth-1][third-1] = self.background_board[fourth-1][third-1], self.background_board[second-1][first-1]
        self.draw_board(SCREEN)
        



    def is_empty(self, x, y):
        if x is None or y is None:
            pass
        else:

            return self.background_board[y-1][x-1] == 0
    
    def promotion(self, coordinates, board):
        surface = pygame.Surface((100, 100))
        surface.fill((49, 20, 100))
        pygame.draw.rect(surface, (8, 9, 100), (0, 0, 100, 100))
        SCREEN.blit(surface, surface.get_rect())
        