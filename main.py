import numpy as np
import random
from game_logic import *

board = np.array([['','',''],['','',''],['','','']])
count = 9
computer = ""
player = input("Enter your choice(X or O)")

if(player == 'X'):
  computer = 'O'
  while(count>0):
    board[0]
    player_play(board)
    count-=1
    if(outcome_pos(board)): break;
    computer_play(board)
    count-=1
    if(outcome_pos(board)): break;

if(player == 'O'):
  computer = 'X'
  while(count>0):
    computer_play(board)
    count-=1
    if(outcome_pos(board)): break;
    player_play(board)
    count-=1
    if(outcome_pos(board)): break;

if(not(outcome_pos(board))):
  print("Tie match")

print(board)     