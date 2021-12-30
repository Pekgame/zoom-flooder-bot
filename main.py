# -*- coding: utf-8 -*- #

print('Loading...')
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
from os import system
from keyboard import is_pressed
from time import sleep
system('cls')
print('Loaded Zoom Flooder Bot V0.1 Beta')

#Setting up

defualt = open('defualt.txt', 'r').read()
defualt = defualt.split('\n')
meetingID = str(input('Meeting ID(Blank for Defualt): '))
if len(meetingID) == 0:
    meetingID = defualt[0]
meetingPasscode = str(input('Meeting Passcode(Blank for Defualt): '))
if len(meetingPasscode) == 0:
    meetingPasscode = defualt[1]
numberOfBots = int(input('Bot(s) Number: '))
customName = input('Name(Leave a blank for Random name): ')
system('cls')

#Import random name

f = []
f = open('names.txt', 'r').read()
f = f.split('\n')

#Option

drivers = []
options = Options()
options.add_argument('--log-level=3') #Disable Log
options.add_argument("--disable-infobars") #Disable anoying info
options.add_argument("start-maximized") #Maximize when opened
options.add_argument("--disable-extensions") #Disable antivirus to make it broken

#Disable Webcams and Microphone

options.add_experimental_option("prefs", {
   \
   "profile.default_content_setting_values.media_stream_mic": 2,
   "profile.default_content_setting_values.media_stream_camera": 2
})
options.add_argument("--mute-audio") #Mute all tabs(Else if you had 2 bots or more, It will broke your pc :o)
options.add_argument("--headless") #Not to see bot screen

#Creating bot(s)

for i in range(numberOfBots):
    baseName = random.choice(f)
    print('Please ignore the warning!')
    drivers.append(webdriver.Chrome(executable_path='chromedriver.exe', options=options))
    drivers[i].get(f'https://zoom.us/wc/join/{meetingID}')
    system('cls')

#Joining
    
print('Please ignore the warning!\nMay take long time to complete.\n')
for i in range(numberOfBots):
    drivers[i].implicitly_wait(10) #Wait untils tabs loaded
    drivers[i].find_element_by_id('onetrust-accept-btn-handler').click() #Accept Cookies
    try:
        #If disable device not woking this will fix
        drivers[i].find_element_by_id('mic-icon').click()
        sleep(1.25)
        drivers[i].find_element_by_id('video-icon').click()
    except:
        #Bruh
        pass
    #Randomize name if random name is enable
    if customName == None or len(customName) == 0:
        baseName = random.choice(f)
    else:
        baseName = customName
    #Select name and join
    drivers[i].find_element_by_name('inputname').send_keys(baseName)
    drivers[i].find_element_by_id('joinBtn').click()
    drivers[i].implicitly_wait(10)
    drivers[i].find_element_by_name('inputpasscode').send_keys(meetingPasscode)
    drivers[i].find_element_by_id('joinBtn').click()

system('cls')

print('All bot(s) is joined!\nPress Alt+Ctrl+Shift+E to Exit all bots')

#Waiting for user to quit bot(s)

while True:
    if is_pressed('alt') and is_pressed('ctrl') and is_pressed('shift') and is_pressed('e') or is_pressed('E'):
        system('cls')
        for i in range(numberOfBots):
            print(f'Exiting Bot Number {i+1}')
            sleep(0.075)
            drivers[i].close()
        system('pause')
        print('If Auto Exit not working,\nPlease Exit by your self!')
        quit() #Idk why it doesn't exit bye it self :\
