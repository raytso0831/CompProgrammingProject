#Ray Tso
#4/4/18
#TicTacToe.py

from ggame import *
def mouseClick(event):
    print(event.x,event.y)
    X=TextAsset('X',fill=black,style='bold 120pt Times')#
    TieGame=TextAsset('Its a tie',fill=black,style='bold 40pt Times')#



    if event.x<=150 and event.y<=150 and isEmpty(1) == True:
        Sprite(X,(0,0))
        data['square1'] = 'X'
        winner()
        if fullboard()==False:
            Computerturn()
        elif fullboard()== True and data['Game Over']==False:
            Sprite(TieGame,(500,250))
            

    elif 150 < event.x<=300 and event.y<=150 and isEmpty(2) == True:
        Sprite(X,(150,0))
        data['square2'] = 'X'
        winner()
        if fullboard()==False:
            Computerturn()
        elif fullboard()== True and data['Game Over']==False:
            Sprite(TieGame,(500,250))


    elif 300<event.x<=450 and event.y<=150 and isEmpty(3) == True:
        Sprite(X,(300,0))
        data['square3'] = 'X'
        winner()
        if fullboard()==False:
            Computerturn()
        elif fullboard()== True and data['Game Over']==False:
            Sprite(TieGame,(500,250))

    elif event.x<=150 and 150<event.y<=300 and isEmpty(4) == True:
        Sprite(X,(0,150))
        data['square4'] = 'X'
        winner()
        if fullboard()==False:
            Computerturn()
        elif fullboard()== True and data['Game Over']==False:
            Sprite(TieGame,(500,250))

    elif 150<event.x<=300 and 150<event.y<=300 and isEmpty(5) == True:
        Sprite(X,(150,150))
        data['square5'] = 'X'
        winner()
        if fullboard()==False:
            Computerturn()
        elif fullboard()== True and data['Game Over']==False:
            Sprite(TieGame,(500,250))

    elif 300<event.x<=450 and 150<event.y<=300 and isEmpty(6) == True:
        Sprite(X,(300,150))
        data['square6'] = 'X'
        winner()
        if fullboard()==False:
            Computerturn()
        elif fullboard()== True and data['Game Over']==False:
            Sprite(TieGame,(500,250))

    elif event.x<=150 and 300<event.y<=450 and isEmpty(7) == True:
        Sprite(X,(0,300))
        data['square7'] = 'X'
        winner()
        if fullboard()==False:
            Computerturn()
        elif fullboard()== True and data['Game Over']==False:
            Sprite(TieGame,(500,250))

    elif 150<event.x<=300 and 300<event.y<=450 and isEmpty(8) == True:
        Sprite(X,(150,300))
        data['square8'] = 'X'
        winner()
        if fullboard()==False:
            Computerturn()
        elif fullboard()== True and data['Game Over']==False:
            Sprite(TieGame,(500,250))
            
    elif 300<event.x<=450 and 300<event.y<=450 and isEmpty(9) == True:
        Sprite(X,(300,300))
        data['square9'] = 'X'
        winner()
        if fullboard()==False:
            Computerturn()
        elif fullboard()== True and data['Game Over']==False:
            Sprite(TieGame,(500,250))


    
def isEmpty(comp_number):
    if comp_number == 1:
        if data['square1'] == 'X' or data['square1'] == 'O' and data['Game Over'] == False:
            return False
        return True
    
    if comp_number == 2:
        if data['square2'] == 'X' or data['square2'] == 'O' and data['Game Over'] == False:
            return False
        return True
    
    if comp_number == 3:
        if data['square3'] == 'X' or data['square3'] =='O' and data['Game Over'] == False:
            return False
        return True
    
    if comp_number == 4:
        if data['square4'] == 'X' or data['square4'] == 'O' and data['Game Over'] == False:
            return False
        return True
    
    if comp_number == 5:
        if data['square5'] == 'X' or data['square5'] == 'O' and data['Game Over'] == False:
            return False
        return True
    
    if comp_number == 6:
        if data['square6'] == 'X' or data['square6'] == 'O' and data['Game Over'] == False:
            return False
        return True
    
    if comp_number == 7:
        if data['square7'] == 'X' or data['square7'] == 'O' and data['Game Over'] == False:
            return False
        return True
    
    if comp_number == 8:
        if data['square8'] == 'X' or data['square8'] == 'O' and data['Game Over'] == False:
            return False
        return True
    
    if comp_number == 9:
        if data['square9'] == 'X' or data['square9'] == 'O' and data['Game Over'] == False:
            return False
        return True
    
    
def Computerturn():
    from random import randint
    comp_num=randint(1,9)
    O=TextAsset('O',fill=black,style='bold 120pt Times')#
    
    if comp_num==1 and isEmpty(1) == True:
        Sprite(O,(0,0))
        data['square1'] = 'O'
        winner()


    elif comp_num==2 and isEmpty(2) == True:
        Sprite(O,(150,0))
        data['square2'] = 'O'        
        winner()


    elif comp_num==3 and isEmpty(3) == True:
        Sprite(O,(300,0))
        data['square3'] = 'O'   
        winner()


    elif comp_num==4 and isEmpty(4) == True:
        Sprite(O,(0,150))
        data['square4'] = 'O'
        winner()

    elif comp_num==5 and isEmpty(5) == True:
        Sprite(O,(150,150))
        data['square5'] = 'O'

    elif comp_num==6 and isEmpty(6) == True:
        Sprite(O,(300,150))
        data['square6'] = 'O'
        winner()

    elif comp_num==7 and isEmpty(7) == True:
        Sprite(O,(0,300))
        data['square7'] = 'O'
        winner()

    elif comp_num==8 and isEmpty(8) == True:
        Sprite(O,(150,300))
        data['square8'] = 'O'
        winner()

    elif comp_num==9 and isEmpty(9) == True:
        Sprite(O,(300,300))
        data['square9'] = 'O'
        winner()
    
    else:
        Computerturn()



def winner():
    computer_winner=TextAsset('Computer Wins!!!',fill=black,style='bold 120pt Times')
    user_winner=TextAsset('YOU wIN!!!!!',fill=black,style='bold 40pt Times')
    if (data['square1'] == 'X' and data['square2'] == 'X' and data['square3'] == 'X') :
        Sprite(user_winner,(500,100))
        data['Game Over']= True

    elif (data['square1'] == 'O' and data['square2'] == 'O' and data['square3'] == 'O'):
        Sprite(computer_winner,(500,100))
        data['Game Over'] =True

    elif (data['square4'] == 'X' and data['square5'] == 'X' and data['square6'] == 'X'):
        Sprite(user_winner,(500,250))
        data['Game Over'] = True

    elif (data['square4'] == 'O' and data['square5'] == 'O' and data['square6'] == 'O'):
        Sprite(computer_winner,(500,250))    
        data['Game Over'] = True

    elif (data['square7'] == 'X' and data['square8'] == 'X' and data['square9'] == 'X'): 
        Sprite(user_winner,(500,250))
        data['Game Over'] =True

    elif (data['square7'] == 'O' and data['square8'] == 'O' and data['square9'] == 'O'):
        Sprite(computer_winner,(500,250))
        data['Game Over'] =True

        
        
    elif (data['square1'] == 'X' and data['square4'] == 'X' and data['square7'] == 'X'):
        Sprite(user_winner,(500,250))
        data['Game Over'] =True

    elif(data['square1'] ==  'O' and data['square4'] == 'O' and data['square7'] == 'O'):
        Sprite(computer_winner,(500,250))
        data['Game Over'] = True

    elif (data['square2'] == 'X' and data['square5'] == 'X' and data['square8'] == 'X'):
        Sprite(user_winner,(500,250))
        data['Game Over'] = True

    elif(data['square2'] == 'O' and data['square5'] == 'O' and data['square8'] == 'O'):
        Sprite(computer_winner,(500,250))
        data['Game Over'] = True

    elif (data['square3'] == 'X' and data['square6'] == 'X' and data['square9'] == 'X'):
        Sprite(user_winner,(500,250))
        data['Game Over'] =True

    elif(data['square3'] == 'O' and data['square6'] == 'O' and data['square9'] == 'O'):
        Sprite(computer_winner,(500,250))
        data['Game Over'] =True

    elif (data['square1'] == 'X' and data['square5'] == 'X' and data['square9'] == 'X'):
        Sprite(user_winner,(500,250))
        data['Game Over'] =True

    elif (data['square1'] == 'O' and data['square5'] == 'O' and data['square9'] == 'O'):
        Sprite(computer_winner,(500,250))
        data['Game Over'] =True

    elif (data['square3'] == 'X' and data['square5'] == 'X' and data['square7'] == 'X'):
        Sprite(user_winner,(500,250))
        data['Game Over'] =True

    elif(data['square3'] == 'O' and data['square5'] == 'O' and data['square7'] == 'O'):
        Sprite(computer_winner,(500,250))
        data['Game Over'] =True


    

def fullboard ():
     if isEmpty(1) == False and isEmpty(2) == False and isEmpty(3) == False and isEmpty(4) == False and isEmpty(5) == False and isEmpty(6) == False and isEmpty(7) == False and isEmpty(8) == False and isEmpty(9) == False:
        return True
     return False
    


if __name__ == '__main__':
    data = {}
    data['square1'] = ''
    data['square2'] = ''
    data['square3'] = ''
    data['square4'] = ''
    data['square5'] = ''
    data['square6'] = ''
    data['square7'] = ''
    data['square8'] = ''
    data['square9'] = ''
    data['Game Over'] = False

    
    
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