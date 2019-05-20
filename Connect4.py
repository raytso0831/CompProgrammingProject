#Ray Tso
#4/26/19
#Connect4.py

from random import randint
from time import time
from ggame import *

RADIUS=33
red=Color(0xFF0000,1)
white=Color(0xFFFFFF,1)
black=Color(0x000000,1)
yellow=Color(0xFFF033,1)
blue= Color(0x33E0FF,1)
blackOutline=LineStyle(1, black)
blueOutline=LineStyle(1, blue)
blueRectangle=RectangleAsset(75,75,blueOutline,white)
redCircle=CircleAsset(35,blackOutline,red)
yellowCircle=CircleAsset(35,blackOutline,yellow)


def redrawall():
    for x in range(0,6):
        for y in range(0,7):
            Sprite(blueRectangle,((2*RADIUS+10)*y,(2*RADIUS+10)*x))
            if data['board'][x][y]=='player':
                Sprite(redCircle,((2*RADIUS+10)*y,(2*RADIUS+10)*x))
            elif data['board'][x][y]=='computer':
                Sprite(yellowCircle,((2*RADIUS+10)*y,(2*RADIUS+10)*x))

def mouseClick(event):
    y=5
    x = int(event.x)
    if data['Game Over']==False and data['click'] == False:
        data['click'] = True
        data['clicktime'] = time()
        print(x//75)
        if data['board'][0][x//75] == '':
            while data['board'][y][x//75]!='':
                y=y-1
            #data['player'][event.y//75][event.x//75]='ship'
            data['board'][y][x//75]='player'
    winner()
    redrawall()

def computer_put_token():
    y=5
    col=randint(0,6)
    data['click'] = True
    data['clicktime'] = time()
    if data['Game Over']==False:
        if data['board'][0][col] == '':
            while data['board'][y][col]!='':
                y=y-1
            data['board'][y][col]='computer'
    winner()
    redrawall()
    
    
def step():
    delay = 1
    if data['click'] and time() > data['clicktime'] + delay:
        computer_put_token()
        data['click'] = False
        
def check_row_for_winner():
    for y in range(7):
        currplayer = None
        count = 0
        for x in range(6):
            if data['board'][x][y]==currplayer:
                count += 1
                if count == 4 and currplayer!='':
                    return currplayer
            else:
                count = 1
                currplayer = data['board'][x][y]
    return ''
    
def winner():
    computer_winner=TextAsset('Computer Wins!!! ',fill=black,style='bold 40pt Arial')
    user_winner=TextAsset('YOU WIN!!!!!',fill=black,style='bold 40pt Arial')
    if check_row_for_winner() == 'player':
        Sprite(user_winner,(750,750))
        data['Game Over']=True
    elif check_row_for_winner() == 'computer':
        Sprite(computer_winner,(7500,750))
        data['Game Over']=True

    
def buildBoard():
    board=[['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','','']]
    return board


if __name__ == '__main__':
    data={}
    data['board']=buildBoard()
    data['click']=False
    redrawall()
    data['tokens_placed']=0
    App().run(step)
    App().listenMouseEvent('click',mouseClick)
    data['Game Over']=False
    
    
    
    
