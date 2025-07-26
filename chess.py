import os
os.environ["OMP_NUM_THREADS"] = "10"
import numpy as np
import pygame
import math
def copy_val(l):
    for i in range(len(l)):
        copy = i
        if l[i] != ".":
            break
    return copy
def bishop(s , i , j):
    actions_list = []
    empty = ["."]
    diag1 = s[[k+i for k in range(8-i)][:min(8-i , 8-j)] , [m + j for m in range(8-j)][:min(8-i , 8-j)]][1:]
    if list(diag1) != []:
            copy = copy_val(diag1)        
            for x in range(j+1 ,j+copy+1 +int( not diag1[copy][0] == s[i][j][0]) ):
                    y = x - (j-i)
                    actions_list.append((((j,i) , (x,y) ) , s[i][j])) 
                            
    diag2 = s[[i+k for k in range(8-i)][:min(8-i, j+1)] , [j-m for m in range(j+1)][:min(8-i , j+1)]][1:]
    if list(diag2) != []:
                    copy = copy_val(diag2)
                    for x in range(j-1, j - copy-   1 -int( not diag2[copy][0] == s[i][j][0])  ,-1 ):
                            y = (j+i)  - x
                            actions_list.append((((j,i) , (x,y) ) , s[i][j]))    
                    
    diag3 =  s[[i-k for k in range(i+1)][:min(i+1 , j+1)] , [ j-m    for m in range(j+1)][:min(i +1, j+1)]][1:]
    if list(diag3) != []:
                   
                    copy = copy_val(diag3)
                   
                    for x in range(j - 1, j-1 - copy-int( not diag3[copy][0] == s[i][j][0]) , -1):
                        y = x - (j - i) 
                        
                        actions_list.append((((j,i) , (x , y) ) , s[i][j]))

    diag4 = s[[i-k for k in range(i+1)][:min(i+1 , 8-j)] , [m + j for m in range(8-j)][:min(i+1 , 8-j)]][1:]
    if list(diag4) != []:
                    copy = copy_val(diag4)
                    for x in range(j+1,j+copy+1+int( not diag4[copy][0] == s[i][j][0])):
                        y  = (j+i) - x
                        actions_list.append((((j,i) , (x , y) ) , s[i][j]))
    return actions_list
def king(s, i , j):
    actions_list = []
    if 0<=(i+1)<8 and 0<=(j)<8 and (s[i][j] == "." or s[i][j][0] != s[i+1][j][0] ):
        actions_list.append((((j , i) , (j, i+1)) , s[i][j]))
    if 0<=(i+1)<8 and 0<=(j+1)<8 and (s[i][j] == "." or s[i][j][0] != s[i+1][j+1][0] ):
        actions_list.append((((j , i) , (j+1, i+1)) , s[i][j]))
    if 0<=(i)<8 and 0<=(j+1)<8 and (s[i][j] == "." or s[i][j][0] != s[i][j+1][0] ):
        actions_list.append((((j , i) , (j+1, i)) , s[i][j]))
    if 0<=(i-1)<8 and 0<=(j-1)<8 and (s[i][j] == "." or s[i][j][0] != s[i-1][j-1][0] ):
        actions_list.append((((j , i) , (j-1, i-1)) , s[i][j]))
    if 0<=(i-1)<8 and 0<=(j)<8 and (s[i][j] == "." or s[i][j][0] != s[i-1][j][0] ):
        actions_list.append((((j , i) , (j, i-1)) , s[i][j]))
    if 0<=(i)<8 and 0<=(j-1)<8 and (s[i][j] == "." or s[i][j][0] != s[i][j-1][0] ):
        actions_list.append((((j , i) , (j-1, i)) , s[i][j]))
    if 0<=(i-1)<8 and 0<=(j-1)<8 and (s[i][j] == "." or s[i][j][0] != s[i-1][j-1][0] ):
        actions_list.append((((j , i) , (j-1, i-1)) , s[i][j]))
    if 0<=(i+1)<8 and 0<=(j-1)<8 and (s[i][j] == "." or s[i][j][0] != s[i+1][j-1][0] ):
        actions_list.append((((j , i) , (j-1, i+1)) , s[i][j]))
    return actions_list
def knight(s, i , j):
    actions_list = []
    #actions_list.append((((j , i) , (j+2, i+1)) , s[i][j]))
    
    if 0<=(j+2)<8 and 0<=(i+1)<8 and (s[i][j] == "." or s[i][j][0] != s[i+1][j+2][0]):
                    actions_list.append((((j , i) , (j+2, i+1)) , s[i][j]))
    if 0<=(j+2)<8 and 0<=(i-1)<8 and (s[i][j] == "." or s[i][j][0] != s[i-1][j+2][0]):
                    actions_list.append((((j , i) , (j+2, i-1)) , s[i][j]))
                
    if 0<=(j-2)<8 and 0<=(i+1)<8 and (s[i][j] == "." or s[i][j][0] != s[i+1][j-2][0]):
                    actions_list.append((((j , i) , (j-2, i+1)) , s[i][j]))
    if 0<=(j-2)<8 and 0<=(i-1)<8 and (s[i][j] == "." or s[i][j][0] != s[i-1][j-2][0]):
                    actions_list.append((((j , i) , (j-2, i-1)) , s[i][j]))
    if 0<=(j+1)<8 and 0<=(i-2)<8 and (s[i][j] == "." or s[i][j][0] != s[i-2][j+1][0]):
                    actions_list.append((((j , i) , (j+1, i-2)) , s[i][j]))
    if 0<=(j-1)<8 and 0<=(i+2)<8 and (s[i][j] == "." or s[i][j][0] != s[i+2][j-1][0]):
                    actions_list.append((((j , i) , (j-1, i+2)) , s[i][j]))
    if 0<=(j+1)<8 and 0<=(i+2)<8 and (s[i][j] == "." or s[i][j][0] != s[i+2][j+1][0]):
                    actions_list.append((((j , i) , (j+1, i+2)) , s[i][j]))
    if 0<=(j-1)<8 and 0<=(i-2)<8 and (s[i][j] == "." or s[i][j][0] != s[i-2][j-1][0]):
                    actions_list.append((((j , i) , (j-1, i-2)) , s[i][j]))
    return actions_list
def rook(s, i , j):
    actions_list = []
    right = s[i , :][j+1:]
    empty = ["."]
    truth_value = (right == (empty*(7-j)))
    for x in range(7-j):
        if not truth_value[x]:
            if right[x][0] != s[i][j][0]:
                actions_list.append((((j,i) , (x+j+1 , i) ) , s[i][j]))
            break
        else:
            actions_list.append((((j,i) , (x+j+1 , i) ) , s[i][j]))                    
    down = s[: , j] [i+1:]
    truth_value = (down == (empty*(7-i)))
    for y in range(7-i):
        if not truth_value[y]:
            if down[y][0] != s[i][j][0]:    
                actions_list.append((((j,i) , ( j, y+1+i) ) , s[i][j]))
            break
        else:
            actions_list.append((((j,i) , ( j, y+1+i) ) , s[i][j]))
    left = s[i][:j]
    truth_value = (left == (empty* (j)))
    for x in range(j):
        if not truth_value[x]:
            if left[x][0] != s[i][j][0]:
                actions_list.append((((j,i) , ( j-x-1, i) ) , s[i][j]))
            break
        else:
            actions_list.append((((j,i) , ( j-x-1, i) ) , s[i][j]))
    up  = s[: , j][:i]
    truth_value = (up == (empty* (i)))
    for y in range(i):
            if not truth_value[y]:
                if up[y][0] != s[i][j][0]:
                   actions_list.append((((j,i) , ( j, i-y-1) ) , s[i][j]))
                break
            else:
                 actions_list.append((((j,i) , ( j, i-y-1) ) , s[i][j]))
                  


    return actions_list
def actions(s , color  , piece = None):
    actions_list = []
    if piece is  not None:
        for i in range(8):
               for j in range(8):
                      if s[i][j] == piece and piece[1:] == "ki":
                            actions_list +=king(s , i ,j)
        return actions_list 
    for i in range(8):
        for j in range(8):
            
            if color+'p' ==   s[i][j]:
                adder = (-1) ** int(s[i][j][0]  == 'w')
                
                if 0<=(i+adder)<8 and s[i+adder][j] == ".":
                    actions_list.append((((j , i) , (j, i+adder)) , s[i][j]))
                if  0<=(i+adder)<8 and 0<=(j+1)<8 and s[i+adder][j+1] != "." and s[i+adder][j+1][0] != color :
                    actions_list.append((((j , i) , (j+1, i+adder)) , s[i][j]))
                if 0<=(i+adder)<8 and 0<=(j-1)<8 and   s[i+adder][j-1] != "." and s[i+adder][j-1][0] != color:
                    actions_list.append((((j , i) , (j-1, i+adder)) , s[i][j]))


            elif color+"b" == s[i][j] :
                actions_list += bishop(s , i , j)
            elif color+"r" == s[i][j] :
                
                actions_list += rook(s, i ,j)

            elif color + "k" == s[i][j] :
                actions_list += knight(s , i ,j)
            elif color+"q" == s[i][j] :
                actions_list += rook(s,i,j) + bishop(s,i,j)
                


            elif color+"ki"   == s[i][j] :
                actions_list += king(s , i, j)
                
            

    return actions_list
def evaluation(s):
    pieces = {"w" :0,
              "b" : 0}
    values = {"k" : 3,
              "p" : 1,
              "b" : 3,
              "q" : 9, 
              "r" : 5,
              "ki" : 139}
    sum  = 0
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] != ".":
                pieces[s[i][j][0]] += values[s[i][j][1:]]
                

    return ((pieces["w"] - pieces["b"]) / (139 ) )

def perform(s ,  actions):
        copy = s.copy()
        copy[actions[0][0][1] , actions[0][0][0]] = "."
        
        copy[actions[0][1][1] , actions[0][1][0]] = actions[1]
        return copy
def terminal(s):

    wki = False
    bki = False
    for i in s:
        for j in i:
            if j == "wki":
                wki = True
            if j == "bki":
                bki = True
    if wki and bki:
        return False
    return True
def minimax(state ,a,b, player=True,depth=0 , ):
    if depth >4:
           return (state , evaluation(state))
    if player:
        max_value = -2
        for i in actions(state , "w"):
            possiblestate = perform(state.copy() , i)
            val =  minimax(possiblestate,a, b,False , depth+1)[1]
            
            
            if val> max_value:
                   max_value = val
                   s = possiblestate
            elif max_value == val:
                if sum(np.char.count(possiblestate[7 , : ] , '.'))  > sum(np.char.count(s[0, :] , ".")):
                    max_value = val
                    s = possiblestate
            if max_value>b:
                break
            a = max(a , max_value)
        
        return (s, max_value)
    else:
        min_value = 2
        for i in actions(state , "b"):
            
            possiblestate = perform(state.copy() , i)
            val =  minimax(possiblestate.copy(),a,b,True ,depth+1)[1]
           
            if val < min_value :
                min_value = val
                s = possiblestate
            elif min_value == val:
                if sum(np.char.count(possiblestate[0 , :] , ". ")) > sum(np.char.count(s[0 , :] , ".")):
                    min_value = val
                    s = possiblestate
            if min_value<a:
                break
            b = min(b , min_value  )  
        
        return  (s,min_value)
def mini(state,depth = 0):                  
    if terminal(state):
           
           return (state, 1)
    if depth >3:
           return (state , evaluation(state))
    
    min_value = 2
    for i in actions(state , "b"):
        possiblestate = perform(state.copy() , i)
        val = maxx(possiblestate.copy(),depth+1)[1]
        if min_value>val:
               min_value = val
               s = possiblestate
        elif min_value == val:
            if len(actions(possiblestate , "b")) > len(actions(s, "b")):
                min_value = val
                s = possiblestate
    return (s , min_value)
def maxx(state  ,depth=0) :
    if terminal(state):
        return (state ,     -1)
    if depth >3:
           return (state , evaluation(state))
    
    max_value = -2
    for i in actions(state , "w"):
            possiblestate = perform(state.copy() , i)
            val = mini(possiblestate,depth+1)[1]
            if max_value < val:
                   max_value = val
                   s = possiblestate
            elif max_value == val:
                if len(actions(possiblestate , "w")) > len(actions(s , "w")):
                    max_value = val
                    s = possiblestate
    return (s , max_value)


board = np.array([['br', 'bk', 'bb', 'bki', 'bq', 'bb', 'bk', 'br'],
 ['bp' ,'bp' ,'bp' ,'bp', 'bp' ,'bp' ,'bp' ,'bp'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.' ,'.' ,'.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.' ,'.', '.' ,'.', '.', '.', '.'],
 ['wp' ,'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
 ['wr', 'wk' ,'wb', 'wki', 'wq', 'wb' ,'wk', 'wr']])
current = board.copy()

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock() 
loaded_pieces = []

running = True
current = board.copy()
board_image = pygame.image.load("board.jpg")
imagerect = board_image.get_rect()
imagerect.center = ((1280//2 , 720//2))
select_box = False
flag = False

current = minimax(current.copy() , -4,4,True)[0]
print(current)


while running:
    for event in pygame.event.get():
        screen.fill("gray")
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x , y = pygame.mouse.get_pos()
            print("Mouse button clicked" ,x,y, math.floor(((x / 415) - 1) * (415/56.25)) , math.floor(((y / 135) - 1) * (135/56.25)))
            x = math.floor(((x / 415) - 1) * (415/56.25))
            y = math.floor(((y / 135) - 1) * (135/56.25))
            
            if flag:
                copy = current.copy()
                current = perform(current , (((inital_pos[0] , inital_pos[1]) , (x,7-y)) , current[inital_pos[1]][inital_pos[0]]))
                print((((inital_pos[0] , inital_pos[1]) , (x,y)) , current[y][x]))
                screen.blit(board_image , imagerect)
                for i in range(8):
                    for j in range(8):
                        if current[i][j] != ".":
                            piece_image = pygame.image.load ("pieces/"+current[i][j]+".png")
                            piece_rect = piece_image.get_rect()
                            piece_rect.center = ((415+((56.25/2) * (2*(j)+1)) , 135+((56.25/2) * (2*(7-i) + 1))))
                    
                            screen.blit(piece_image , piece_rect)
                
                pygame.display.flip()
                clock.tick(60)
                
                if not np.all(current[:,:] == (copy[:, :])): 
                    current = minimax(current.copy() , -4,4,True)[0]
                print(current)
            else:
                selec  = pygame.image.load("pieces/s"+current[7-y][x]+".png")
                selec_rect = selec.get_rect()
                selec_rect.center = ((415+ ((56.25/2) * (2*x + 1))) , (135+ ((56.25/2) * (2*(y) + 1))))
            flag  = not flag
            inital_pos = (x,7-y)      
    screen.fill("gray")
            
    # fill the screen with a color to wipe away anything from last frame
    screen.blit(board_image , imagerect)
    for i in range(8):
        for j in range(8):
            
            if current[i][j] != ".":
                    piece_image = pygame.image.load ("pieces/"+current[i][j]+".png")
                    piece_rect = piece_image.get_rect()
                    piece_rect.center = ((415+((56.25/2) * (2*(j)+1)) , 135+((56.25/2) * (2*(7-i) + 1))))
                    
                    screen.blit(piece_image , piece_rect)
    if flag:
        screen.blit(selec, selec_rect)
 
    pygame.display.flip()
    clock.tick(60)
        
            
            
pygame.quit()

'''for i in range(8):
        for j in range(8):
               if current[i][j] != ".":
                    piece_image = pygame.image.load ("pieces/"+current[i][j]+".png")
                    piece_rect = piece_image.get_rect()
                    piece_rect.center = ((415+((56.25/2) * (2*(j)+1)) , 135+((56.25/2) * (2*(7-i) + 1))))
                    
                    screen.blit(piece_image , piece_rect)
    
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
                    pygame.display.flip()
                    clock.tick(60)  
    screen.blit(board_image , imagerect)
    current = minimax(current.copy() , -4,4)[0]
    print(current)
    for i in range(8):
        for j in range(8):
               if current[i][j] != ".":
                    piece_image = pygame.image.load ("pieces/"+current[i][j]+".png")
                    piece_rect = piece_image.get_rect()
                    piece_rect.center = ((415+((56.25/2) * (2*(j)+1)) , 135+((56.25/2) * (2*(7-i) + 1)))) 
                    screen.blit(piece_image , piece_rect)
                    pygame.display.flip()
                    clock.tick(60)
    move = input("Enter move: ")
    copy = current[int(move[2]) ,int( move[0])]
    current[int(move[6]) , int(move[4])] =copy
    current[int(move[2]) , int(move[0])] = "."
    print(current)
    screen.blit(board_image , imagerect)
    for i in range(8):
        for j in range(8):
               if current[i][j] != ".":
                    piece_image = pygame.image.load ("pieces/"+current[i][j]+".png")
                    piece_rect = piece_image.get_rect()
                    piece_rect.center = ((415+((56.25/2) * (2*(j)+1)) , 135+((56.25/2) * (2*(7-i) + 1))))
                    
                    screen.blit(piece_image , piece_rect)
                    pygame.display.flip()
                    clock.tick(60)'''





'''test_board = []
for i in range(8):
    l = []
    for j in range(8):
        l.append("..")
    test_board.append(l)
print(test_board)
test_board = np.array(test_board)
for i in range(8):
    for j in range(8):
        test = test_board.copy()
        test[i][j] = "wr"
        print(test)
        actions(test)
#print(actions(board))
# 
'''
'''
board = np.array([['br', '.', '.', '.', 'bki', 'bb', '.', 'br'],
 ['bp' ,'bp' ,'bp' ,'bq', '.' ,'bp' ,'bp' ,'.'],
 ['.', '.', '.', '.', '.', 'bk', '.', 'bp'],
 ['.', '.', '.', 'bp' ,'bp' ,'.', 'wq', '.'],
 ['.', 'bk', '.', '.', '.', '.', '.', '.'],
 ['.', '.' ,'wk', '.' ,'wp', '.', '.', '.'],
 ['wp' ,'wp', 'wp', 'wp', '.', 'wp', 'wp', 'wp'],
 ['wr', '.' ,'wb', 'wki', '.', '.' ,'wk', 'wr']])
max_value = -2
for i in actions(board , "w"):
    val = minimax(board.copy() , -4,4 )
    if max_value < val:
        max_value = val
        possiblestate  = perform(board.copy() , i)
print(possiblestate)
'''
