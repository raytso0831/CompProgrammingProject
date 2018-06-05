#Ray Tso
#5/23/18
#battleship.py
from random import randint
from ggame import *

def redrawall():
    RADIUS=33
    red=Color(0xFF0000,1)
    white=Color(0xFFFFFF,1)
    black=Color(0x000000,1)
    green=Color(0x00FC00,1)

    blackOutline=LineStyle(1, black)
    whiteRectangle=RectangleAsset(75,75,blackOutline,white)
    redCircle=CircleAsset(35,blackOutline,red)
    greenCircle=CircleAsset(35,blackOutline,green)
    for r in range(0,5):
        for c in range(0,5):
            Sprite(whiteRectangle,((2*RADIUS+10)*c,(2*RADIUS+10)*r))
            if data['player'][r][c]=='ship':
                Sprite(greenCircle,((2*RADIUS+10)*c,(2*RADIUS+10)*r))
            elif data['player'][r][c]=='hit':
                Sprite(redCircle,(500+(2*RADIUS+10)*c,(2*RADIUS+10)*r))
    
    for r in range(0,5):
        for c in range(0,5):
            Sprite(whiteRectangle,(500+(2*RADIUS+10)*r,(2*RADIUS+10)*c))
            if data['computer'][r][c]=='ship':
                Sprite(greenCircle,(500+(2*RADIUS+10)*c,(2*RADIUS+10)*r))
            elif data['computer'][r][c]=='hit':
                Sprite(redCircle,(500+(2*RADIUS+10)*c,(2*RADIUS+10)*r))


def mouseClick(event):
     print(event.x//75,event.y//75)
     if data['ships_placed']<3:
         data['player'][event.y//75][event.x//75]='ship'
         data['ships_placed']+=1
     else:
         if data['computer'][event.y//75][(event.x-500)//75]=='ship':
             data['computer'][event.y//75][(event.x-500)//75]='hit'
         else:
             data['computer'][event.y//75][(event.x-500)//75]='miss'
             
     redrawall()
     
    
def pickComputerShips():
    while data['computer_ships']<3:
        col=randint(0,4)
        row=randint(0,4)
        data['computer'][row][col]='ship'
        data['computer_ships']+=1
        redrawall()
        

def buildBoard():
    board=[['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]
    return board

if __name__ == '__main__':
    data={}
    data['player']=buildBoard()
    data['computer']=buildBoard()
    data['ships_placed']=0
    data['computer_ships']=0
    redrawall()
    App().listenMouseEvent('click',mouseClick)
    App().run()
    pickComputerShips()
























'''
from ggame import *
 #graphics
white=Color(0xFFFFFF,1)
black=Color(0x000000,1)
    

blackOutline=LineStyle(1, black)
whiteRectangle=RectangleAsset(75,75,blackOutline,white) 
whiteRectangle2=RectangleAsset(75,75,blackOutline,white) 
whiteRectangle3=RectangleAsset(75,75,blackOutline,white) 
whiteRectangle4=RectangleAsset(75,75,blackOutline,white) 
whiteRectangle5=RectangleAsset(75,75,blackOutline,white) 
whiteRectangle6=RectangleAsset(75,75,blackOutline,white) 
whiteRectangle7=RectangleAsset(75,75,blackOutline,white) 
whiteRectangle8=RectangleAsset(75,75,blackOutline,white) 
whiteRectangle9=RectangleAsset(75,75,blackOutline,white) 
    
Sprite(whiteRectangle,(0,0))
Sprite(whiteRectangle2,(75,0))
Sprite(whiteRectangle3,(150,0))
Sprite(whiteRectangle4,(225,0))
Sprite(whiteRectangle5,(300,0))
Sprite(whiteRectangle6,(300,150))
Sprite(whiteRectangle7,(0,300))
Sprite(whiteRectangle8,(150,300))
Sprite(whiteRectangle9,(300,300))
    
    
App().run()
'''