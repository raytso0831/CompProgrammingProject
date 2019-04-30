#Ray Tso
#5/23/18
#battleship.py

#These are imports used.
from random import randint
from ggame import *

red=Color(0xFF0000,1)
white=Color(0xFFFFFF,1)
black=Color(0x000000,1)
green=Color(0x00FC00,1)


# This function will draws the player board and computer board.
def redrawall():
    RADIUS=33
    #graphics for colors
    #graphics for the board
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

#This function should figure out what row and column the user clicked on

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
     
# The function should have the computer pick a random spot to guess and process the guess if it is a valid move. 
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

# This function will select a random number and then places it on a board without being allowed to place two ships on top of each other
def pickComputerShips():
    while data['computer_ships']<3:
        col=randint(0,4)
        row=randint(0,4)
        if data['computer'][row][col]!='ship':
            data['computer_ships']+=1
            data['computer'][row][col]='ship'
    redrawall()

#This function return True if the user or the computer won and False otherwise.
def winner():
    computer_winner=TextAsset('Computer Wins!!! ',fill=black,style='bold 40pt Arial')
    user_winner=TextAsset('YOU WIN!!!!!',fill=black,style='bold 40pt Arial')
    if data['computer_ships_sunk']==3:
        Sprite(user_winner,(500,400))
    else:
        Sprite(computer_winner,(500,400))
    data['Game Over']=True
        
#Creates a 5x5 empty matrix and returns it.
def buildBoard():
    board=[['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]
    return board



#This will store all of the code and will setup the game
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
    
    
























