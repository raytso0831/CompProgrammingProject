#Ray Tso
#4/4/18
#TicTacToe.py

from ggame import *
def mouseClick(event):
    print(event.x,event.y)
    X=TextAsset('X',fill=black,style='bold 120pt Times')#
    O=TextAsset('O',fill=black,style='bold 120pt Times')#


    if event.x<=150 and event.y<=150:
        Sprite(X)
    elif event.x<=300 and event.y<=150:
        Sprite(X)
    elif event.x<=450 and event.y<=150:
        Sprite(X)
    elif event.x<=150 and event.y<=300:
        Sprite(X)
    elif event.x<=300 and event.y<=300:
        Sprite(X)
    elif event.x<=450 and event.y<=300:
        Sprite(X)
    elif event.x<=150 and event.y<=450:
        Sprite(X)
    elif event.x<=300 and event.y<=450:
        Sprite(X)
    else:
        Sprite(X)

def isEmpty (): 
    if 'X' not in whiteRectangle or 'O' not in whiteRectangle:
        return True
    if 'X' not in whiteRectangle or 'O' not in whiteRectangle2:
        return True
    if 'X' not in whiteRectangle or 'O' not in whiteRectangle3:
        return True
    if 'X' not in whiteRectangle or 'O' not in whiteRectangle4:
        return True
    if 'X' not in whiteRectangle or 'O' not in whiteRectangle5:
        return True
    if 'X' not in whiteRectangle or 'O' not in whiteRectangle6:
        return True
    if 'X' not in whiteRectangle or 'O' not in whiteRectangle7:
        return True
    if 'X' not in whiteRectangle or 'O' not in whiteRectangle8:
        return True
    if 'X' not in whiteRectangle or 'O' not in whiteRectangle9:
        return True

    else:
        return False
        
        
    

white=Color(0xFFFFFF,1)
black=Color(0x000000,1)
blackOutline=LineStyle(1, black)
whiteRectangle=RectangleAsset(150,150,blackOutline,white) 
whiteRectangle2=RectangleAsset(150,150,blackOutline,white) 
whiteRectangle3=RectangleAsset(150,150,blackOutline,white) 
whiteRectangle4=RectangleAsset(150,150,blackOutline,white) 
whiteRectangle5=RectangleAsset(150,150,blackOutline,white) 
whiteRectangle6=RectangleAsset(150,150,blackOutline,white) 
whiteRectangle7=RectangleAsset(150,150,blackOutline,white) 
whiteRectangle8=RectangleAsset(150,150,blackOutline,white) 
whiteRectangle9=RectangleAsset(150,150,blackOutline,white) 


Sprite(whiteRectangle,(0,0))
Sprite(whiteRectangle2,(150,0))
Sprite(whiteRectangle3,(300,0))
Sprite(whiteRectangle4,(0,150))
Sprite(whiteRectangle5,(150,150))
Sprite(whiteRectangle6,(300,150))
Sprite(whiteRectangle7,(0,300))
Sprite(whiteRectangle8,(150,300))
Sprite(whiteRectangle9,(300,300))


App().listenMouseEvent('click',mouseClick)
App().run()

