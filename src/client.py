import pygame
from board import Board
from network import Network
from sys import argv

SQUARE_SIZE = 100
WINDOW_SIZE = 800

def clicked_pos(pos):
    return int(pos[0]/SQUARE_SIZE), int(pos[1]/SQUARE_SIZE)

# Flips position coordinates so that it can be properly sent over the network
def flip_pos(x, y):
    return abs(7 - x), abs(7 - y)

def flip_pos_list(list):
    flipped = []

    for pos in list:
        flipped.append(flip_pos(pos[0], pos[1]))

    return flipped

def turn(x, y, piece_clicked):
    global own_turn
    available_jumps = board.available_jumps()
    available_king_jumps = board.available_king_jumps()

    if not piece_clicked: # Player clicked on a piece and then switched pieces
        if board.is_piece(x, y) and board.board_pieces[y][x].is_own_piece():
            if board.is_king(x, y):
                if len(available_king_jumps) == 0:
                    moves = board.king_moves(x, y)
                    board.color_moves(moves)
                else:
                    if (x, y) in available_king_jumps:
                        moves = available_king_jumps[(x, y)]    
                        board.color_moves(moves)
                    else:
                        return None # There are available jumps but wrong piece was clicked
            else:
                if len(available_jumps) == 0:
                    moves = board.moves(x, y) 
                    board.color_moves(moves)
                else:
                    if (x, y) in available_jumps:
                        moves = available_jumps[(x, y)]    
                        board.color_moves(moves)
                    else:
                        return None # There are available jumps but wrong piece was clicked
            return {'coords': (x, y), 'moves': moves, 'init_coords': (x, y), 'jumped_pieces': []}
        else: # Player didn't click on a piece
            return None
    else:
        if board.is_piece(x, y) and len(piece_clicked['jumped_pieces']) == 0: # User hasn't jumped any pieces in current turn
            if piece_clicked['coords'][0] == x and piece_clicked['coords'][1] == y: # Piece unclicked
                board.color_board()
                return None        
            elif board.is_piece(x, y) and board.board_pieces[y][x].is_own_piece(): # Users changes to another one of their own pieces
                return turn(x, y, None) 
            else: # User clicked opponent pawn                
                board.color_board()
                return None
        elif board.is_piece(x, y) == False:
            if board.is_king(*piece_clicked['coords']):
                if len(available_king_jumps) == 0:
                    if (x, y) in piece_clicked['moves']: # Valid move
                        board.color_board()
                        board.move_piece(*piece_clicked['coords'], x, y)
                        network.send_data((*flip_pos(*piece_clicked['coords']), *flip_pos(x, y)))
                        own_turn = False
                        return None
                    else: # Invalid move
                        board.color_moves(piece_clicked['moves'])
                        return piece_clicked
                else: # Player can jump piece
                    if (x, y) in available_king_jumps[piece_clicked['coords']]: 
                        x_jumped = (piece_clicked['coords'][0] + x) / 2
                        y_jumped = (piece_clicked['coords'][1] + y) / 2 
                        board.jump_piece([[int(x_jumped), int(y_jumped)]])

                        piece_clicked['jumped_pieces'].append([int(x_jumped),int(y_jumped)])
                        board.move_piece(*piece_clicked['coords'], x, y)
                        
                        available_king_jumps = board.available_king_jumps()
                        if (x, y) in available_king_jumps:
                            piece_clicked['coords'] = (x, y)
                            piece_clicked['moves'] = available_king_jumps[(x, y)]
                            board.color_moves(piece_clicked['moves'])
                            return piece_clicked # Returns piece to see if any more jumps can be made
                        else:
                            network.send_data((*flip_pos(*piece_clicked['init_coords']),
                                *flip_pos(x, y), flip_pos_list(piece_clicked['jumped_pieces'])))
                            own_turn = False
                            return None
                    else: # Nothing happens because the user must jump
                        board.color_moves(piece_clicked['moves'])
                        return piece_clicked
            else:
                if len(available_jumps) == 0:
                    if (x, y) in piece_clicked['moves']: # Valid move
                        board.color_board()
                        board.move_piece(*piece_clicked['coords'], x, y)
                        network.send_data((*flip_pos(*piece_clicked['coords']), *flip_pos(x, y)))
                        own_turn = False
                        return None
                    else: # Invalid move
                        board.color_moves(piece_clicked['moves'])
                        return piece_clicked
                else: # Player can jump piece
                    if (x, y) in available_jumps[piece_clicked['coords']]: 
                        x_jumped = (piece_clicked['coords'][0] + x) / 2
                        y_jumped = (piece_clicked['coords'][1] + y) / 2
                        board.jump_piece([[int(x_jumped), int(y_jumped)]]) # Piece being jumped

                        piece_clicked['jumped_pieces'].append([int(x_jumped),int(y_jumped)])
                        board.move_piece(*piece_clicked['coords'], x, y)

                        available_jumps = board.available_jumps()
                        if (x, y) in available_jumps:
                            piece_clicked['coords'] = (x, y)
                            piece_clicked['moves'] = available_jumps[(x, y)]
                            board.color_moves(piece_clicked['moves'])
                            return piece_clicked # Returns piece to see if any more jumps can be made
                        else:
                            network.send_data((*flip_pos(*piece_clicked['init_coords']),
                                *flip_pos(x, y), flip_pos_list(piece_clicked['jumped_pieces'])))
                            own_turn = False
                            return None
                    else: # Nothing happens because the user must jump
                        board.color_moves(piece_clicked['moves'])
                        return piece_clicked

        else: # User hasn't moved
            board.color_moves(piece_clicked['moves'])
            return piece_clicked

def main():
    global board, own_turn
    running = True
    piece_clicked = None

    while running:        
        if board.num_own_pieces == 0: # Opponent win
            running = False
            print("You Lose!")
        elif board.num_opp_pieces == 0: # Player win
            running = False
            print("You Win!")

        board.draw_board(WINDOW)
        board.draw_pieces(WINDOW)
        pygame.display.update()

        if own_turn == False:
            data_recv = network.recieve_data()
            
            if data_recv is not None and len(data_recv) > 0:
                board.move_piece(data_recv[0], data_recv[1], data_recv[2], data_recv[3])
                if len(data_recv) > 4:
                    board.jump_piece(data_recv[4])
                own_turn = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                network.disconnect_server()
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if own_turn == True:
                    pos = pygame.mouse.get_pos()
                    x, y =  clicked_pos(pos)
                    piece_clicked = turn(x, y, piece_clicked)

    network.disconnect_server()
    pygame.quit()
    quit()

if __name__ == '__main__':    
    WINDOW = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption('Online Checkers Game')

    network = Network(argv)
    own_turn = network.connect_server()
    
    if own_turn == False:
        board = Board(1)
    elif own_turn:
        board = Board(2)

    main()