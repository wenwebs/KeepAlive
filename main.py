from turtle import color
from pkg_resources import safe_extra
import pygame as pyg  #载入pygame并缩写为pyg
import time
import sys
import configparser
from pygame.locals import *
#-----------------------------------------------------------------------------------------------------------------------#

pyg.init()  #初始化pygame
WinSize = [1280,720]
screen = pyg.display.set_mode(WinSize)  #设置窗口大小
clock = pyg.time.Clock()
pyg.display.set_caption("生存末日-Verson.Alpha.1    -By MWX")  #设置标题
pyg.mixer.init()

#初始化颜色
white = 255,255,255
green = 0,255,0
blue = 0,0,128
black = 0,0,0

def  drawText(content, x, y, color):
    pyg.font.init()
    font  =  pyg.font.Font('gameFont.ttf',60)
    text  =  font.render(content,True,pyg.Color(color))
    screen.blit(text,(x,y))

#读写文件
def flieget(flie, wr, content):
    f = open(flie, 'r')
    print(f.read())
    f.close()
    if wr == 1:
        f = open(flie, 'w')
        f.write(content)
        f.close()

#导入背景：
bg = pyg.image.load('img/hbg.png')
bg = pyg.transform.scale(bg,(1280,720))
aboutbg = pyg.image.load('img/aboutbg.png')
Gbg = pyg.image.load('img/gameBg.png')
Gbg = pyg.transform.scale(Gbg,(1280,720))



#导入背景音乐
bgm = pyg.mixer.music.load('Gsound/bgm.mp3')


#导入按钮
start1 = pyg.image.load('img/start-off.png')
start2 = pyg.image.load('img/start-on.png')
Mui1 = pyg.image.load('img/music-on.png')
Mui2 = pyg.image.load('img/music-off.png')
quitUI = pyg.image.load('img/quit.png')
quitUI1 = pyg.image.load('img/quit-1.png')
about1 = pyg.image.load('img/about-off.png')
about2 = pyg.image.load('img/about-on.png')

#初始化变量
start = 0
music = 1
about = 0
quit = 0
startUIx = 770
startUIy = 275
aboutUIx = 770
aboutUIy = 350
mUIx = 1225
mUIy = 10
quitUIy = 60
page = 1







    

#打开页面
def opabout(load):
    page = 2
    screen.fill((white))
    screen.blit(aboutbg,(0,0))
    screen.blit(quitUI,(1225,10))
    pyg.mixer.music.pause()
    
    
def opstart(load):   
    page = 3
    f = open('username.txt')
    UserName = f.read()
    screen.fill((white))
    screen.blit(Gbg,(0,0))
    drawText(用户名： + UserName,1000,60,white)
    pyg.mixer.music.pause()









#初始化窗口及刷新屏幕
def Winload(load):
    if load == 1:
        #初始化屏幕
        screen.blit(bg,(0,0))
        screen.blit(start1,(770,275))
        screen.blit(about1,(770,350))
        screen.blit(Mui1,(1225,10))    
        screen.blit(quitUI,(1225,60))
    pyg.display.flip()
    if load == 2:
        screen.fill((white)) #将屏幕覆盖
        #刷新屏幕
        screen.blit(bg,(0,0))
        if about == 0:
            screen.blit(about1,(770,350))
        else:
            screen.blit(about2,(770,350))        
        if start == 0:
            screen.blit(start1,(770,275))
        else:
            screen.blit(start2,(770,275))
        if music == 1:
            screen.blit(Mui1,(1225,10))
        else:
            screen.blit(Mui2,(1225,10))
        if quit == 0:
            screen.blit(quitUI,(1225,60))        
        else:
            screen.blit(quitUI1,(1225,60))
    pyg.display.flip()

Winload(1)
pyg.mixer.music.play()
aboutopen = 0
gameopen = 0
flieget('site.txt', 1, '0')


#长方形UI长105宽50
#正方形UI长45宽40

#关闭页面
done = False
while not done:

    pX,pY = pyg.mouse.get_pos()
    for event in pyg.event.get():
             
        if event.type == pyg.MOUSEBUTTONDOWN:
            if page == 1:    
                if pX >= startUIx and startUIy >= 275 and pX < startUIx + 105 and pY < startUIy + 50:   
                    start = 1
                    print('start')
                    Winload(2)
                    time.sleep(0.1)
                    start = 0
                    Winload(2)
                    opstart(1)
                if pX >= aboutUIx and pY >= aboutUIy and pX < aboutUIx + 105 and pY < aboutUIy + 50:
                    about = 1
                    print('about')
                    Winload(2)
                    time.sleep(0.1)
                    about = 0
                    Winload(2)
                    opabout(1)
                if pX >= mUIx and pY >= mUIy and pX < mUIx + 45 and pY < mUIy + 40:
                        if music == 1:
                            pyg.mixer.music.pause()
                            music = 0
                            Winload(2)
                        else:
                            pyg.mixer.music.unpause()
                            music = 1
                            Winload(2)
                if pX >= mUIx and pY >= quitUIy and pX < mUIx + 45 and pY < quitUIy + 40:
                        quit = 0
                        Winload(2)
                        time.sleep(0.1)
                        quit = 1
                        Winload(2)
                        done = True
            if page == 2:
                if pX >= mUIx and pY >= mUIy and pX < mUIx + 45 and pY < mUIy + 40:                    
                    time.sleep(0.5)
                    Winload(1)
                    page = 1
        

                    

            print(pX,pY)
                  
    pyg.display.flip()
    pyg.display.update()    

pyg.quit()
sys.exit()