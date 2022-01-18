import shogi.KIF
import shogi
import shutil
import time
  
# ts stores the time in seconds
ts = str(time.time()).replace('.',"")

kif=shogi.KIF.Parser.parse_file('partie_01.kif')[0]
board = shogi.Board(kif["sfen"])
shutil.copy('partie_01.kif', 'old/'+ts+'_partie_01.kif')
print(board)
print("\n")
print(shogi.Move(shogi.B2, shogi.B3).usi())
print("\n")
print(shogi.Move.from_usi('8g8f') in board.legal_moves)
print("\n")
print(board.legal_moves)
board.push_usi('8g8f')
print(board)
print("\n")
print(board.kif_str())