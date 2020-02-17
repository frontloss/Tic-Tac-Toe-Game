def player_play(arr):
  i,j = map(int,input("Enter the (i,j) value to play your turn:").split(" "))
  if(count==0):
    return()
  else: 
    if(arr[i][j]==''):
      arr[i][j] = player
      print(board)
    else:
      print(str(i)+","+str(j) + " already filled")
      player_play(arr) 

def outcome_pos(arr):
  flag = False
  computer_win = np.array([computer,computer,computer])
  player_win = np.array([player,player,player])
  opp_diagonal = np.array([arr[0][2],arr[1][1],arr[2][0]])
  for i in range(3): 
   if(all(arr[i]==computer_win) or all(arr[:,i]==computer_win)):
     print("Computer Wins")
     flag = True
   if(all(arr[i]==player_win) or all(arr[:,i]==player_win)):
     print("Player Wins")
     flag = True
  if(all(np.diagonal(arr)==computer_win) or all(opp_diagonal==computer_win)):
     print("Computer Wins")
     flag = True
  if(all(np.diagonal(arr)==player_win) or all(opp_diagonal==player_win)):
     print("Player Wins")
     flag = True
  return flag

def computer_play(arr):
  computer_gamepoint = [np.array([computer,computer,'']),np.array([computer,'',computer]),np.array(['',computer,computer])]
  opp_diagonal = np.array([arr[0][2],arr[1][1],arr[2][0]]) 
  for i in range(3):
    for game in computer_gamepoint:
      if(all(arr[i] == game)):
        arr[i] = np.where(arr[i]=='',computer,arr[i])
        j = list(arr[i]).index(computer)
        print("Computer plays: "+str(i)+","+str(j))
        print(board)
        return()
      if(all(arr[:,i] == game)):
        arr[:,i] = np.where(arr[:,i]=='',computer,arr[:,i])
        j = list(arr[:,i]).index(computer)
        print("Computer plays: "+str(j)+","+str(i))
        print(board) 
        return()
      if(all(opp_diagonal == game) and arr[i][2-i]==''):
        arr[i][2-i] = computer
        print("Computer plays: "+str(i)+","+str(2-i))
        print(board)
        return()
      if(all(np.diagonal(arr) == game) and arr[i][i]==''):
        arr[i][i] = computer
        print("Computer plays: "+str(i)+","+str(i))
        print(board)
        return() 

  player_gamepoint = [np.array([player,player,'']),np.array([player,'',player]),np.array(['',player,player])]
  for i in range(3):
    for game in player_gamepoint:
      if(all(arr[i] == game)):
        arr[i] = np.where(arr[i]=='',computer,arr[i])
        j = list(arr[i]).index(computer)
        print("Computer plays: "+str(i)+","+str(j))
        print(board)
        return()
      if(all(arr[:,i] == game)):
        arr[:,i] = np.where(arr[:,i]=='',computer,arr[:,i])
        j = list(arr[:,i]).index(computer)
        print("Computer plays: "+str(j)+","+str(i))
        print(board) 
        return()

  i,j = random.randint(0,2),random.randint(0,2)
  if(arr[i][j]==''):
      arr[i][j] = computer
      print("Computer plays : " +str(i)+","+str(j))
      print(board)
  else:
      print(str(i)+","+str(j) + " already filled")
      computer_play(arr)