
from pathlib import Path
from chessy.config import FIGURES_DIR, PROCESSED_DATA_DIR
import chess 

def show_board(fen): ## ADD VOICE OVER !
    if fen != None :
        print(chess.Board(fen))
    else: 
         print(chess.Board())
