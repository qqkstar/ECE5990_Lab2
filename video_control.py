
#XiaoXing Zhao (xz254)
#William Voge  (wjv29)
#Lab 2
#Edited 3/10/2016

import RPi.GPIO as GPIO
from subprocess import call
import time

def main():
  GPIO.setmode(GPIO.BCM)	#prepare the GPIO pins
  GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)	#set GPIO pins 17, 22, 23, 27, 13, 6 as pull up
  GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  print "waiting for button press"		
  in_22 = 1		#state variables for each button
  in_23 = 1
  in_27 = 1
  in_17 = 1
  in_13 = 1
  in_6 = 1

  prev_in_17 = 1	#previous state variable for each button as a debounce mechanism
  prev_in_22 = 1
  prev_in_23 = 1
  prev_in_13 = 1
  prev_in_6 = 1
  prev_in_27 = 1
  
  time_stamp = time.time()		#create a time stamp that would stop the program after 10 seconds
  while time.time()-time_stamp <= 10:	#Enter a polling while loop
  #  time.sleep(0.00002)
    in_17 = GPIO.input(17)		# Set each button state variable if the button is pressed 
    in_22 = GPIO.input(22)
    in_23 = GPIO.input(23)
    in_27 = GPIO.input(27)
    in_13 = GPIO.input(13)
    in_6  = GPIO.input(6)
 
    if(not (in_17) and prev_in_17):		#Poll to check whether each button is pressed, debounce by checking the prev state of the button 
      print "17 Pressed"
      call("echo 'pause' > ~/Documents/lab2/video_fifo", shell=True)   #issue a fifo command via subprocess
    if(not (in_22) and prev_in_22):
      print "22 Pressed"
      call("echo 'seek 10 0' > ~/Documents/lab2/video_fifo", shell=True)
    if(not (in_23) and prev_in_23):
      print "23 Pressed"
      call("echo 'seek -10 0' > ~/Documents/lab2/video_fifo", shell=True)
    if(not (in_13) and prev_in_13):
      print "13 Pressed"
      call("echo 'seek 30 0' > ~/Documents/lab2/video_fifo", shell=True)
    if(not (in_6) and prev_in_6):
      print "6 Pressed"
      call("echo 'seek -30 0' > ~/Documents/lab2/video_fifo", shell=True)
    if(not (in_27) and prev_in_27):
      print "27 Pressed"
      call("echo 'quit' > ~/Documents/lab2/video_fifo", shell=True)
      break

    prev_in_17 = in_17			# set the debounce variables
    prev_in_22 = in_22
    prev_in_23 = in_23
    prev_in_27 = in_27
    prev_in_13 = in_13
    prev_in_6 = in_6

if __name__=='__main__':
  main()
