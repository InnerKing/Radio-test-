#Imports#
import pygame
from time import sleep
from sys import exit
import RPi.GPIO as GPIO
radioIndex = 1

  
#Buttons#
GPIO.setmode(GPIO.BOARD)

#Changing Song Buttons#
channelDown=15
channelUp=13
GPIO.setup(channelDown, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(channelUp, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#Volume Buttons#
volumeDown=12
volumeUp=11
GPIO.setup(volumeDown, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(volumeUp, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#Play/Pause Buttons#
pauseButton=10
playButton=8
GPIO.setup(pauseButton, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(playButton, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#File Setup#
path = '/home/pi/Desktop/Python/General Songs/'
playlist = ['bones.mp3', 'Brass monkey.mp3', 'dancin.mp3']

#def checkPressed():
 
#Volume#
pygame.mixer.init()
speaker_volume = 100
pygame.mixer.music.set_volume(speaker_volume)

while (True):

        #Changing Stations#
        if GPIO.input(channelDown)==0 and radioIndex > 0:
            print('Channel Down')
            radioIndex -= 1
            pygame.mixer.music.load(path + playlist[radioIndex])
            pygame.mixer.music.play()
            sleep(0.3)
            
            
        if GPIO.input(channelUp)==0 and radioIndex < len(playlist)-1:
            print('Channel Up')
            radioIndex += 1
            pygame.mixer.music.load(path + sound_files[radioIndex])
            pygame.mixer.music.play()
            sleep(0.3)
            
        #Changing Volume#
        if GPIO.input(volumeDown)==0 and speaker_volume > 0:
            print('Volume Down')
            speaker_volume -= 10
            pygame.mixer.music.set_volume(speaker_volume/100)
            print("Volume: " + str(speaker_volume)+"%")
            sleep(0.3)
            
        if GPIO.input(volumeUp)==0 and speaker_volume < 100:
            print('Volume Up')
            speaker_volume += 10
            pygame.mixer.music.set_volume(speaker_volume/100)
            print("Volume: " + str(speaker_volume)+"%")
            sleep(0.3)
            
        #Play/Pause#
        if GPIO.input(pauseButton)==0:
            print('Music Paused')
            pygame.mixer.music.pause()
            sleep(0.3)
        if GPIO.input(playButton)==0:
            print('Music Played')
            pygame.mixer.music.play()
            sleep(0.3) 

GPIO.cleanup()


#Stopping Songs Double Playing#
for playlist in playlists:
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy()==True:
        continue
