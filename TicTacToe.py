#Ray Tso
#4/4/18
#TicTacToe.py

from ggame import *
def mouseClick(event):
    print(event.x,event.y)
    X=TextAsset('X',fill=black,style='bold 120pt Times')#


    if event.x<=150 and event.y<=150:
        Sprite(X,(0,0))
        data['square'] = X
        Computerturn()

    elif event.x<=300 and event.y<=150:
        Sprite(X,(150,0))
        data['square2'] = X
        Computerturn()

    elif event.x<=450 and event.y<=150:
        Sprite(X,(300,0))
        data['square3'] = X
        Computerturn()

    elif event.x<=150 and event.y<=300:
        Sprite(X,(0,150))
        data['square4'] = X
        Computerturn()

    elif event.x<=300 and event.y<=300:
        Sprite(X,(150,150))
        data['square5'] = X
        Computerturn()

    elif event.x<=450 and event.y<=300:
        Sprite(X,(300,150))
        data['square6'] = X
        Computerturn()

    elif event.x<=150 and event.y<=450:
        Sprite(X,(0,300))
        data['square7'] = X
        Computerturn()

    elif event.x<=300 and event.y<=450:
        Sprite(X,(150,300))
        data['square8'] = X
        Computerturn()

    else:
        Sprite(X,(300,300))
        data['square9'] = X
        Computerturn()

'''
def isEmpty ():
'''
    
def Computerturn():
    from random import randint
    comp_num=randint(1,9)
    O=TextAsset('O',fill=black,style='bold 120pt Times')#

    
    if comp_num==1:
        Sprite(O,(0,0))
        data['square'] = O

    elif comp_num==2:
        Sprite(O,(150,0))
        data['square'] = O

    elif comp_num==3:
        Sprite(O,(300,0))
        data['square'] = O

    elif comp_num==4:
        Sprite(O,(0,150))
        data['square'] = O

    elif comp_num==5:
        Sprite(O,(150,150))
        data['square'] = O

    elif comp_num==6:
        Sprite(O,(300,150))
        data['square'] = O

    elif comp_num==7:
        Sprite(O,(0,300))
        data['square'] =O

    elif comp_num==8:
        Sprite(O,(150,300))
        data['square'] = O

    elif comp_num==9:
        Sprite(O,(300,300))
        data['square'] = O



if __name__ == '__main__':
    data = {}
    data['square'] = ''
    data['square2'] = ''
    data['square3'] = ''
    data['square4'] = ''
    data['square5'] = ''
    data['square6'] = ''
    data['square7'] = ''
    data['square8'] = ''
    data['square9'] = ''
    
   
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