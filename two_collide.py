#XiaoXing Zhao (xz254)
#William Voge  (wjv29)
#Lab 2
#Edited 3/10/2016
import sys, pygame
import RPi.GPIO as GPIO
from subprocess import call

ended = 0

pygame.init()

def pin_17_cb(channel):
  call("kill -9 $(pidof python two_collide.py)", shell=True)
  ended = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(17, GPIO.FALLING, callback=pin_17_cb, bouncetime=200)

size = width, height = 320, 240
speed1 = [1, 1]
speed2 = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball1 = pygame.image.load("ball.bmp")
ball2 = pygame.image.load("ball.bmp")
ballrect1 = ball1.get_rect()
ballrect2 = ball2.get_rect()
ballrect2.centerx = 200
ballrect2.centery = 100


while not ended:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

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
  screen.blit(ball1, ballrect1)
  screen.blit(ball2, ballrect2)
  pygame.display.flip()
