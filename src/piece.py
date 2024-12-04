import pygame

class Piece:

    def __init__(self, id, row, col, color, img):
        self.id = id
        self.starting_row = row
        self.starting_col = col
        self.color = color
        self.img = img
        self.king = False
    
    def is_own_piece(self):
        if self.color == 'b':
            return True
        else:
            return False

    def is_opp_piece(self):
        if self.color == 'r':
            return True
        else:
            return False
        
    def make_king(self):
        self.king = True
        if self.img == pygame.image.load("imgs/black-pawn.png"):
            self.img = pygame.image.load("imgs/black-king.png")
        else:
            self.img = pygame.image.load("imgs/red-king.png")