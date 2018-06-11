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
    blackX=TextAsset('X',fill=black,style='bold 60pt Arial')
    for r in range(0,5):
        for c in range(0,5):
            Sprite(whiteRectangle,((2*RADIUS+10)*c,(2*RADIUS+10)*r))
            if data['player'][r][c]=='ship':
                Sprite(greenCircle,((2*RADIUS+10)*c,(2*RADIUS+10)*r))
            elif data['player'][r][c]=='hit':
                Sprite(redCircle,((2*RADIUS+10)*c,(2*RADIUS+10)*r))
            elif data['player'][r][c]=='miss':
                Sprite(blackX,((2*RADIUS+10)*c,(2*RADIUS+10)*r))
                
    
    for r in range(0,5):
        for c in range(0,5):
            Sprite(whiteRectangle,(500+(2*RADIUS+10)*c,(2*RADIUS+10)*r))
            if data['computer'][r][c]=='hit':
                Sprite(redCircle,(500+(2*RADIUS+10)*c,(2*RADIUS+10)*r))
            elif data['computer'][r][c]=='miss':
                Sprite(blackX,(500+(2*RADIUS+10)*c,(2*RADIUS+10)*r))
    if data['computer_ships_sunk']==3 or data['ships_sunk']==3:
    
     winner()

def mouseClick(event):
    if data['Game Over']==False:
        print(event.x//75,event.y//75)
        if data['ships_placed']<3:
            if data['player'][event.y//75][event.x//75]!='ship':
                data['ships_placed']+=1
                data['player'][event.y//75][event.x//75]='ship'
        else:
            if data['computer'][event.y//75][(event.x-500)//75]=='ship':
                data['computer'][event.y//75][(event.x-500)//75]='hit'
                data['computer_ships_sunk']+=1
                computerTurn()
    
            elif data['computer'][event.y//75][(event.x-500)//75]=='':
                 data['computer'][event.y//75][(event.x-500)//75]='miss'
                 computerTurn()
        redrawall()
     
def computerTurn():
    col=randint(0,4)
    row=randint(0,4)
    if data['player'][row][col]=='ship':
        data['player'][row][col]='hit'
        data['ships_sunk']+=1
    elif data['player'][row][col]=='':
        data['player'][row][col]='miss'
    else:
        computerTurn()

def pickComputerShips():
    while data['computer_ships']<3:
        col=randint(0,4)
        row=randint(0,4)
        if data['computer'][row][col]!='ship':
            data['computer_ships']+=1
            data['computer'][row][col]='ship'
    redrawall()

def winner():
    computer_winner=TextAsset('Computer Wins!!! Better luck next time :(',fill=black,style='bold 40pt Arial')
    user_winner=TextAsset('YOU WIN!!!!! XD',fill=black,style='bold 40pt Arial')
    if data['computer_ships_sunk']==3:
        Sprite(user_winner,(500,100))
    else:
        Sprite(computer_winner,(500,100))
    data['Game Over']=True
        

def buildBoard():
    board=[['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]
    return board

if __name__ == '__main__':
    data={}
    data['player']=buildBoard()
    data['computer']=buildBoard()
    data['ships_sunk']=0
    data['computer_ships_sunk']=0
    data['ships_placed']=0
    data['computer_ships']=0
    data['Game Over']=False
    pickComputerShips()    
    App().listenMouseEvent('click',mouseClick)
    App().run()
    
    
























