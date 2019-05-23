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
    check_row_for_winner()


def mouseClick(event):
    if event.x>= (75*7) or event.y >= (75*6):
        return
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
    check_row_for_winner()        
    winner()
    redrawall()

def computer_put_token():
    y=5
    col=randint(0,6)
    while data['board'][0][col]!="":
        col=randint(0,6)
    data['click'] = True
    data['clicktime'] = time()
    if data['Game Over']==False:
        if data['board'][0][col] == '':
            while data['board'][y][col]!='':
                y=y-1
            data['board'][y][col]='computer'
    check_row_for_winner()
    winner()
    redrawall()
    
    
'''
def computer_put_token():
    y=5
    col=randint(0,6)
    while data['board'][0][col]!="":
        col=randint(0,6)
    data['click'] = True
    data['clicktime'] = time()
    if data['Game Over']==False:
        for col in range(6):
            if data['board'][0][col]=='':
                while data['board'][y][col]!='':
                    y=y-1
                data['board'][y][col]='computer'
                if winner()==True:
                    redrawall()
                else:
                    data['board'][y][col]=""
                    y=y-1
                data['board'][y][col]='computer'
                    
    check_row_for_winner()
    winner()
    redrawall()'''
    
    
def step():
    delay = 1
    if data['click'] and time() > data['clicktime'] + delay:
        computer_put_token()
        data['click'] = False
        
def check_row_for_winner():
    for y in range(6):
        currplayer = None
        count = 0
        for x in range(7):
            if data['board'][y][x]==currplayer:
                count += 1
                if count == 4 and currplayer!='':
                    return currplayer
            else:
                count = 1
                currplayer = data['board'][y][x]
    return ''

def check_col_for_winner():
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
    
    
def diagonal_left():
    startposition=[(0,3),(0,4),(0,5),(1,5),(2,5),(3,5)]
    for x, y in startposition:
        currplayer=None
        while y>= 0 and x<=6:
            if data['board'][y][x]==currplayer:
                count += 1
                if count == 4 and currplayer!='':
                    return currplayer
            else:
                count = 1
                currplayer = data['board'][y][x]
            x+=1
            y-=1



def diagonal_right():
    startposition=[(0,0),(0,1),(0,2),(1,0),(2,0),(3,0)]
    for x, y in startposition:
        currplayer=None
        while y<= 5 and x<=6:
            if data['board'][y][x]==currplayer:
                count += 1
                if count == 4 and currplayer!='':
                    return currplayer
            else:
                count = 1
                currplayer = data['board'][y][x]
            x+=1
            y+=1

def winner():
    computer_winner=TextAsset('Computer Wins!!! ',fill=black,style='bold 40pt Arial')
    user_winner=TextAsset('YOU WIN!!!!!',fill=black,style='bold 40pt Arial')
    if check_row_for_winner() == 'player' or check_col_for_winner()=='player'or diagonal_left() or diagonal_right()=='player':
        Sprite(user_winner,(550,200))
        data['Game Over']=True
        return True
    elif check_row_for_winner() == 'computer'or check_col_for_winner() or diagonal_left() or diagonal_right()== 'computer':
        Sprite(computer_winner,(550,200))
        data['Game Over']=True
        return True
    else:
        return False

    
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
    
    
    
