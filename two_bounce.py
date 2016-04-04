#XiaoXing Zhao (xz254)
#William Voge  (wjv29)
#Lab 2
#Edited 3/10/2016
import sys, pygame
pygame.init()

size = width, height = 1280, 800    #declare screen size
speed1 = [4, 1]   #set ball speed
speed2 = [2, 3]
black = 0, 0, 0    # set black RGB value

screen = pygame.display.set_mode(size)   #set display size as indicated

ball1 = pygame.image.load("ball.bmp")     # load ball bmp file
ball2 = pygame.image.load("ball.bmp")
ballrect1 = ball1.get_rect()        #get rectangel coordinates around ball
ballrect2 = ball2.get_rect()

while 1:
  for event in pygame.event.get():  #check for game event if it's quit
    if event.type == pygame.QUIT: sys.exit()

  ballrect1 = ballrect1.move(speed1)  #move ball according to speed
  ballrect2 = ballrect2.move(speed2)
  if ballrect1.left < 0 or ballrect1.right > width:     # logic to detect ball collisiont to screen walls
    speed1[0] = -speed1[0]
  if ballrect1.top < 0 or ballrect1.bottom > height:
    speed1[1] = -speed1[1]

  if ballrect2.left < 0 or ballrect2.right > width:
    speed2[0] = -speed2[0]
  if ballrect2.top < 0 or ballrect2.bottom > height:
    speed2[1] = -speed2[1]


  screen.fill(black)              #clear the screen
  screen.blit(ball1, ballrect1)    #set the new pixel values of where the ball will be
  screen.blit(ball2, ballrect2)
  pygame.display.flip()             #refresh the screen
