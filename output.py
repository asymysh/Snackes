import random
import time
import datetime as dt
import os
from copy import deepcopy
from turtle import update

time_diff = 1
Speed = 10                   #Temp
SpeedIterator = 0
BoxArr = []
score = 0                   #InitialScore
BoxTemp = []
FruitPos = [1,1]            # InitialPosition
SnakeHead = []
SnakeHead.append([1,1])   # InitialPosition
SnakeTail = []
SnakeDir = [+1,0]           #InitialDirection
# SnakeDir = {2:"up", 8: "down", 4: "left", 6: "right"}

for i in range(16):
  for j in range(16):
    BoxTemp.append("·")
  BoxArr.append(BoxTemp.copy())
  BoxTemp.clear()

for i in range(16):
  for j in range(16):
    BoxArr[0][j]= "■"
    BoxArr[j][0]= "■"
    BoxArr[15][j]= "■"
    BoxArr[j][15]= "■"

def printBox():

    for i in range(16):
        for j in range(16):
            print(BoxArr[i][j], end="   ")
        print("")
        print("")
    print(f' Your Score is {score}')
    print(f'Frames: {SpeedIterator}  RunTime: {time_diff:.2f} FPS: {SpeedIterator/time_diff}')
    print(SnakeTail)

def updateScore():
    global score
    score = score + 1 

def DidIEat():
    if(SnakeHead[0][0] == FruitPos[0] and SnakeHead[0][1] == FruitPos[1]):
        updateScore()
        getFruit()
        SnakeTail.insert(0, deepcopy(SnakeHead))


def getFruit():

  BoxArr[FruitPos[0]][FruitPos[1]] = "·"
  posx = random.randint(1,14)
  posy = random.randint(1,14)
  if (posx == FruitPos[0] or posy == FruitPos[1]):
    getFruit()
  FruitPos[0] = posx
  FruitPos[1] = posy
  BoxArr[FruitPos[0]][FruitPos[1]] = "O"

def getDirn():
    with open('keystroke') as file:
        i = 0
        for lines in file:
            SnakeDir[i] = int(lines)
            i+=1  

def getSnake():

    getDirn()
    BoxArr[SnakeHead[0][0]][SnakeHead[0][1]] = "·"
        

    SnakeHead[0][0] += SnakeDir[0]
    SnakeHead[0][1] += SnakeDir[1]
    if(SnakeHead[0][0] > 14 ):
      SnakeHead[0][0] = 1
    if(SnakeHead[0][0] < 1 ):
      SnakeHead[0][0] = 14
    if(SnakeHead[0][1] > 14 ):
      SnakeHead[0][1] = 1
    if(SnakeHead[0][1] < 1 ):
      SnakeHead[0][1] = 14

    BoxArr[SnakeHead[0][0]][SnakeHead[0][1]] = "X"
        



# -----------------------MAIN PROGRAM ------------------------------------

getFruit()      #Initialise Fruit Position


start_time = dt.datetime.today().timestamp()
while(True):
    SpeedIterator+=1
    if(SpeedIterator% (Speed) == 0):
        getSnake()
        DidIEat()
    printBox()
    time.sleep(0.005)
    time_diff = dt.datetime.today().timestamp() - start_time
    os.system('cls')
        


