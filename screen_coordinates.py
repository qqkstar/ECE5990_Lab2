#XiaoXing Zhao (xz254)
#William Voge  (wjv29)
#Lab 2
#Edited 3/10/2016
import pygame
import sys
import os

os.environ['SDL_VIDEODRIVER'] = 'fbcon'
os.environ['SDL_FBDEV'] = '/dev/fb1'
os.environ['SDL_MOUSEDEV'] = '/dev/input/touchscreen'
os.environ['SDL_MOUSEDRV'] = 'TSLIB'

black = 0, 0, 0

pygame.init()

size = width, height = 320, 240
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 20)
quit_text = font.render("QUIT",1,(255,250,255))
q_text_pos = quit_text.get_rect()
q_text_pos.centerx = screen.get_rect().centerx
q_text_pos.centery = screen.get_rect().centery + 100
coord = font.render('No press recorded',1,(255,255,255))

while 1:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:  #capture touch screen press event
      p = pygame.mouse.get_pos()    #set p as position of touch screen
      coord = font.render('Hit at ' + `p`,1,(255,255,255))    #display tuple at pixel location
      print `p`
      if p[0]>124 and p[0]<190 and p[1]>207 and p[1]<231:   #detect if quit button is pressed by checking range of pixel locations
        sys.exit()
    elif event.type == pygame.KEYDOWN:
      sys.exit()

  screen.fill(black)
  screen.blit(quit_text, q_text_pos)
  screen.blit(coord, (0, 0))
  pygame.display.flip()
