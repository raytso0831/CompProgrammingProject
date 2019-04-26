#Ray Tso
#4/26/18
#Connect4.py

from random import randint
from ggame import *

def redrawall():

    RADIUS=33
    red=Color(0xFF0000,1)
    white=Color(0xFFFFFF,1)
    black=Color(0x000000,1)
    yellow=Color(0xFFF033,1)
    blue= Color(0x3633FF,1)
    
    blackOutline=LineStyle(1, black)
    blueRectangle=RectangleAsset(75,75,blackOutline,blue)
    redCircle=CircleAsset(35,blackOutline,red)
    yellowCircle=CircleAsset(35,blackOutline,yellow)
    for r in range(0,7):
            for c in range(0,6):
                Sprite(blueRectangle,((2*RADIUS+10)*c,(2*RADIUS+10)*r))


def buildBoard():
    board=[['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','','']]
    return board


if __name__ == '__main__':
    data={}
    App().run()