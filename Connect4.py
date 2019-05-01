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
    data['click'] = True
    data['clicktime'] = time()
    if data['Game Over']==False:
        print(event.x//75)
       
        # needs work here \/
        if data['board'][event.y//75]!= 'player':
            data['tokens_placed']+=1
            data['board'][event.x//75] = 'player'
    redrawall()

def step():
    delay = 4
    if data['click'] and time() > data['clicktime'] + delay:
        print("CLICK")
        data['click'] = False

    
def buildBoard():
    board=[['','','','','','player','computer'],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','','']]
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

    
    
    
    
    
    
    
    
    
