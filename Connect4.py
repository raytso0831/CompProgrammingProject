#Ray Tso
#4/26/19
#Connect4.py

from random import randint
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
    for r in range(0,6):
            for c in range(0,7):
                Sprite(blueRectangle,((2*RADIUS+10)*c,(2*RADIUS+10)*r))
                if data[r][c]=='player':
                    Sprite(redCircle,((2*RADIUS+10)*c,(2*RADIUS+10)*r))
                elif data[r][c]=='computer':
                    Sprite(yellowCircle,((2*RADIUS+10)*c,(2*RADIUS+10)*r))

def mouseClick(event):
    if data['Game Over']==False:
        print(event.x//75,event.y//75)

    
    
    
def buildBoard():
    board=[['','','','','','player','computer'],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','','']]
    return board


if __name__ == '__main__':
    data={}
    data=buildBoard()
    redrawall()
    App().run()
    App().listenMouseEvent('click',mouseClick)
    data['Game Over']=False

    
    
    
    
    
    
    
    
    
