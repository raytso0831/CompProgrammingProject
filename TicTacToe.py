#Ray Tso
#4/4/18
#TicTacToe.py

from ggame import *
def mouseClick(event):
    print(event.x,event.y)

    if event.x<=150 and event.y<=150:
        print('X')
    

'''def isEmpty (): 
    if 'X' not in whiteRectangle or if 'O' not in whiteRectangle:
        return True
    else:
        return False'''
        
        
    

white=Color(0xFFFFFF,1)
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

