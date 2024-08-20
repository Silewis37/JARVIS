# File Name: cliProjectMode.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] Convert all of the main projectMode.py code into code that can be used only in a CLI Prompt
#[] Make sure that all of the commands and procedures that happen in the projectMode.py code are properly interpreted in a CLI Prompt format


#* Libraries *#

import pyttsx3
import time
from playsound import playsound
import os


#* Custom Libraries *#

import plugins.connections.thingiverse as thv
import plugins.mongoDB.mongoIN as mongoIN
import interfaces.desktop.voiceBox as VBox
import speech_recognition as sr

#^ Variables ^#

engine = pyttsx3.init('nsss')

#& Functions &#

def clear():
  os.system("clear")

def Speak(text):
    print(text)

def projectMode_main():
    speech_rate = 150
    playsound('./audio/online.mp3'))
    print("Project Mode Activated\n")
    Speak("Project Mode Activated, Sir!")
    
    #| User Requests
    
    search_list = mongoIN.userReq("ProjectMode.Search")
    toPrinter_list = mongoIN.userReq("ProjectMode.Printer")
    downloadFiles_list = mongoIN.userReq("ProjectMode.Download")
    exitProjectMode_list = mongoIN.userReq("BackToHome")
    printOne_list = mongoIN.userReq("ProjectMode.Download.One")
    printTwo_list = mongoIN.userReq("ProjectMode.Download.Two")
    printThree_list = mongoIN.userReq("ProjectMode.Download.Three")
    data = input("$User > ")
    try:
        print("You Said: " + data)
        #- Speech Aliases -#
        if data in exitProjectMode_list:
            clear()
            Speak("Yes, Sir! Now Exiting Project Mode.")
            time.sleep(4)
            VBox.start_recognizer()
        elif data in search_list:
            clear()
            print("Searching Print > What do you want to lookup!\n") #prints to screen
            Speak("What would you like to look for?")
            playsound('./audio/online.mp3'))
            data1 = input("$User > ") #assigns user voice entry to variable 'data'
            try:
                print("You said: " + data1) #shows what user said and what was recognised
                thv.getPrints(data1)
                printInfo = thv.getPrintInfo()
                PrintName1 = printInfo[0]["Print_Name"]
                PrintName2 = printInfo[1]["Print_Name"]
                PrintName3 = printInfo[2]["Print_Name"]
                PrintAuthor1 = printInfo[0]["Print_Author"]
                PrintAuthor2 = printInfo[1]["Print_Author"]
                PrintAuthor3 = printInfo[2]["Print_Author"]
                NumOfFiles1 = printInfo[0]["Number_Of_Files"]
                NumOfFiles2 = printInfo[1]["Number_Of_Files"]
                NumOfFiles3 = printInfo[2]["Number_Of_Files"]
                text = f"Here are three prints that match your request:This print is called {PrintName1}. It was made by {PrintAuthor1}, and has {NumOfFiles1} stl Model Files. This print is called {PrintName2}. It was made by {PrintAuthor2}, and has {NumOfFiles2} stl Model Files. This print is called {PrintName3}. It was made by {PrintAuthor3}, and has {NumOfFiles3} stl Model Files."
                Speak(text)
            except:
                print("idk")
        elif data in downloadFiles_list:
            print("Searching Print > What do you want to lookup!\n") #prints to screen
            Speak("What would you like to look for?\n")
            playsound('./audio/online.mp3'))
            data1 = input("$User > ") #assigns user voice entry to variable 'data'
            print(data1)
            try:
                print("You said: " + data1) #shows what user said and what was recognised
                thv.getPrints(data1)
                printInfo = thv.getPrintInfo()
                PrintName1 = printInfo[0]["Print_Name"]
                PrintName2 = printInfo[1]["Print_Name"]
                PrintName3 = printInfo[2]["Print_Name"]
                PrintAuthor1 = printInfo[0]["Print_Author"]
                PrintAuthor2 = printInfo[1]["Print_Author"]
                PrintAuthor3 = printInfo[2]["Print_Author"]
                NumOfFiles1 = printInfo[0]["Number_Of_Files"]
                NumOfFiles2 = printInfo[1]["Number_Of_Files"]
                NumOfFiles3 = printInfo[2]["Number_Of_Files"]
                text = f"Here are three prints that match your request:This print is called {PrintName1}. It was made by {PrintAuthor1}, and has {NumOfFiles1} stl Model Files. This print is called {PrintName2}. It was made by {PrintAuthor2}, and has {NumOfFiles2} stl Model Files. This print is called {PrintName3}. It was made by {PrintAuthor3}, and has {NumOfFiles3} stl Model Files."
                Speak(text)
                time.sleep(3)
                print("\nSelect a Print you would Like to download!\n") #prints to screen
                text1 = f"Print 1 is called {PrintName1}, Print 2 is called {PrintName2}, Print 3 is called {PrintName3}. Pick a number 1-3."
                Speak(text1)
                playsound('./audio/online.mp3'))
                data2 = input("$User > ")
                try:
                    clear()
                    print("You said: " + data2)
                    if data2 in printOne_list:
                        thv.downloadFiles(0)
                    elif data2 in printTwo_list:
                        thv.downloadFiles(1)
                    elif data2 in printThree_list:
                        thv.downloadFiles(2)
                    else:
                        pass
                except:
                    pass
            except:
                print("idk")
        
        
    except:
        pass

#= Classes =#

#~ define and build classes here

#! Main Program !#

#~ the main program goes here



#- UNASSIGNED COLOR -#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#
