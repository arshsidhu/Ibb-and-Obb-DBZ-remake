from pygame import *
HTPRect=Rect(200,150,600,100)
playRect=Rect(200,284,600,100)
creditsRect=Rect(200,416,600,100)
backRect=Rect(850,35,100,100)
screen=display.set_mode((1000,600))
mode="main menu"
level="0"
level1c="incomplete"
level2c="incomplete"
level3c="incomplete"
level4c="incomplete"
level5c="incomplete"
htp=image.load("howtoplay.png")
htp1=image.load("Instructions Page 1.png")
htp2=image.load("Instructions Page 2.png")
mainmenu=image.load("Home_Button.png")
title=image.load("title.png")
titlepic=image.load("g+v.png")
playnow=image.load("playnow.png")
credit=image.load("credits.png")
creditpage=image.load("creditspage.png")
ending=image.load("ending.png")
page="1"
htpNXT=Rect(879,505,70,70)
htpBCK=Rect(22,497,70,70)
mb=mouse.get_pressed()
mx,my=mouse.get_pos()
mpos=mx,my
mous=False
running=True
while running:
    for e in event.get():
        if e.type==MOUSEBUTTONDOWN:
            mous=True
            if HTPRect.collidepoint(mpos):
                mode="how to play"
            if playRect.collidepoint(mpos):
                mode="play now"
            if creditsRect.collidepoint(mpos):
                mode="credits"
            if backRect.collidepoint(mpos):
                mode="main menu"
        if e.type==QUIT:
            running=False
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    mpos=mx,my
    if mode=="main menu":
        screen.fill((255,255,255))
        screen.blit(title,(200,12))
        screen.blit(titlepic,(100,12))
        screen.blit(titlepic,(800,12))
        draw.rect(screen,(100,100,100),HTPRect)
        screen.blit(htp,(200,150))
        draw.rect(screen,(100,100,100),playRect)
        screen.blit(playnow,(200,284))
        draw.rect(screen,(100,100,100),creditsRect)
        screen.blit(credit,(200,416))
    if mode=="how to play":
        if mb[0]==1:
            if htpNXT.collidepoint(mpos):
                page="2"
            if htpBCK.collidepoint(mpos):
                page="1"
        if page=="1":
            screen.blit(htp1,(0,0))
        if page=="2":
            screen.blit(htp2,(0,0))
        screen.blit(mainmenu,(850,35))
    if mode=="credits":
        screen.blit(creditpage,(0,0))
        draw.rect(screen,(100,100,100),backRect)
        screen.blit(mainmenu,(850,35))
    if mode=="play now":
        if level=="0":
            background=image.load("background.jpg")
            mask=image.load("mask.jpg")
            door1=image.load("doortest.png")
            door2=image.load("door2.png")
            door3=image.load("door3.png")
            levelselect=image.load("levelselect.png")
            myClock=time.Clock()
            level1Rect=Rect(455,312,60,67)
            level2Rect=Rect(555,312,60,67)
            level3Rect=Rect(655,312,60,67)
            player1 = [150,0,0,K_RIGHT,K_LEFT,K_UP,K_DOWN,0,0,1,-1] 
            player2 = [100,0,0,K_d,K_a,K_w,K_s,0,0,1,-1]
            X=0
            Y=1
            VY=2
            RIGHT=3
            LEFT=4
            UP=5
            DOWN=6
            MOVE=7
            FRAME=8
            GRAV=9
            NMOVE=10
            def scene(player1,player2):
                screen.blit(background,(0,0))
                screen.blit(levelselect,(200,12))
                screen.blit(door1,(455,272))
                if level1c=="complete":

                    screen.blit(door2,(555,272))
                if level2c=="complete":

                    screen.blit(door3,(655,272))
                gpic=gpics[player1[MOVE]][int(player1[FRAME])]
                vpic=vpics[player2[MOVE]][int(player2[FRAME])]
                screen.blit(gpic,(player1[X]-21,player1[Y]-47))
                screen.blit(vpic,(player2[X]-21,player2[Y]-47))

            
            def getcolor(mask,x,y):
                if 0<=x< mask.get_width() and 0<= y< mask.get_height():             #Taken from Mac(Scroll Mask Example)
                    return mask.get_at((int(x),int(y)))
                else:
                    return (-1,-1,-1)

            def red(c):
                return c[0]>245 and c[1]<5 and c[2] < 5

            def blue(c):
                return c[0]<5 and c[1]<5 and c[2]>245

            def mleft(player,vx):
                for i in range(vx):
                    if getcolor(mask,player[X]-36,player[Y]-10)!=(254,0,0):
                        player[X] -=1
                    else:
                        player[X] +=1
                        
            def mright(player,vx):
                for i in range(vx):
                    if getcolor(mask,player[X]+36,player[Y]-10)!=(254,0,0):
                        player[X] +=1
                    else:
                        player[X] -=1
                
            def moving(player):
                keylist=key.get_pressed()

                player[NMOVE] = MSTAND

                if keylist[player[RIGHT]] and player[X] <=950:
                    player[NMOVE] = MRIGHT      #right
                    mright(player,10)
                elif keylist[player[LEFT]] and player[X] >=50:
                    player[NMOVE] = MLEFT       #left
                    mleft(player,10)
                else:
                    player[FRAME] = 0
                    player[MOVE] = 0
                    player[NMOVE] = -1
                        
                while red(getcolor(mask,player[X],player[Y])):
                    player[VY] = 0
                    player[Y] -= 1

                if player[MOVE] == player[NMOVE]:     
                    player[FRAME] = player[FRAME] + 0.2 
                    if player[FRAME] >= len(gpics[player[MOVE]]):       #for gpics
                        player[FRAME] = 0
                    if player[FRAME] >= len(vpics[player[MOVE]]):       #for vpics
                        player[FRAME] = 0
                elif player[NMOVE] != -1:     
                    player[MOVE] = player[NMOVE]    
                    player[FRAME] = 1
                    
                player[VY] += 1                       #Added gravity
                player[Y] += player[VY]

                if player[Y]>1500:
                    player[VY] = 0
                    player[Y] = 1500

            def sprite(name,start,end):
                move=[]
                for i in range(start,end+1):
                    move.append(image.load("%s/%s%d.png" % (name,name,i)))
                return move
            
            gpics=[]
            gpics.append(sprite("standG",0,3))
            gpics.append(sprite("moveRG",0,3)) #Change these back
            gpics.append(sprite("moveLG",0,3))
            gpics.append(sprite("jumpG",0,4))
            gpics.append(sprite("RstandG",0,3))
            gpics.append(sprite("RmoveRG",0,3))
            gpics.append(sprite("RmoveLG",0,3))
            gpics.append(sprite("RjumpG",0,4))

            vpics=[]
            vpics.append(sprite("StandV",0,3))
            vpics.append(sprite("MoveRV",0,2))
            vpics.append(sprite("MoveLV",0,2))
            vpics.append(sprite("JumpV",0,2))
            vpics.append(sprite("RstandV",0,3))
            vpics.append(sprite("RmoveRV",0,2))
            vpics.append(sprite("RmoveLV",0,2))
            vpics.append(sprite("RjumpV",0,2))

            MSTAND=0
            MRIGHT=1
            MLEFT=2
            MUP=3
            RSTAND=4
            RRIGHT=5
            RLEFT=6
            RUP=7

            screen=display.set_mode((1000,600))
            running0=True
            while running0:
                for e in event.get():
                    if e.type==QUIT:
                        running0=False
                        quit()
                scene(player1,player2)
                moving(player1)
                moving(player2)
                keylist=key.get_pressed()
                if level1Rect.collidepoint(player1[X],player1[Y]-47):
                    if keylist[player1[UP]]:
                        level="1"
                        running0=False
                if level2Rect.collidepoint(player1[X],player1[Y]-47):
                    if keylist[player1[UP]]:
                        level="2"
                        running0=False
                if level3Rect.collidepoint(player1[X],player1[Y]-47):
                    if keylist[player1[UP]]:
                        level="3"
                        running0=False
                myClock.tick(30)
                display.flip()
        if level=="1":            
            background=image.load("level1.png")
            mask=image.load("level1maskthickgates.jpg")
            reversemask=image.load("level1maskreverse.jpg")
            red=(254,0,0,255)
            myClock = time.Clock()
            #------------- Players ---------------------------------

            player1 = [133,1326,0,K_RIGHT,K_LEFT,K_UP,K_DOWN,0,0,1,-1,0,0,73,1326,0,False] 
            player2 = [103,1326,0,K_d,K_a,K_w,K_s,0,0,1,-1,0,0,23,1326,0,False]
            X=0
            Y=1
            VY=2
            RIGHT=3
            LEFT=4
            UP=5
            DOWN=6
            MOVE=7
            FRAME=8
            GRAV=9
            NMOVE=10
            DIST=11
            TIME=12
            STARTX=13
            STARTY=14
            GTIME=15
            DEAD=16
            #--------------------------------------------------
            def scene(player1,player2):
                global screenX,screenY

                keylist=key.get_pressed()
            #-------------------offset----------------------
                if player1[X] - screenX < 100:
                    screenX = player1[X] - 100
                if player1[X] - screenX > 900:
                    screenX = player1[X] - 900
                if player1[Y] - screenY < 100:
                    screenY = player1[Y] - 100
                if player1[Y] - screenY > 500:
                    screenY = player1[Y] - 500
            #-----------------------------------------------
                screen.blit(background,(-screenX,-screenY))
                gpic=gpics[player1[MOVE]][int(player1[FRAME])]
                vpic=vpics[player2[MOVE]][int(player2[FRAME])]
                screen.blit(gpic,(player1[X]-21-screenX,player1[Y]-47-screenY))
                screen.blit(vpic,(player2[X]-21-screenX,player2[Y]-47-screenY))
                if blue(getcolor(background,player1[X],player1[Y])) and player1[GTIME]>=2:
                    player1[GRAV]= player1[GRAV]*-1
                    player1[GTIME]=0
                if blue(getcolor(background,player2[X],player2[Y])) and player2[GTIME]>=2:
                    player2[GRAV]= player2[GRAV]*-1
                    player2[GTIME]=0
                    
            def getcolor(mask,x,y):
                if 0<=x< mask.get_width() and 0<= y< mask.get_height():             #Taken from Mac(Scroll Mask Example)
                    return mask.get_at((int(x),int(y)))
                else:
                    return (-1,-1,-1)

            def red(c):
                return c[0]>245 and c[1]<5 and c[2] < 5

            def blue(c):
                return c[0]<5 and c[1]<5 and c[2]>245

            def mleft(player,vx):
                for i in range(vx):
                    if player[GRAV]==1:
                        if getcolor(mask,player[X]-36,player[Y]-10)!=(254,0,0):
                            player[X] -=1
                        else:
                            player[X] +=1

                    if player[GRAV]==-1:
                        if getcolor(reversemask,player[X]-36,player[Y]-10)!=(254,0,0):
                            player[X] -=1
                        else:
                            player[X] +=1
            def mright(player,vx):
                for i in range(vx):
                    if player[GRAV]==1:
                        if getcolor(mask,player[X]+36,player[Y]-10)!=(254,0,0):
                            player[X] +=1
                        else:
                            player[X] -=1
                    if player[GRAV]==-1:
                        if getcolor(reversemask,player[X]+36,player[Y]-10)!=(254,0,0):
                            player[X] +=1
                        else:
                            player[X] -=1 
                        
            def falling(player,vy):
                for i in range(vy):
                    if getcolor(mask,player[X],player[Y+i])!=(254,0,0):
                        player[Y] -=1
                    else:
                        player[VY] +=1
                        
            def rfalling(player,vy):
                for i in range(vy):
                    if getcolor(reversemask,player[X],player[Y+i])!=(254,0,0):
                        player[Y] +=1
                    else:
                        player[VY] -=1

            def playercollide(g,v,grect,vrect):
                keylist=key.get_pressed()
                
                if grect.collidepoint(v[X],v[Y]):
                    if g[Y] - v[Y] >= 10:
                        v[Y] -= 1
                        v[VY] = 0
                        if keylist[v[UP]]:
                            v[VY] = -15

                    
                if vrect.collidepoint(g[X],g[Y]):
                    if v[Y] - g[Y] >= 10:
                        g[Y] -= 1
                        g[VY] = 0
                        if keylist[g[UP]]:
                            g[VY] = -15

            def Rplayercollide(g,v,grect,vrect):
                keylist=key.get_pressed()
                
                if grect.collidepoint(v[X],v[Y]):
                    if g[Y] - v[Y] <= 10:
                        v[Y] += 1
                        v[VY] = 0
                        if keylist[v[UP]]:
                            v[VY] = +15

        
                if vrect.collidepoint(g[X],g[Y]):
                    if v[Y] - g[Y] <= 10:
                        g[Y] += 1
                        g[VY] = 0
                        if keylist[g[UP]]:
                            g[VY] = +15
                        
            def moving(player,g,v):
                keylist=key.get_pressed()

                player[NMOVE] = MSTAND

                if keylist[player[RIGHT]] and player[DEAD]!=True and player[X]<=1900:
                    player[NMOVE] = MRIGHT       #right
                    mright(player,10)
                elif keylist[player[LEFT]] and player[DEAD]!=True and player[X]>=100:
                    player[NMOVE] = MLEFT       #left
                    mleft(player,10)
                elif keylist[player[UP]] and player[DEAD]!=True: 
                    player[NMOVE] = MUP   #up
                else:
                    if player[DEAD]==False:
                        player[NMOVE] = MSTAND
                    if player[DEAD]==True:
                        player[NMOVE] = DEATH
                        player[TIME] += 0.1
                        if player[TIME] >= 3.5:
                            player[TIME] = 0
                            g[X],g[Y] = g[STARTX],g[STARTY]
                            v[X],v[Y] = v[STARTX],v[STARTY]
                            player[DEAD] = False
                            player1[GRAV] = 1
                            
                while red(getcolor(mask,player[X],player[Y])):
                    player[VY] = 0
                    player[Y] -= 1
                    
                if keylist[player[UP]] and player[DEAD]!=True:
                    if player[VY] == 0 and (red(getcolor(mask,player[X],player[Y]+30)) or player[Y]==1500):
                        player[VY] = -15    #Change this value for hop
                        falling(player,player[VY])

                if player[MOVE] == player[NMOVE]:     
                    player[FRAME] = player[FRAME] + 0.2 
                    if player[FRAME] >= len(gpics[player[MOVE]]):       #for gpics
                        player[FRAME] = 0
                    if player[FRAME] >= len(vpics[player[MOVE]]):       #for vpics
                        player[FRAME] = 0
                elif player[NMOVE] != -1:     
                    player[MOVE] = player[NMOVE]    
                    player[FRAME] = 1
                    
                player[VY] += 1                       #Added gravity
                player[Y] += player[VY]

                if player[Y]>1450:
                    player[Y] = 1450
                    player[DEAD]=True

            def Rmoving(player,g,v):            #Moving with reverse gravity
                keylist=key.get_pressed()

                player[NMOVE] = -1

                if keylist[player[RIGHT]] and player[DEAD]!=True and player[X]<=1900:
                    player[NMOVE] = RRIGHT       #right
                    mright(player,10)
                elif keylist[player[LEFT]] and player[DEAD]!=True and player[X]<=1900:
                    player[NMOVE] = RLEFT       #left
                    mleft(player,10)
                elif keylist[player[UP]]and player[DEAD]!=True: 
                    player[NMOVE] = RUP   #up
                else:
                    if player[DEAD]==False:
                        player[NMOVE] = RSTAND
                    if player[DEAD]==True:
                        player[NMOVE] = RDEATH
                        player[TIME] += 0.1
                        if player[TIME] >= 3.5:
                            player[TIME] = 0
                            g[X],g[Y] = g[STARTX],g[STARTY]
                            v[X],v[Y] = v[STARTX],v[STARTY]
                            player[DEAD] = False
                            player1[GRAV] = 1
                        
                while red(getcolor(reversemask,player[X],player[Y]-40)):
                    player[VY] = 0
                    player[Y] += 1
                    
                if keylist[player[UP]] and player[DEAD]!=True :
                    if player[VY] == 0 and (red(getcolor(mask,player[X],player[Y]+30)) or player[Y]==0):
                        player[VY] = +15    #Change this value for hop


                if player[MOVE] == player[NMOVE]:     
                    player[FRAME] = player[FRAME] + 0.2 
                    if player[FRAME] >= len(gpics[player[MOVE]]):       #for gpics
                        player[FRAME] = 0
                    if player[FRAME] >= len(vpics[player[MOVE]]):       #for vpics
                        player[FRAME] = 0
                elif player[NMOVE] != -2:     
                    player[MOVE] = player[NMOVE]    
                    player[FRAME] = 1
                player[VY] -= 1                       #Added gravity
                player[Y] += player[VY]
                if player[VY]<-40:
                    player[VY]=-40
                
                if player[Y]<50:
                    player[Y] = 50
                    player[DEAD]=True
                    
            def sprite(name,start,end):
                move=[]
                for i in range(start,end+1):
                    move.append(image.load("%s/%s%d.png" % (name,name,i)))
                return move
              

            gpics=[]
            gpics.append(sprite("standG",0,3))
            gpics.append(sprite("moveRG",0,3)) #Change these back
            gpics.append(sprite("moveLG",0,3))
            gpics.append(sprite("jumpG",0,4))
            gpics.append(sprite("RstandG",0,3))
            gpics.append(sprite("RmoveRG",0,3))
            gpics.append(sprite("RmoveLG",0,3))
            gpics.append(sprite("RjumpG",0,4))
            gpics.append(sprite("deathG",0,3))
            gpics.append(sprite("RdeathG",0,3))

            vpics=[]
            vpics.append(sprite("StandV",0,3))
            vpics.append(sprite("MoveRV",0,2))
            vpics.append(sprite("MoveLV",0,2))
            vpics.append(sprite("JumpV",0,2))
            vpics.append(sprite("RstandV",0,3))
            vpics.append(sprite("RmoveRV",0,2))
            vpics.append(sprite("RmoveLV",0,2))
            vpics.append(sprite("RjumpV",0,2))
            vpics.append(sprite("deathV",0,3))
            vpics.append(sprite("RdeathV",0,3))

            MSTAND=0
            MRIGHT=1
            MLEFT=2
            MUP=3
            RSTAND=4
            RRIGHT=5
            RLEFT=6
            RUP=7
            DEATH=8
            RDEATH=9
            
            screen=display.set_mode((1000,600))
            running1=True
            screenX,screenY = 0,0
            WORLDY = 1450
            while running1:
                for e in event.get():
                    if e.type==QUIT:
                        running1=False
                        quit()
                mb=mouse.get_pressed()
                mx,my=mouse.get_pos()
                mpos=mx,my
                
                gokurect = Rect((player1[X]-20,player1[Y]-50,40,100))
                vegetarect = Rect((player2[X]-20,player2[Y]-50,40,100))

                player1[GTIME]+=0.1
                player2[GTIME]+=0.1

                scene(player1,player2)
                
                if player1[GRAV]==1:
                    moving(player1,player1,player2)
                    playercollide(player1,player2,gokurect,vegetarect)
                if player2[GRAV]==1:
                    moving(player2,player1,player2)

                if player1[GRAV]==-1:
                    Rmoving(player1,player1,player2)
                    Rplayercollide(player1,player2,gokurect,vegetarect)
                if player2[GRAV]==-1:
                    Rmoving(player2,player1,player2)

                if player1[X]>=1823 and player2[X]>=1823:
                    if player1[Y]>=330 and player2[Y]>=330:
                        level1c="complete"
                        level="0"
                        running1=False
                                        
                    
                myClock.tick(30)
                
                display.flip()
            
    if level=="2":
        background=image.load("level2.png")
        mask=image.load("level2mask.jpg")
        reversemask=image.load("level2reverse.jpg")
        red=(254,0,0,255)
        myClock = time.Clock()
        #------------- Players ---------------------------------

        player1 = [133,1326,0,K_RIGHT,K_LEFT,K_UP,K_DOWN,0,0,1,-1,0,0,73,1326,0,False] 
        player2 = [103,1326,0,K_d,K_a,K_w,K_s,0,0,1,-1,0,0,73,1326,0,False]
        X=0
        Y=1
        VY=2
        RIGHT=3
        LEFT=4
        UP=5
        DOWN=6
        MOVE=7
        FRAME=8
        GRAV=9
        NMOVE=10
        DIST=11
        TIME=12
        STARTX=13
        STARTY=14
        GTIME=15
        DEAD=16
        #--------------------------------------------------

        def scene(player1,player2):
            global screenX,screenY
        #-------------------offset----------------------
            if player1[X] - screenX < 100:
                screenX = player1[X] - 100
            if player1[X] - screenX > 900:
                screenX = player1[X] - 900
            if player1[Y] - screenY < 100:
                screenY = player1[Y] - 100
            if player1[Y] - screenY > 500:
                screenY = player1[Y] - 500
        #-----------------------------------------------
            screen.blit(background,(-screenX,-screenY))
            gpic=gpics[player1[MOVE]][int(player1[FRAME])]
            vpic=vpics[player2[MOVE]][int(player2[FRAME])]
            screen.blit(gpic,(player1[X]-21-screenX,player1[Y]-47-screenY))
            screen.blit(vpic,(player2[X]-21-screenX,player2[Y]-47-screenY))
            if blue(getcolor(background,player1[X],player1[Y])) and player1[GTIME]>=2:
                player1[GRAV]= player1[GRAV]*-1
                player1[GTIME]=0
            if blue(getcolor(background,player2[X],player2[Y])) and player2[GTIME]>=2:
                player2[GRAV]= player2[GRAV]*-1
                player2[GTIME]=0
                
        def getcolor(mask,x,y):
            if 0<=x< mask.get_width() and 0<= y< mask.get_height():             #Taken from Mac(Scroll Mask Example)
                return mask.get_at((int(x),int(y)))
            else:
                return (-1,-1,-1)

        def red(c):
            return c[0]>245 and c[1]<5 and c[2] < 5

        def blue(c):
            return c[0]<5 and c[1]<5 and c[2]>245

        def mleft(player,vx):
            for i in range(vx):
                if player[GRAV]==1:
                    if getcolor(mask,player[X]-36,player[Y]-10)!=(254,0,0):
                        player[X] -=1
                    else:
                        player[X] +=1

                if player[GRAV]==-1:
                    if getcolor(reversemask,player[X]-36,player[Y]-10)!=(254,0,0):
                        player[X] -=1
                    else:
                        player[X] +=1
        def mright(player,vx):
            for i in range(vx):
                if player[GRAV]==1:
                    if getcolor(mask,player[X]+36,player[Y]-10)!=(254,0,0):
                        player[X] +=1
                    else:
                        player[X] -=1
                if player[GRAV]==-1:
                    if getcolor(reversemask,player[X]+36,player[Y]-10)!=(254,0,0):
                        player[X] +=1
                    else:
                        player[X] -=1                   

        def falling(player,vy):
            for i in range(vy):
                if getcolor(mask,player[X],player[Y]+i)!=(254,0,0):
                    player[Y] -=1
                else:
                    player[VY] +=1

        def rfalling(player,vy):
            for i in range(vy):
                if getcolor(mask,player[X],player[Y]+i)!=(254,0,0):
                    player[Y] +=1
                else:
                    player[VY] -=1

        def playercollide(g,v,grect,vrect):
            keylist=key.get_pressed()
            
            if grect.collidepoint(v[X],v[Y]):
                if g[Y] - v[Y] >= 10:
                    v[Y] -= 1
                    v[VY] = 0
                    if keylist[v[UP]]:
                        v[VY] = -15

                
            if vrect.collidepoint(g[X],g[Y]):
                if v[Y] - g[Y] >= 10:
                    g[Y] -= 1
                    g[VY] = 0
                    if keylist[g[UP]]:
                        g[VY] = -15


        def Rplayercollide(g,v,grect,vrect):
            keylist=key.get_pressed()
            
            if grect.collidepoint(v[X],v[Y]):
                if g[Y] - v[Y] <= 10:
                    v[Y] += 1
                    v[VY] = 0
                    if keylist[v[UP]]:
                        v[VY] = +15

    
            if vrect.collidepoint(g[X],g[Y]):
                if v[Y] - g[Y] <= 10:
                    g[Y] += 1
                    g[VY] = 0
                    if keylist[g[UP]]:
                        g[VY] = +15

            
        def moving(player,g,v):
            keylist=key.get_pressed()

            player[NMOVE] = MSTAND

            if keylist[player[RIGHT]] and player[DEAD]!=True and player[X]<=2935:
                player[NMOVE] = MRIGHT       #right
                mright(player,10)
            elif keylist[player[LEFT]] and player[DEAD]!=True and player[X]>=120:
                player[NMOVE] = MLEFT       #left
                mleft(player,10)
            elif keylist[player[UP]] and player[DEAD]!=True: 
                player[NMOVE] = MUP   #up
            else:
                if player[DEAD]==False:
                    player[NMOVE]=MSTAND
                if player[DEAD]==True:
                    player[NMOVE] = DEATH
                    player[TIME] += 0.1
                    if player[TIME] >= 3.5:
                        player[TIME] = 0
                        g[X],g[Y] = g[STARTX],g[STARTY]
                        v[X],v[Y] = v[STARTX],v[STARTY]
                        player[DEAD] = False
                        player1[GRAV] = 1
                    
            while red(getcolor(mask,player[X],player[Y])):
                player[VY] = 0
                player[Y] -= 1
                
            if keylist[player[UP]]:
                if player[VY] == 0 and (red(getcolor(mask,player[X],player[Y]+30)) or player[Y]==1500):
                    player[VY] = -15    #Change this value for hop

            if player[MOVE] == player[NMOVE]:     
                player[FRAME] = player[FRAME] + 0.2 
                if player[FRAME] >= len(gpics[player[MOVE]]):       #for gpics
                    player[FRAME] = 0
                if player[FRAME] >= len(vpics[player[MOVE]]):       #for vpics
                    player[FRAME] = 0
            elif player[NMOVE] != -1:     
                player[MOVE] = player[NMOVE]    
                player[FRAME] = 1
                
            player[VY] += 1                       #Added gravity
            player[Y] += player[VY]

            if player[Y]>1500:
                player[Y]=1500
                player[DEAD] = True


        def Rmoving(player,g,v):            #Moving with reverse gravity
            keylist=key.get_pressed()

            player[NMOVE] = -1

            if keylist[player[RIGHT]] and player[DEAD]!=True:
                player[NMOVE] = RRIGHT       #right
                mright(player,10)
            elif keylist[player[LEFT]] and player[DEAD]!=True:
                player[NMOVE] = RLEFT       #left
                mleft(player,10)
            elif keylist[player[UP]] and player[DEAD]!=True: 
                player[NMOVE] = RUP   #up
            else:
                if player[DEAD]==False:
                    player[NMOVE]=RSTAND
                if player[DEAD]==True:
                    player[NMOVE] = RDEATH
                    player[TIME] += 0.1
                    if player[TIME] >= 3.5:
                        player[TIME] = 0
                        g[X],g[Y] = g[STARTX],g[STARTY]
                        v[X],v[Y] = v[STARTX],v[STARTY]
                        player[DEAD] = False
                        player1[GRAV] = 1
                    
            while red(getcolor(reversemask,player[X],player[Y]-40)):
                player[VY] = 0
                player[Y] += 1
                
            if keylist[player[UP]]:
                if player[VY] == 0 and (red(getcolor(mask,player[X],player[Y]+50)) or player[Y]==0):
                    player[VY] = +15    #Change this value for hops


            if player[MOVE] == player[NMOVE]:     
                player[FRAME] = player[FRAME] + 0.2 
                if player[FRAME] >= len(gpics[player[MOVE]]):       #for gpics
                    player[FRAME] = 0
                if player[FRAME] >= len(vpics[player[MOVE]]):       #for vpics
                    player[FRAME] = 0
            elif player[NMOVE] != -2:     
                player[MOVE] = player[NMOVE]    
                player[FRAME] = 1
            player[VY] -= 1                       #Added gravity
            player[Y] += player[VY]
            if player[VY]<-40:
                player[VY]=-40
            
            if player[Y]<0:
                player[Y] = 0
                player[DEAD]=True

            
        def sprite(name,start,end):
            move=[]
            for i in range(start,end+1):
                move.append(image.load("%s/%s%d.png" % (name,name,i)))
            return move

        gpics=[]
        gpics.append(sprite("standG",0,3))
        gpics.append(sprite("moveRG",0,3)) #Change these back
        gpics.append(sprite("moveLG",0,3))
        gpics.append(sprite("jumpG",0,4))
        gpics.append(sprite("RstandG",0,3))
        gpics.append(sprite("RmoveRG",0,3))
        gpics.append(sprite("RmoveLG",0,3))
        gpics.append(sprite("RjumpG",0,4))
        gpics.append(sprite("deathG",0,3))
        gpics.append(sprite("RdeathG",0,3))

        vpics=[]
        vpics.append(sprite("StandV",0,3))
        vpics.append(sprite("MoveRV",0,2))
        vpics.append(sprite("MoveLV",0,2))
        vpics.append(sprite("JumpV",0,2))
        vpics.append(sprite("RstandV",0,3))
        vpics.append(sprite("RmoveRV",0,2))
        vpics.append(sprite("RmoveLV",0,2))
        vpics.append(sprite("RjumpV",0,2))
        vpics.append(sprite("deathV",0,3))
        vpics.append(sprite("RdeathV",0,3))

        MSTAND=0
        MRIGHT=1
        MLEFT=2
        MUP=3
        RSTAND=4
        RRIGHT=5
        RLEFT=6
        RUP=7
        DEATH=8
        RDEATH=9

        screen=display.set_mode((1000,600))
        running2=True
        screenX,screenY = 0,0
        WORLDY = 1450
        while running2:
            for e in event.get():
                if e.type==QUIT:
                    running2=False
                    quit()
            mb=mouse.get_pressed()
            mx,my=mouse.get_pos()
            mpos=mx,my

            gokurect = Rect((player1[X]-20,player1[Y]-50,40,100))
            vegetarect = Rect((player2[X]-20,player2[Y]-50,40,100))

            player1[GTIME]+=0.1
            player2[GTIME]+=0.1
            
            scene(player1,player2)

            
            if player1[GRAV]==1:
                moving(player1,player1,player2)
                playercollide(player1,player2,gokurect,vegetarect)
            if player2[GRAV]==1:
                moving(player2,player1,player2)

            if player1[GRAV]==-1:
                Rmoving(player1,player1,player2)
                Rplayercollide(player1,player2,gokurect,vegetarect)
            if player2[GRAV]==-1:
                Rmoving(player2,player1,player2)

            if player1[X]>=2915 and player2[X]>=2915:
                level2c="complete"
                level="0"
                running2=False
                
            myClock.tick(30)

            display.flip()
    if level=="3":
        background=image.load("level3.png")
        mask=image.load("level3mask1.png")
        reversemask=image.load("level3mask1.png")
        myClock = time.Clock()
        #------------- Players ---------------------------------

        player1 = [73,1326,0,K_RIGHT,K_LEFT,K_UP,K_DOWN,0,0,1,-1,0,0,73,1326,0] # players
        player2 = [23,1326,0,K_d,K_a,K_w,K_s,0,0,1,-1,0,0,23,1326,0]
        frieza1 = [1143,1450,-2,-2,-2,-2,-2,0,0,-1,-1]                          #3 badguys
        frieza2 = [1053,0,-2,-2,-2,-2,-2,0,0,-1,-1]
        frieza3 = [1693,0,-2,-2,-2,-2,-2,0,0,-1,-1]
        blast1 = [1143,1431,-2,-2,-2,-2,-2,0,0,-1,-2,-2,0,1143,1431]            #blasts fired by badguys
        blast2 = [1053,286,-2,-2,-2,-2,-2,0,0,-1,-2,-2,0,1053,286]
        blast3 = [1693,285,-2,-2,-2,-2,-2,0,0,-1,-2,-2,0,1693,285]
        X=0             #X position
        Y=1             #Y position
        VY=2            #Velocity of player in y direction
        RIGHT=3         #Moving key
        LEFT=4          #Moving key
        UP=5            #Moving key
        DOWN=6          #Moving key
        MOVE=7          #Sprite action
        FRAME=8         #Sprite frame
        GRAV=9          #Current gravity of player
        NMOVE=10        #Switching between sprite actions
        DIST = 11       #distance between player and badguy
        TIME = 12       #time used to calculate blast range and animation
        STARTX = 13     #Starting X postion  
        STARTY = 14     #Starting Y postion
        GTIME = 15      #GTIME used to prevent constant flipping in gravity gate

        #---------------------FLAGS---------------------------
        gokuhit = "FALSE"       #flag for if goku should die
        vegetahit = "FALSE"
        Rgokuhit = "FALSE"       
        Rvegetahit = "FALSE"
        dead = "FALSE"          #flag for death function
        Rdead = "FALSE"
        #--------------------------------------------------

        def scene(player1,player2,blast1,blast2,blast3,frieza1,frieza2,frieza3):
            global screenX,screenY 
        #-------------------offset----------------------     #offset allows for the screen to follow player1
            if player1[X] - screenX < 100:
                screenX = player1[X] - 100
            if player1[X] - screenX > 900:
                screenX = player1[X] - 900
            if player1[Y] - screenY < 100:
                screenY = player1[Y] - 100
            if player1[Y] - screenY > 500:
                screenY = player1[Y] - 500
        #-----------------------------------------------
            screen.blit(background,(-screenX,-screenY))
            gpic=gpics[player1[MOVE]][int(player1[FRAME])]      #Current sprite animation and frame
            vpic=vpics[player2[MOVE]][int(player2[FRAME])]
            screen.blit(gpic,(player1[X]-21-screenX,player1[Y]-47-screenY))     #blitting current sprite onto screen
            screen.blit(vpic,(player2[X]-21-screenX,player2[Y]-47-screenY))

            fpic1 = fpics[frieza1[MOVE]][int(frieza1[FRAME])]           #Current sprite animation and frame
            screen.blit(fpic1,(frieza1[X]-screenX,frieza1[Y]-screenY))
            fpic2 = fpics[frieza2[MOVE]][int(frieza2[FRAME])]
            screen.blit(fpic2,(frieza2[X]-screenX,frieza2[Y]-screenY))
            fpic3 = fpics[frieza3[MOVE]][int(frieza3[FRAME])]
            screen.blit(fpic3,(frieza3[X]-screenX,frieza3[Y]-screenY))

            if blast1[3] == 1:                                          #Blast is not always blitted onto screen
                bpic1 = blastpics[blast1[MOVE]][int(blast1[FRAME])]
                screen.blit(bpic1,(blast1[X]-screenX,blast1[Y]-screenY))
            if blast2[3] == 1:
                bpic2 = blastpics[blast2[MOVE]][int(blast2[FRAME])]
                screen.blit(bpic2,(blast2[X]-screenX,blast2[Y]-screenY))
            if blast3[3] == 1:
                bpic3 = blastpics[blast3[MOVE]][int(blast3[FRAME])]
                screen.blit(bpic3,(blast3[X]-screenX,blast3[Y]-screenY))
        #-------------Flipping the gravity---------------------        
            if blue(getcolor(background,player1[X],player1[Y])) and player1[GTIME] >=2: 
                player1[GRAV]= player1[GRAV]*-1
                player1[GTIME] = 0      #GTIME prevents players from flipping continously in the gravity gate
            if blue(getcolor(background,player2[X],player2[Y])) and player2[GTIME] >=2:
                player2[GRAV]= player2[GRAV]*-1
                player2[GTIME] = 0
        #------------------------------------------------------
                
        def getcolor(mask,x,y):
            if 0<=x< mask.get_width() and 0<= y< mask.get_height():             #Taken from Mac(Scroll Mask Example)
                return mask.get_at((int(x),int(y)))
            else:
                return (-1,-1,-1)

        def red(c):                                     #If colour is red but not completely
            return c[0]>245 and c[1]<5 and c[2] < 5

        def blue(c):
            return c[0]<5 and c[1]<5 and c[2]>245

        def green(c):
            return c[0]<5 and c[1]>245 and c[2]<5

        def mleft(player,vx):       #Checks every pixel moving left
            for i in range(vx):
                if getcolor(mask,player[X]-36,player[Y]-10)!=(254,0,0):
                    player[X] -=1
                else:
                    player[X] +=1
                    
        def mright(player,vx):      #Checks every pixel moving right
            for i in range(vx):
                if getcolor(mask,player[X]+36,player[Y]-10)!=(254,0,0):
                    player[X] +=1
                else:
                    player[X] -=1
                    
        def falling(player,vy):     #Checks every pixel in the y direction while in the air only
            for i in range(vy):
                if getcolor(mask,player[X],player[Y])!=(254,0,0):
                    player[Y] -=1
                else:
                    player[VY] +=1

        def death(g,v):
            global gokuhit,vegetahit,dead
            
            if blastrect1.collidepoint(g[X],g[Y]):          #player1 colliding with badguy and/or its projectiles
                gokuhit = "TRUE"
            elif friezarect1.collidepoint(g[X],g[Y]):
                gokuhit = "TRUE"
            elif blastrect2.collidepoint(g[X],g[Y]):
                gokuhit = "TRUE"
            elif friezarect2.collidepoint(g[X],g[Y]):
                gokuhit = "TRUE"
            elif blastrect3.collidepoint(g[X],g[Y]):
                gokuhit = "TRUE"
            elif friezarect3.collidepoint(g[X],g[Y]):
                gokuhit = "TRUE"
            elif g[Y] >=1875:
                gokuhit = "TRUE"
            elif g[Y] <= 0:
                gokuhit = "TRUE"

            if gokuhit == "TRUE":       #flag
                g[NMOVE] = DEATH        #death animation
                if g[FRAME] >= 3.8:     #when death animation is complete
                    g[FRAME] = 0
                    g[X],g[Y] = g[STARTX],g[STARTY]     #both players restart at beginning of level
                    v[X],v[Y] = v[STARTX],v[STARTY]
                    gokuhit = "FALSE"
                    dead = "FALSE"
                    player1[GRAV] = 1       #gravity is not flipped when restarting level

            if blastrect1.collidepoint(v[X],v[Y]):      #player1 colliding with badguy and/or its projectiles
                vegetahit = "TRUE"
            elif friezarect1.collidepoint(v[X],v[Y]):
                vegetahit = "TRUE"
            elif blastrect2.collidepoint(v[X],v[Y]):
                vegetahit = "TRUE"
            elif friezarect2.collidepoint(v[X],v[Y]):
                vegetahit = "TRUE"
            elif blastrect3.collidepoint(v[X],v[Y]):
                vegetahit = "TRUE"
            elif friezarect3.collidepoint(v[X],v[Y]):
                vegetahit = "TRUE"
            elif v[Y] >=1875:
                vegetahit = "TRUE"
            elif v[Y] <= 0:
                vegetahit = "TRUE"

            if vegetahit == "TRUE":
                v[NMOVE] = DEATH
                if v[FRAME] >= 3.8:
                    v[FRAME] = 0
                    g[X],g[Y] = g[STARTX],g[STARTY]
                    v[X],v[Y] = v[STARTX],v[STARTY]
                    vegetahit = "FALSE"
                    dead = "FALSE"
                    player2[GRAV] = 1

        def Rdeath(g,v):
            global Rgokuhit,Rvegetahit,Rdead
            
            if blastrect1.collidepoint(g[X],g[Y]):          #player1 colliding with badguy and/or its projectiles
                Rgokuhit = "TRUE"
            elif friezarect1.collidepoint(g[X],g[Y]):
                Rgokuhit = "TRUE"
            elif blastrect2.collidepoint(g[X],g[Y]):
                Rgokuhit = "TRUE"
            elif friezarect2.collidepoint(g[X],g[Y]):
                Rgokuhit = "TRUE"
            elif blastrect3.collidepoint(g[X],g[Y]):
                Rgokuhit = "TRUE"
            elif friezarect3.collidepoint(g[X],g[Y]):
                Rgokuhit = "TRUE"
            elif g[Y] >=1875:
                Rgokuhit = "TRUE"
            elif g[Y] <= 0:
                Rgokuhit = "TRUE"

            if Rgokuhit == "TRUE":       #flag
                g[NMOVE] = RDEATH        #death animation
                if g[FRAME] >= 3.8:     #when death animation is complete
                    g[FRAME] = 0
                    g[X],g[Y] = g[STARTX],g[STARTY]     #both players restart at beginning of level
                    v[X],v[Y] = v[STARTX],v[STARTY]
                    Rgokuhit = "FALSE"
                    Rdead = "FALSE"
                    player1[GRAV] = 1       #gravity is not flipped when restarting level

            if blastrect1.collidepoint(v[X],v[Y]):      #player1 colliding with badguy and/or its projectiles
                Rvegetahit = "TRUE"
            elif friezarect1.collidepoint(v[X],v[Y]):
                Rvegetahit = "TRUE"
            elif blastrect2.collidepoint(v[X],v[Y]):
                Rvegetahit = "TRUE"
            elif friezarect2.collidepoint(v[X],v[Y]):
                Rvegetahit = "TRUE"
            elif blastrect3.collidepoint(v[X],v[Y]):
                Rvegetahit = "TRUE"
            elif friezarect3.collidepoint(v[X],v[Y]):
                Rvegetahit = "TRUE"
            elif v[Y] >=1875:
                Rvegetahit = "TRUE"
            elif v[Y] <= 0:
                Rvegetahit = "TRUE"

            if Rvegetahit == "TRUE":
                v[NMOVE] = RDEATH
                if v[FRAME] >= 3.8:
                    v[FRAME] = 0
                    g[X],g[Y] = g[STARTX],g[STARTY]
                    v[X],v[Y] = v[STARTX],v[STARTY]
                    Rvegetahit = "FALSE"
                    Rdead = "FALSE"
                    player2[GRAV] = 1

        def playercollide(g,v,grect,vrect): #Players colliding with eachother
            keylist=key.get_pressed()       #keyboard
            
            if grect.collidepoint(v[X],v[Y]):       #if player1 rect collides with player2
                if g[Y] - v[Y] >= 10:               #player2 must be atleast 10 pixels higher than player1
                    v[Y] -= 1                       #player2 stays on top of player1
                    v[VY] = 0
                    if keylist[v[UP]]:              #Allows for player to jump while on top of other player
                        v[VY] = -15
                        
            if vrect.collidepoint(g[X],g[Y]):       #if player2 rect collides with player1      
                if v[Y] - g[Y] >= 10:
                    g[Y] -= 1
                    g[VY] = 0
                    if keylist[g[UP]]:
                        g[VY] = -15

        def Rplayercollide(g,v,grect,vrect):    #Players colliding while in reverse gravity
            keylist=key.get_pressed()
            
            if grect.collidepoint(v[X],v[Y]):   
                if g[Y] - v[Y] <= 10:
                    v[Y] += 1
                    v[VY] = 0
                    if keylist[v[UP]]:          
                        v[VY] = +15             #jumping
                
            if vrect.collidepoint(g[X],g[Y]):
                if v[Y] - g[Y] <= 10:
                    g[Y] += 1
                    g[VY] = 0
                    if keylist[g[UP]]:
                        g[VY] = +15          
            
        def moving(player):
            global dead
            keylist=key.get_pressed()       #keyboard

            player[NMOVE] = MSTAND          #Starting animation

            if keylist[player[RIGHT]] and dead!= "TRUE" and player[X]<=2353:    #key is pressed and player is not dying
                player[NMOVE] = MRIGHT       #moving right animation
                mright(player,10)           #move 10 pixels right
            elif keylist[player[LEFT]] and dead!= "TRUE" and player[X]>=25:
                player[NMOVE] = MLEFT       #moving left animation
                mleft(player,10)            #move 10 pixels left
            elif keylist[player[UP]] and dead!= "TRUE": 
                player[NMOVE] = MUP   #jumping animation
            elif blastrect1.collidepoint(player[X],player[Y]):  #player collides with blast
                dead = "TRUE"               #flag
                death(player1,player2)      #calls death function
            elif friezarect1.collidepoint(player[X],player[Y]): #player collides with badguy
                dead = "TRUE"
                death(player1,player2)
            elif blastrect2.collidepoint(player[X],player[Y]):
                dead = "TRUE"
                death(player1,player2)
            elif friezarect2.collidepoint(player[X],player[Y]):
                dead = "TRUE"
                death(player1,player2)
            elif blastrect3.collidepoint(player[X],player[Y]):
                dead = "TRUE"
                death(player1,player2)
            elif friezarect3.collidepoint(player[X],player[Y]):
                dead = "TRUE"
                death(player1,player2)
            else:
                if dead == "FALSE":
                    player[NMOVE] = MSTAND  #idle animation
                else:
                    death(player1,player2)  #calls death function
                    
            while red(getcolor(mask,player[X],player[Y])):  #while 
                player[VY] = 0
                player[Y] -= 1
                
            if keylist[player[UP]]:
                if player[VY] == 0 and red(getcolor(mask,player[X],player[Y]+30)):
                    player[VY]-=15
                    falling(player,player[VY])   #Change this value for hop

            if player[MOVE] == player[NMOVE]:     
                player[FRAME] = player[FRAME] + 0.2 
                if player[FRAME] >= len(gpics[player[MOVE]]):       #for gpics
                    player[FRAME] = 0
                if player[FRAME] >= len(vpics[player[MOVE]]):       #for vpics
                    player[FRAME] = 0
            elif player[NMOVE] != -1:     
                player[MOVE] = player[NMOVE]    
                player[FRAME] = 1
                
            player[VY] += 1                       #Added gravity
            player[Y] += player[VY]

            if player[Y]>1905:
                player[VY] = 0
                player[Y] = 1905

        def Rmoving(player):        #Moving with reverse gravity
            global Rdead
            keylist=key.get_pressed()

            player[NMOVE] = -1

            if keylist[player[RIGHT]] and Rdead!= "TRUE":
                player[NMOVE] = RRIGHT       #right
                mright(player,10)
            elif keylist[player[LEFT]] and Rdead!= "TRUE":
                player[NMOVE] = RLEFT       #left
                mleft(player,10)
            elif keylist[player[UP]] and Rdead!= "TRUE": 
                player[NMOVE] = RUP   #up
            elif blastrect1.collidepoint(player[X],player[Y]):
                Rdead = "TRUE"
                Rdeath(player1,player2)
            elif friezarect1.collidepoint(player[X],player[Y]):
                Rdead = "TRUE"
                Rdeath(player1,player2)
            elif blastrect2.collidepoint(player[X],player[Y]):
                Rdead = "TRUE"
                Rdeath(player1,player2)
            elif friezarect2.collidepoint(player[X],player[Y]):
                Rdead = "TRUE"
                Rdeath(player1,player2)
            elif blastrect3.collidepoint(player[X],player[Y]):
                Rdead = "TRUE"
                Rdeath(player1,player2)
            elif friezarect3.collidepoint(player[X],player[Y]):
                Rdead = "TRUE"
                Rdeath(player1,player2)
            else:
                if Rdead == "FALSE":
                    player[NMOVE] = RSTAND
                else:
                    Rdeath(player1,player2)         
                    
            while red(getcolor(reversemask,player[X],player[Y]-40)):
                player[VY] = 0
                player[Y] += 1
                
            if keylist[player[UP]]:
                if player[VY] == 0 and (red(getcolor(mask,player[X],player[Y]-50)) or player[Y]==0):
                    player[VY] = +15    #Change this value for hops


            if player[MOVE] == player[NMOVE]:     
                player[FRAME] = player[FRAME] + 0.2 
                if player[FRAME] >= len(gpics[player[MOVE]]):       #for gpics
                    player[FRAME] = 0
                if player[FRAME] >= len(vpics[player[MOVE]]):       #for vpics
                    player[FRAME] = 0
            elif player[NMOVE] != -2:     
                player[MOVE] = player[NMOVE]    
                player[FRAME] = 1
            player[VY] -= 1                       #Added gravity
            player[Y] += player[VY]
            if player[VY]<-40:
                player[VY]=-40
            
            if player[Y]<0:
                player[VY] = 0
                player[Y] = 0

        def shootleft(f,b,g,v):
            g[DIST] = g[X] - f[X]
            v[DIST] = v[X] - f[X]
            
            if v[DIST] < 0:
                f[NMOVE] = BLASTFL
            elif g[DIST] < 0:
                f[NMOVE] = BLASTFL
            else:
                f[NMOVE] = STANDFL
                b[FRAME] = 0
                
            if f[NMOVE] == BLASTFL:
                b[3] = 1
                b[NMOVE] = BLASTL
                mleft(b,10)
                b[FRAME] = b[FRAME] + 0.5
                if b[FRAME] >= 3:       
                     b[FRAME] = 3
                     f[FRAME] = 3
                     b[TIME] += 0.1
                     if b[TIME] >= 4:
                         b[FRAME] = 4
                         f[FRAME] = 5
                         b[TIME] += 0.1
                         if b[TIME] >=5:
                             b[TIME] = 0
                             b[X],b[Y] = b[STARTX],b[STARTY]
                             b[FRAME] = 0
                             f[NMOVE] = STANDFL
                
            elif f[NMOVE] != BLASTFL:
                b[3] = -1
                b[NMOVE] = -1
                b[X] = f[X]
                
            f[VY] += 1
            f[Y] += f[VY]

            while red(getcolor(mask,f[X],f[Y]+47)):
                f[VY] = 0
                f[Y] -= 1

            if f[MOVE] == f[NMOVE]:     
                f[FRAME] = f[FRAME] + 0.2 
                if f[FRAME] >= len(fpics[f[MOVE]]):       
                    f[FRAME] = 0
            elif f[NMOVE] != -1:     
                f[MOVE] = f[NMOVE]    
                f[FRAME] = 1

        def shootright(f,b,g,v):
            g[DIST] = g[X] - f[X]
            v[DIST] = v[X] - f[X]
            
            if v[DIST] > 0:
                f[NMOVE] = BLASTFR
            elif g[DIST] > 0:
                f[NMOVE] = BLASTFR
            else:
                f[NMOVE] = STANDFR
                b[FRAME] = 0
                
            if f[NMOVE] == BLASTFR:
                b[X],b[Y] = f[X],f[Y]
                b[STARTX],b[STARTY] = f[X],f[Y]
                b[3] = 1
                b[NMOVE] = BLASTR
                mright(b,10)
                b[FRAME] = b[FRAME] + 0.5
                if b[FRAME] >= 3:       
                     b[FRAME] = 3
                     f[FRAME] = 3
                     b[TIME] += 0.1
                     if b[TIME] >= 6:
                         b[FRAME] = 4
                         f[FRAME] = 5
                         b[TIME] += 0.1
                         if b[TIME] >=8:
                             b[TIME] = 0
                             b[X],b[Y] = b[STARTX],b[STARTY]
                             b[FRAME] = 0
                             f[NMOVE] = STANDFR
                
            elif f[NMOVE] != BLASTFR:
                b[3] = -1
                b[NMOVE] = -1
                b[X] = f[X]
                
            f[VY] += 1
            f[Y] += f[VY]

            while red(getcolor(mask,f[X],f[Y]+47)):
                f[VY] = 0
                f[Y] -= 1

            if f[MOVE] == f[NMOVE]:     
                f[FRAME] = f[FRAME] + 0.2 
                if f[FRAME] >= len(fpics[f[MOVE]]):       
                    f[FRAME] = 0
            elif f[NMOVE] != -1:     
                f[MOVE] = f[NMOVE]    
                f[FRAME] = 1

        def Rshootleft(f,b,g,v):
            g[DIST] = g[X] - f[X]
            v[DIST] = v[X] - f[X]
            
            if v[DIST] < 0:
                f[NMOVE] = RBLASTFL
            elif g[DIST] < 0:
                f[NMOVE] = RBLASTFL
            else:
                f[NMOVE] = RSTANDFL
                b[FRAME] = 0
                
            if f[NMOVE] == RBLASTFL:
                b[3] = 1
                b[NMOVE] = RBLASTL
                mleft(b,10)
                b[FRAME] = b[FRAME] + 0.5
                if b[FRAME] >= 3:       
                     b[FRAME] = 3
                     f[FRAME] = 3
                     b[TIME] += 0.1
                     if b[TIME] >= 4:
                         b[FRAME] = 4
                         f[FRAME] = 5
                         b[TIME] += 0.1
                         if b[TIME] >=5:
                             b[TIME] = 0
                             b[X],b[Y] = b[STARTX],b[STARTY]
                             b[FRAME] = 0
                             f[NMOVE] = RSTANDFL
                
            elif f[NMOVE] != RBLASTFL:
                b[3] = -1
                b[NMOVE] = -1
                b[X] = f[X]
                
            f[VY] -= 1
            f[Y] += f[VY]

            while red(getcolor(mask,f[X],f[Y]+10)):
                f[VY] = 0
                f[Y] += 1

            if f[MOVE] == f[NMOVE]:     
                f[FRAME] = f[FRAME] + 0.2 
                if f[FRAME] >= len(fpics[f[MOVE]]):       
                    f[FRAME] = 0
            elif f[NMOVE] != -1:     
                f[MOVE] = f[NMOVE]    
                f[FRAME] = 1
            
        def sprite(name,start,end):
            move=[]
            for i in range(start,end+1):
                move.append(image.load("%s/%s%d.png" % (name,name,i)))
            return move

        gpics=[]
        gpics.append(sprite("standG",0,3))
        gpics.append(sprite("moveRG",0,3)) #Change these back
        gpics.append(sprite("moveLG",0,3))
        gpics.append(sprite("jumpG",0,4))
        gpics.append(sprite("RstandG",0,3))
        gpics.append(sprite("RmoveRG",0,3))
        gpics.append(sprite("RmoveLG",0,3))
        gpics.append(sprite("RjumpG",0,4))
        gpics.append(sprite("deathG",0,3))
        gpics.append(sprite("RdeathG",0,3))

        vpics=[]
        vpics.append(sprite("StandV",0,3))
        vpics.append(sprite("MoveRV",0,2))
        vpics.append(sprite("MoveLV",0,2))
        vpics.append(sprite("JumpV",0,2))
        vpics.append(sprite("RstandV",0,3))
        vpics.append(sprite("RmoveRV",0,2))
        vpics.append(sprite("RmoveLV",0,2))
        vpics.append(sprite("RjumpV",0,2))
        vpics.append(sprite("deathV",0,3))
        vpics.append(sprite("RdeathV",0,3))

        fpics = []
        fpics.append(sprite("standFR",0,5))
        fpics.append(sprite("blastFR",0,5))
        fpics.append(sprite("blastFL",0,4))
        fpics.append(sprite("RblastFR",0,5))
        fpics.append(sprite("RblastFL",0,5))
        fpics.append(sprite("standFL",0,5))
        fpics.append(sprite("RstandFR",0,5))
        fpics.append(sprite("RstandFL",0,5))

        blastpics = []
        blastpics.append(sprite("blastL",0,4))
        blastpics.append(sprite("blastL",0,4))
        blastpics.append(sprite("RblastR",0,4))
        blastpics.append(sprite("RblastL",0,4))

        MSTAND=0
        MRIGHT=1
        MLEFT=2
        MUP=3
        RSTAND=4
        RRIGHT=5
        RLEFT=6
        RUP=7
        DEATH = 8
        RDEATH = 9

        STANDFR = 0
        BLASTFR = 1
        BLASTFL = 2
        RBLASTFR = 3
        RBLASTFL = 4
        STANDFL = 5
        RSTANDFR = 6
        RSTANDFL = 7

        BLASTR = 0
        BLASTL = 1
        RBLASTR = 2
        RBLASTL = 3

        screen=display.set_mode((1000,600))
        running3=True
        screenX,screenY = 0,0
        WORLDY = 1450
        while running3:
            for e in event.get():
                if e.type==QUIT:
                    running3=False
            mb=mouse.get_pressed()
            mx,my=mouse.get_pos()
            mpos=mx,my

            player1[GTIME] += 0.1
            player2[GTIME] += 0.1

            blastrect1 = Rect((blast1[X]-15,blast1[Y]+20,40,40))
            friezarect1 = Rect((frieza1[X]-10,frieza1[Y]-50,40,100))
            blastrect2 = Rect((blast2[X]-15,blast2[Y]+20,70,40))
            friezarect2 = Rect((frieza2[X]-10,frieza2[Y]-50,40,100))
            blastrect3 = Rect((blast3[X]-15,blast3[Y]+20,70,40))
            friezarect3 = Rect((frieza3[X]-10,frieza3[Y]-50,40,100))
            
            gokurect = Rect((player1[X]-20,player1[Y]-50,40,100))
            vegetarect = Rect((player2[X]-20,player2[Y]-50,40,100))


            scene(player1,player2,blast1,blast2,blast3,frieza1,frieza2,frieza3)

            

            Rshootleft(frieza1,blast1,player1,player2)
            shootleft(frieza2,blast2,player1,player2)
            shootleft(frieza3,blast3,player1,player2)

            if player1[GRAV]==1:
                moving(player1)
                playercollide(player1,player2,gokurect,vegetarect)
            if player2[GRAV]==1:
                moving(player2)

            if player1[GRAV]==-1:
                Rmoving(player1)
                Rplayercollide(player1,player2,gokurect,vegetarect)
            if player2[GRAV]==-1:
                Rmoving(player2)

            if player1[X]>=2283 and player2[X]>=2283:
                if player1[Y]>=500 and player2[Y]>=500:
                    level3c="complete"
                    level="4"
                    running3=False

            myClock.tick(30)

            display.flip()
    if level=="4":
        screen.blit(ending,(0,0))
    display.flip()
quit()

