import numpy as np
from piece import Piece
import pygame

LIGHT_SQUARE = (193, 154, 107)
DARK_SQUARE = (101, 67, 33)
CLICK_SQUARE = (242, 204, 52)
SQUARE_SIZE = 100
NUM_ROWS_COLS = 8
NUM_PIECES = 12

class Board:
    def __init__(self, id):
        self.num_jumps = 0
        self.num_own_pieces = NUM_PIECES
        self.num_opp_pieces = NUM_PIECES
        self.player_id = id
        self.board_pattern = []
        self.board_pieces = [] # Main array, keeps track of which pieces are where
        self.starting_list = []
        self.color_board()
        self.create_board()

    # Creates the checkerboard pattern
    def color_board(self): 
        self.board_pattern = np.zeros((NUM_ROWS_COLS,NUM_ROWS_COLS), dtype=int)
        self.board_pattern[1::2,::2] = 1
        self.board_pattern[::2,1::2] = 1

    # Defines the starting positions of pieces
    def starting_position(self, id): 
        x = 0
        for row in self.board_pattern:
            y = 0
            for square in row:
                if 0 <= x <= 2 or 5 <= x <= 7:
                    if square == 1:
                        self.starting_list.append([x, y])
                y += 1
            x += 1

        return self.starting_list[id]
    
    # Creates the board and puts pawns on the appropriate tiles 
    def create_board(self):
        self.board_pieces = ([], [], [], [], [], [], [], [])

        for i in range(NUM_ROWS_COLS):
            for _ in range(NUM_ROWS_COLS):
                self.board_pieces[i].append(None)
        
        for i in range(NUM_PIECES * 2):
            if i < NUM_PIECES:
                pos = self.starting_position(i)
                if self.player_id == 1:
                    piece = Piece(i, pos[0], pos[1], "r", pygame.image.load("imgs/red-pawn.png"))
                    self.board_pieces[pos[0]][pos[1]] = piece
                else:
                    piece = Piece(i, pos[0], pos[1], "r", pygame.image.load("imgs/black-pawn.png"))
                    self.board_pieces[pos[0]][pos[1]] = piece
            else:
                pos = self.starting_position(i)
                if self.player_id == 1:
                    piece = Piece(i, pos[0], pos[1], "b", pygame.image.load("imgs/black-pawn.png"))
                    self.board_pieces[pos[0]][pos[1]] = piece
                else:
                    piece = Piece(i, pos[0], pos[1], "b", pygame.image.load("imgs/red-pawn.png"))
                    self.board_pieces[pos[0]][pos[1]] = piece

    # Takes the image for each piece and scales it to fit in each tile
    def draw_pieces(self, window):
        for row in range(NUM_ROWS_COLS):
            for col in range(NUM_ROWS_COLS):
                if self.board_pieces[row][col] is not None:
                    window.blit(pygame.transform.scale((self.board_pieces[row][col].img), (SQUARE_SIZE, SQUARE_SIZE)),
                        pygame.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    
    # Colors the board using the checkerboard pattern (and highlights tiles if necessary)
    def draw_board(self, window):
        window.fill(DARK_SQUARE)
        for row in range(NUM_ROWS_COLS):
            for col in range(NUM_ROWS_COLS):
                if self.board_pattern[row][col] == 0:
                    pygame.draw.rect(window, LIGHT_SQUARE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                elif self.board_pattern[row][col] == 2: # Colors tile if move can be made
                    pygame.draw.rect(window, CLICK_SQUARE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def is_piece(self, x, y):
        if self.board_pieces[y][x] is not None:
            return True
        else:
            return False

    def is_own_piece(self, x, y):
        if self.is_piece(x, y):
            if self.board_pieces[y][x].color == 'b':
                return True
            else:
                return False
        else:
            return False

    def is_opp_piece(self, x, y):
        if self.is_piece(x, y):
            if self.board_pieces[y][x].color == 'r':
                return True
            else:
                return False
        else:
            return False

    # Returns possible moves
    def moves(self, x, y):
        move_list = []
        
        if x != 7 and y != 0: # Make sure not on edge of board
            if not self.is_piece(x+1, y-1):
                move_list.append((x+1, y-1))
                
        if x != 0 and y != 0:
            if not self.is_piece(x-1, y-1):
                move_list.append((x-1, y-1))

        return move_list

    # Returns possible king moves
    def king_moves(self, x, y):
        move_list = self.moves(x,y)

        if x != 7 and y != 7:
            if not self.is_piece(x+1, y+1):
                move_list.append((x+1, y+1))
                
        if x != 0 and y != 7:
            if not self.is_piece(x-1, y+1):
                move_list.append((x-1, y+1))        

        return move_list

    # Colors tiles that can be used to jump pieces
    def color_moves(self, moves):
        self.color_board()
        for move in moves:
            self.board_pattern[move[0]][move[1]] = 2

    # Returns possible jumps for single pawn
    def jumps(self, x, y):
        self.color_board() # Removes the highlighted square after jump
        jump_list = []
        
        # Jump diagonal left
        if x > 1 and y > 1:
            if self.is_piece(x-1, y-1) and self.board_pieces[y-1][x-1].is_opp_piece() and not self.is_piece(x-2, y-2):
                jump_list.append((x-2, y-2))

        # Jump diagonal right
        if x < 6 and y > 1:
            if self.is_piece(x+1, y-1) and self.board_pieces[y-1][x+1].is_opp_piece() and not self.is_piece(x+2, y-2):
                jump_list.append((x+2, y-2))

        return jump_list
    
    # Returns possible king jumps for single king
    def king_jumps(self, x, y):
        jump_list = self.jumps(x, y)
        
        if x > 1 and y < 6:
            if self.is_piece(x-1, y+1) and self.board_pieces[y+1][x-1].is_opp_piece() and not self.is_piece(x-2, y+2):
                jump_list.append((x-2, y+2))

        if x < 6 and y < 6:
            if self.is_piece(x+1, y+1) and self.board_pieces[y+1][x+1].is_opp_piece() and not self.is_piece(x+2, y+2):
                jump_list.append((x+2, y+2))

        return jump_list

    # Returns all possible jumps
    def available_jumps(self):
        jump_list = {}
        
        for x in range(NUM_ROWS_COLS):
            for y in range(NUM_ROWS_COLS):
                if self.is_piece(x, y) and self.board_pieces[y][x].is_own_piece():
                    if len(self.jumps(x, y)) > 0: 
                        jump_list[(x, y)] = self.jumps(x, y)

        self.num_jumps = len(jump_list)

        return jump_list

    # Returns all possible king jumps
    def available_king_jumps(self):
        jump_list = {}
        
        for x in range(NUM_ROWS_COLS):
            for y in range(NUM_ROWS_COLS):
                if self.is_own_piece(x, y):
                    if len(self.king_jumps(x, y)) > 0: 
                        jump_list[(x, y)] = self.king_jumps(x, y)

        self.num_jumps = len(jump_list)

        return jump_list
    
    # Moves the desired piece and checks if it should turn into a king
    def move_piece(self, start_x, start_y, end_x, end_y):
        self.board_pieces[end_y][end_x] = self.board_pieces[start_y][start_x]
        self.board_pieces[start_y][start_x] = None

        piece = self.board_pieces[end_y][end_x]
        if end_y == 0 and piece.color == 'b' or end_y == 7 and piece.color == 'r':
            piece.make_king()

    # Updates the number of pieces and removes the piece from the board
    def jump_piece(self, jump_list):
        for x, y in jump_list:
            if self.board_pieces[y][x].color == 'b':
                self.num_own_pieces -= 1
            else:
                self.num_opp_pieces -= 1

            self.board_pieces[y][x] = None

    def is_king(self, x, y):
        if self.board_pieces[y][x].king:
            return True
        else:
            return False