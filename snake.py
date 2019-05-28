
  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
#!/usr/bin/env python
# -*-coding:utf-8-*-
import pygame,sys
import win32api,win32console,win32gui,codecs
import time,random
from pygame.sprite import Sprite

pygame.init()

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height = 600

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Flafel")

icon=pygame.image.load("apple.png")
pygame.display.set_icon(icon)

img=pygame.image.load("snakehead.png")
appleimg=pygame.image.load("apple.png")

clock = pygame.time.Clock()

AppleThickness=30
block_size = 20
FPS = 15

direction="right"

smallfont = pygame.font.SysFont("comicsansms",25)
medfont = pygame.font.SysFont("comicsansms",50)
largefont = pygame.font.SysFont("comicsansms",80)

pygame.mixer.init()
intro_sound=pygame.mixer.Sound("intro.wav")
dead_sound=pygame.mixer.Sound("dead.wav")

def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    intro=False
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        
        message_to_screen("Welcome to Flafel",green,-100,"large")
        message_to_screen("The objective of the game is to eat red apples",black,-30)
        message_to_screen("The more apples you eat,the longer you get",black,10)
        message_to_screen("If you run into yourself, or the edges, you die!",black,50)
        message_to_screen("Press C to play, P to pause or Q to quit",black,180)
        pygame.display.update()
        clock.tick(15)

def pause():

    paused=True
    
    message_to_screen("Paused",black,-100,size="large")
    message_to_screen("Press C to continue or Q to quit",black,25)

    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    paused=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        
        clock.tick(5)
    
def score(score):

    text=smallfont.render("Score: "+str(score),True,black)
    gameDisplay.blit(text,[0,0])

    
def randAppleGen():

    randApplex = round(random.randrange(0,display_width-AppleThickness))#/10.0)*10.0
    randAppley = round(random.randrange(0,display_height-AppleThickness))#/10.0)*10.0
    return randApplex,randAppley

def snake(block_size,snakeList):

    if direction=="right":
        head=pygame.transform.rotate(img,270)
    if direction=="left":
        head=pygame.transform.rotate(img,90)
    if direction=="up":
        head=img
    if direction=="down":
        head=pygame.transform.rotate(img,180)

    gameDisplay.blit(head,(snakeList[-1][0],snakeList[-1][1]))

    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, (XnY[0],XnY[1],block_size,block_size))
    
def text_objects(text,color,size):

    if size=="small":
        textSurface=smallfont.render(text,True,color)
    elif size=="medium":
        textSurface=medfont.render(text,True,color)
    elif size=="large":
        textSurface=largefont.render(text,True,color)
    return textSurface,textSurface.get_rect()
    
def message_to_screen(msg,color,y_displace=0,size="small"):

    textSurf,textRect=text_objects(msg,color,size)
    textRect.center=(display_width/2),(display_height/2)+y_displace
    gameDisplay.blit(textSurf,textRect)
    


def gameLoop():

    global direction

    direction="right"
    running = True
    gameOver= False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeList=[]
    snakeLength=1

    randApplex,randAppley=randAppleGen()
    
    while running:
        if gameOver==True:
            message_to_screen("Game over",red,-50,size="large")
            message_to_screen("Press C to play again or Q to quit",black,50,size="medium")
            pygame.display.update()
            
        while gameOver == True:
            #gameDisplay.fill(white)
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameOver=False
                    running=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        running=False
                        gameOver=False
                    if event.key==pygame.K_c:
                        gameLoop()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction="left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction="right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction="up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction="down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key==pygame.K_p:
                    pause()
        if lead_x>=display_width or lead_x<0 or lead_y<0 or lead_y>=display_height:
           gameOver=True
           dead_sound.play()


        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)

        gameDisplay.blit(appleimg,(randApplex,randAppley))

        
        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList)>snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment==snakeHead:
                gameOver=True
                dead_sound.play()
                
                
        snake(block_size,snakeList)

        score(snakeLength-1)

        
        pygame.display.update()

       
        if lead_x>randApplex and lead_x <randApplex+AppleThickness or lead_x+block_size>randApplex and lead_x+block_size<randApplex+AppleThickness:
            if lead_y>randAppley and lead_y <randAppley+AppleThickness:
                randApplex,randAppley=randAppleGen()
                snakeLength+=1
            elif lead_y+block_size > randAppley and lead_y+block_size<randAppley+AppleThickness:
                randApplex,randAppley=randAppleGen()
                snakeLength+=1

        clock.tick(FPS)
    
    pygame.quit()
    quit()
intro_sound.play()
game_intro()
intro_sound.stop()
gameLoop()