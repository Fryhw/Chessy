from pathlib import Path
from chessy.config import FIGURES_DIR, PROCESSED_DATA_DIR
import chess 
import os

def show_board_fen(fen): ## ADD VOICE OVER !
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
    
def play_move(fen, move): ## ADD VOICE OVER ! 
    if move is None:
        return "missing move"
    if fen is not None:
        board = chess.Board(fen)
    else:
        board = chess.Board()
        
    move_obj = chess.Move.from_uci(move)
    if move not in board.legal_moves:
        return f"Illegal move: {move}"

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

