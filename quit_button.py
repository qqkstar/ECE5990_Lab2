#XiaoXing Zhao (xz254)
#William Voge  (wjv29)
#Lab 2
#Edited 3/10/2016
import pygame
import sys
import os

os.environ['SDL_VIDEODRIVER'] = 'fbcon'	#os environment setting to set up videodriver for TFT
os.environ['SDL_FBDEV'] = '/dev/fb1'	#set display device to TFT
os.environ['SDL_MOUSEDEV'] = '/dev/input/touchscreen' #set mouse input as touchscreen input
os.environ['SDL_MOUSEDRV'] = 'TSLIB'		#set mouse driver

black = 0, 0, 0

pygame.init()

size = width, height = 320, 240
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 36)
quit_text = font.render("QUIT",1,(255,250,255))		#display QUIT text with specified RGB value
q_text_pos = quit_text.get_rect()
q_text_pos.centerx = screen.get_rect().centerx		# set text position as middle of display
q_text_pos.centery = screen.get_rect().centery

while 1:
  for event in pygame.event.get():		#poll for events while program is running
    if event.type == pygame.MOUSEBUTTONDOWN:	#if touch screen is pressed, quit program
      sys.exit()
  screen.fill(black)		#clear screnn	
  screen.blit(quit_text, q_text_pos)		#display text at pixel locations
  pygame.display.flip()		#refresh pixel values
