#XiaoXing Zhao (xz254)
#William Voge  (wjv29)
#Lab 2
#Edited 3/10/2016
import pygame
import sys
import os

os.environ['SDL_VIDEODRIVER'] = 'fbcon'   #set up os environment to display to TFT
os.environ['SDL_FBDEV'] = '/dev/fb1'
os.environ['SDL_MOUSEDEV'] = '/dev/input/touchscreen' #set up touchscreen as mouse input
os.environ['SDL_MOUSEDRV'] = 'TSLIB'

black = 0, 0, 0

pygame.init()
#pygame.mouse.set_visible(False)

size = width, height = 320, 240
screen = pygame.display.set_mode(size)
speed1 = [1, 2]
speed2 = [2, 1]

ball1 = pygame.image.load("ball.bmp")   #set up ball 
ball2 = pygame.image.load("ball.bmp")
ball1 = pygame.transform.scale(ball1, (40,40))
ball2 = pygame.transform.scale(ball2, (40,40))
ballrect1 = ball1.get_rect()
ballrect2 = ball2.get_rect()
ballrect2.centerx = 200
ballrect2.centery = 100

font = pygame.font.Font(None, 20)

quit_text = font.render("QUIT",1,(255,250,255))   #set up texts as buttons
q_text_pos = quit_text.get_rect()
q_text_pos.centerx = screen.get_rect().centerx + 100
q_text_pos.centery = screen.get_rect().centery + 100

start_text = font.render("START",1,(255,250,255))
s_text_pos = start_text.get_rect()
s_text_pos.centerx = screen.get_rect().centerx - 100
s_text_pos.centery = screen.get_rect().centery + 100

pause_text = font.render("Pause",1,(255,250,255))
p_text_pos = start_text.get_rect()
p_text_pos.centerx = 70
p_text_pos.centery = 220

fast_text = font.render("Fast",1,(255,250,255))
f_text_pos = start_text.get_rect()
f_text_pos.centerx = 140
f_text_pos.centery = 220

slow_text = font.render("Slow",1,(255,250,255))
sl_text_pos = start_text.get_rect()
sl_text_pos.centerx = 200
sl_text_pos.centery = 220

back_text = font.render("Back",1,(255,250,255))
b_text_pos = start_text.get_rect()
b_text_pos.centerx = 260
b_text_pos.centery = 220

start = False
count = 0
pause = 0
time_div = 100      #time div controls how many iterations of the while loop until new ball location is calculated

while 1:
  count += 1
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      p = pygame.mouse.get_pos()
      if not start and p[0]>240 and p[0]<285 and p[1]>200 and p[1]<220:   #touch screen button press detection logic
        sys.exit()
      elif not start and p[0]>35 and p[0]<80 and p[1]>200 and p[1]<220:
        start = True
      elif start and p[0]>50 and p[0]<90 and p[1]>200 and p[1]<230:
        pause ^= 1 
      elif start and p[0]>120 and p[0]<160 and p[1]>200 and p[1]<230:
        time_div -= 20
        if time_div <= 3:
          time_div = 3
      elif start and p[0]>180 and p[0]<220 and p[1]>200 and p[1]<230:
        time_div += 50
        if time_div > 300:
          time_div = 300
      elif start and p[0]>240 and p[0]<280 and p[1]>200 and p[1]<230:
        start = False
    elif event.type == pygame.KEYDOWN:
      sys.exit()
  if count > time_div and not pause:      #ball collision logic
          count = 0
          ballrect1 = ballrect1.move(speed1)
          ballrect2 = ballrect2.move(speed2)
 
          if ballrect1.left < 0 or ballrect1.right > width:
            speed1[0] = -speed1[0]
          if ballrect1.top < 0 or ballrect1.bottom > height:
            speed1[1] = -speed1[1]

          if ballrect2.left < 0 or ballrect2.right > width:
            speed2[0] = -speed2[0]
          if ballrect2.top < 0 or ballrect2.bottom > height:
            speed2[1] = -speed2[1]

          if (ballrect1.left < ballrect2.right
           and ballrect1.right >  ballrect2.left
           and ballrect1.top < ballrect2.bottom
           and ballrect1.bottom > ballrect2.top):
            speed1[0], speed2[0] = speed2[0], speed1[0]
            speed1[1], speed2[1] = speed2[1], speed1[1]
                

  screen.fill(black)
  screen.blit(quit_text, q_text_pos)
  screen.blit(start_text, s_text_pos)
  if start:         #pygram refresh screen logic
    screen.fill(black)
    screen.blit(pause_text, p_text_pos)
    screen.blit(fast_text, f_text_pos)
    screen.blit(slow_text, sl_text_pos)
    screen.blit(back_text, b_text_pos)
    screen.blit(ball1, ballrect1)
    screen.blit(ball2, ballrect2)
  pygame.display.flip()
