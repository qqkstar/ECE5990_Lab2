#XiaoXing Zhao (xz254)
#William Voge  (wjv29)
#Lab 2
#Edited 3/10/2016
import RPi.GPIO as GPIO
from subprocess import call
import time

ended = False

def main():
  GPIO.setmode(GPIO.BCM)    #set up GPIO pins
  GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)  #set pins 17. 22, 23, 27, 13, 6 as pull up 
  GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  GPIO.add_event_detect(17, GPIO.FALLING, callback=pin_17_cb, bouncetime=200)   #set up callback and bouncetime for each pin
  GPIO.add_event_detect(22, GPIO.FALLING, callback=pin_22_cb, bouncetime=200)
  GPIO.add_event_detect(23, GPIO.FALLING, callback=pin_23_cb, bouncetime=200)
  GPIO.add_event_detect(13, GPIO.FALLING, callback=pin_13_cb, bouncetime=200)
  GPIO.add_event_detect(6, GPIO.FALLING, callback=pin_6_cb, bouncetime=200)
  GPIO.add_event_detect(27, GPIO.FALLING, callback=pin_27_cb, bouncetime=200)

  p=0
  time_stamp = time.time()
  while (time.time()-time_stamp <= 10) and not ended:     #set up time stamp of 10 seconds for the program to run
    p = p^1   #do something in while loop

def pin_17_cb(channel):     #call back function if the pin is pressed
  call("echo 'pause' > ~/Documents/lab2/video_fifo", shell=True)    #issue the appropriate command to video fifo

def pin_22_cb(channel):
  call("echo 'seek 10 0' > ~/Documents/lab2/video_fifo", shell=True)

def pin_23_cb(channel):
  call("echo 'seek -10 0' > ~/Documents/lab2/video_fifo", shell=True)

def pin_13_cb(channel):
  call("echo 'seek 30 0' > ~/Documents/lab2/video_fifo", shell=True)

def pin_6_cb(channel):
  call("echo 'seek -30 0' > ~/Documents/lab2/video_fifo", shell=True)

def pin_27_cb(channel):
  call("echo 'quit' > ~/Documents/lab2/video_fifo", shell=True)
  ended = True

if __name__=='__main__':
  main()


