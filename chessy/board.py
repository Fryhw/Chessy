from pathlib import Path
# from chessy.config import FIGURES_DIR, PROCESSED_DATA_DIR
import chess 
import os

def return_board_fen(fen = None): ## ADD VOICE OVER !
    if fen != None :
        print(chess.Board(fen))
    else: 
         print(chess.Board())

def show_board(board): ## ADD VOICE OVER !
    if board != None :
        print(board)
    else: 
         print(board)


#take in fen + move => return board updated and error otherwise
    
def play_move(board, move):
    if move is None:
        return "missing move"
    if board is None:
        board = chess.Board()
    
    try:
        move_obj = chess.Move.from_uci(move)
    except ValueError:
        return f"Coup invalide : {move}"
    
    if move_obj not in board.legal_moves:
        return f"Coup illégal : {move}"

    board.push(move_obj)
    return board

def save_board_fen(board, name):
    if board is not None and name:
        save_dir = "../saves"
        os.makedirs(save_dir, exist_ok=True) 

        fen = board.fen()
        filepath = os.path.join(save_dir, f"{name}.fen")

        with open(filepath, "w") as f:
            f.write(fen)

        print(f"FEN saved as {name}.fen")
    else:
        print(" Missing board or name.")


def load_board_fen(name):   ## ADD VOICE OVER ! 
    save_dir = "../saves"
    name = f"{name}.fen"
    filepath = os.path.join(save_dir, name)
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            fen = f.read().strip()
        board = chess.Board(fen)
        print(f"Loaded board from {filepath}")
        return board
    else:
        print(f"File {filepath} not found.")
        return None

