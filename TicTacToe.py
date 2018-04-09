#Ray Tso
#4/4/18
#TicTacToe.py

from ggame import *
def mouseClick(event):
    print(event.x,event.y)
    X=TextAsset('X',fill=black,style='bold 120pt Times')#
    O=TextAsset('O',fill=black,style='bold 120pt Times')#


    if event.x<=150 and event.y<=150:
        Sprite(X,(0,0))
    elif event.x<=300 and event.y<=150:
        Sprite(X,(150,0))
    elif event.x<=450 and event.y<=150:
        Sprite(X,(300,0))
    elif event.x<=150 and event.y<=300:
        Sprite(X,(0,150))
    elif event.x<=300 and event.y<=300:
        Sprite(X,(150,150))
    elif event.x<=450 and event.y<=300:
        Sprite(X,(300,150))
    elif event.x<=150 and event.y<=450:
        Sprite(X,(0,300))
    elif event.x<=300 and event.y<=450:
        Sprite(X,(150,300))
    else:
        Sprite(X,(300,300))
'''
def isEmpty ():
    '''


if __name__ == '__main__':
    square1=
    square2=
    square3=
    square4=
    square5=
    square6=
    square7=
    square8=
    square9=

    

        
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