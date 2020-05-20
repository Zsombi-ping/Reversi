import os
import sys
import numpy as np
import math
import multiprocessing
import time
import signal


table = np.zeros((8, 8), dtype=int)

player = 1
maxLevel = 3
computer = 2
round = 1
waiting_time = 5
position = (0,0)

step_row = [-1,-1,0,1,1,1,0,-1]
step_col = [0,1,1,1,0,-1,-1,-1]



#def handler(signum, frame):
    #print('Varakozasi ido veget ert', signum)
    #raise OSError("Couldn't open device!")

def print_table():

    for i in range (8):
        print(str(i) + " ", end = '')
        print(table[i])
    print("   ",end = '')
    for i in range(8):
        print (str(i) + " " , end = '')
    print("\n")


def tick():
    for i in range (20):
        print(i)
        time.sleep(1)


def initialize_table():

    table[int(8/2-1)][int(8/2-1)] = 1
    table[int(8/2-1)][int(8/2)] = 2
    table[int(8/2)][int(8/2-1)] = 2
    table[int(8/2)][int(8/2)] = 1
    print_table()



def heuristic():

    count_player = 0
    count_computer = 0
    
    for i in range(8):
        for j in range(8):
            if table[i][j] == 1:
                count_player+=1
            elif table[i][j] == 2:
                count_computer+=1
    
    if table[0][0] == 2:
        count_computer +=2
    elif table[0][0] == 1:
        count_player +=2
    if table[0][7] == 2:
        count_computer +=2
    elif table[0][7] == 1:
        count_player +=2
    if table[7][0] == 2:
        count_computer +=2
    elif table[7][0] == 1:
        count_player +=2
    if table[7][7] == 2:
        count_computer +=2
    elif table[7][7] == 1:
        count_player +=2

    if count_computer == count_player:
        return 0
    else:
        return (count_computer - count_player) 

def isfull ():

    count_empty_fields = 0

    for i in range(8):
        for j in range(8):
            if table[i][j] == 0:
                count_empty_fields +=1

    return (count_empty_fields == 0)

def legalmove(row,col,who):

    legal_x = []
    legal_y = []
    step_size = []

    if who == computer:
        enemy = player
    else:
        enemy = computer
    
    for i in range(8):
        if table[row][col] == 0:
            if (row + step_row[i]) >=0 and (col + step_col[i]) >=0 and (row + step_row[i]) <8 and (col + step_col[i]) < 8:
                if table[row + step_row[i]][col + step_col[i]] == enemy:
                    cons = 1
                    while (row + cons*step_row[i]) >=0 and (row + cons*step_row[i]) <8 and (col + cons*step_col[i]) >=0 and (col + cons*step_col[i]) <8 and table[row + cons*step_row[i]][col + cons*step_col[i]] == enemy:
                        cons +=1
                    if  (row + cons*step_row[i]) >=0 and (row + cons*step_row[i]) <8 and (col + cons*step_col[i]) >=0 and (col + cons*step_col[i]) <8 and table[row + cons*step_row[i]][col + cons*step_col[i]] == who:
                        legal_x.append(step_row[i])
                        legal_y.append(step_col[i])
                        step_size.append(cons)
    
   
    return (legal_x,legal_y,step_size)


                

def step_decision():

    value_chosen = -math.inf
    time.sleep(1)
    for i in range(8):
        for j in range(8):
            valid_x,valid_y,STEPS = legalmove(i,j,computer)
            if len(STEPS) > 0:
                for k in range(len(STEPS)):
                    for flip in range(STEPS[k]):
                        table[i + flip*valid_x[k]][j + flip*valid_y[k]] = computer
                value = alpha_beta(table,0,False,-math.inf,math.inf)
                for k in range(len(STEPS)):    
                    for flip in range(STEPS[k]):
                        table[i + flip*valid_x[k]][j + flip*valid_y[k]] = player
                table[i][j] = 0
                if value > value_chosen:
                    value_chosen = value
                    global position
                    position = (i,j)
    valid_x,valid_y,STEPS = legalmove(position[0],position[1],computer)
    print(position[0],position[1])
    for k in range(len(STEPS)):
        for flip in range(STEPS[k]):
            table[position[0] + flip*valid_x[k]][position[1] + flip*valid_y[k]] = computer


def alpha_beta(table, level , Max_node ,alpha , beta):
  
    if level == maxLevel or isfull():
        predicted = heuristic()
        return predicted
    
    if Max_node:
        for i in range(8):
            for j in range(8):
                valid_x,valid_y,STEPS = legalmove(i,j,computer)
                if len(STEPS) > 0:
                    for k in range(len(STEPS)):
                        for flip in range(STEPS[k]):
                            table[i + flip*valid_x[k]][j + flip*valid_y[k]] = computer
                    value = alpha_beta(table, level + 1 , False, alpha , beta)
                    for k in range(len(STEPS)):    
                        for flip in range(STEPS[k]):
                            table[i + flip*valid_x[k]][j + flip*valid_y[k]] = player
                    table[i][j] = 0
                    alpha =  max(value , alpha)
                    if  alpha >= beta :
                        return alpha        
        return alpha
    else:
        for i in range(8):
            for j in range(8):
                valid_x,valid_y,STEPS = legalmove(i,j,player)
                if len(STEPS) > 0:
                    for k in range(len(STEPS)):
                        for flip in range(STEPS[k]):
                            table[i + flip*valid_x[k]][j + flip*valid_y[k]] = player
                    value = alpha_beta(table, level + 1 , True,alpha,beta)
                    for k in range(len(STEPS)):
                        for flip in range(STEPS[k]):
                            table[i + flip*valid_x[k]][j + flip*valid_y[k]] = computer
                    table[i][j] = 0
                    beta =  min(value , beta)
                    if  alpha >= beta :
                        return beta
        return beta




if __name__ == "__main__":

    rounds = input("Hany kort jatszana = ")
    rnd = int(rounds)
    difficult = input("nehezsegi szint = ")
    maxLevel = int(difficult)
    #timeW = input("Maximalis gondolkozasi ido a gepnek = ")
    #waiting_time = int(timeW)

    initialize_table()
  
    while True and rnd > 0:

        posx = input("sor: ")
        posy = input("oszlop: ")
        print("\n\n")
        valid_x,valid_y,STEPS = legalmove(int(posx),int(posy),player)
        if int(posx) >= 8 or  int(posx) < 0 or int(posy) >= 8 or int(posy) < 0:
            print("Rossz index")
            continue 
        if len(STEPS) > 0:
            for k in range(len(STEPS)):
                for flip in range(STEPS[k]):
                    table[int(posx) + flip*valid_x[k]][int(posy) + flip*valid_y[k]] = player
        else:
            print("Nem szabalyos lepes")
            continue
        print('Jatekos lepese :')
        print_table()
        print("Szamitogep lepese :")
    
        # signal.signal(signal.SIGTERM, handler)
        # signal.alarm(8)

        step_decision()
        print_table()
        rnd -=1
    final = heuristic()
    if final > 0:
        print("\n\nSzamitogep nyert")
    elif final == 0:
        print("\n\nDontetlen")
    else:
        print("\n\nOn nyert")
        

