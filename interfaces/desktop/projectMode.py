# File Name: projectMode.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[*] Finish the Speech Recognition
#[] Finish the Print Selection Methods
#[] Make a way to re-do the Search or go to the next three prints
#[] Make a way to send prints to a 3D Printer
#[] Make a way to checkup on and/or monitor a 3D Printer

#* Libraries *#

import pyttsx3
import time
from playsound import playsound

#* Custom Libraries *#

import plugins.connections.thingiverse as thv
import interfaces.desktop.voiceBox as VBox
import speech_recognition as sr
import plugins.mongoDB.mongoIN as mongoIN

#^ Variables ^#

engine = pyttsx3.init('nsss')
source = sr.Microphone()
r = sr.Recognizer()

#& Functions &#

def Speak(text):
    rate = 100 #Sets the default rate of speech
    engine.setProperty('rate', rate+50) #Adjusts the rate of speech
    engine.say(text) #tells Python to speak variable 'text'
    engine.startLoop()

def projectMode_main():
    
    #| User Requests
    
    search_list = mongoIN.userReq("ProjectMode.Search")
    toPrinter_list = mongoIN.userReq("ProjectMode.Printer")
    downloadFiles_list = mongoIN.userReq("ProjectMode.Download")
    exitProjectMode_list = mongoIN.userReq("BackToHome")
    printOne_list = mongoIN.userReq("ProjectMode.Download.One")
    printTwo_list = mongoIN.userReq("ProjectMode.Download.Two")
    printThree_list = mongoIN.userReq("ProjectMode.Download.Three")
    
    speech_rate = engine.getProperty('rate')
    with sr.Microphone() as source:
        playsound('./audio/online.mp3')
        print("Project Mode Activated")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        data.lower()
        print("You Said: " + data)
        #- Speech Aliases -#
        if data in exitProjectMode_list:
            Speak("Yes, Sir! Now Exiting Project Mode.")
            time.sleep(4)
            engine.stopLoop()
            VBox.start_recognizer()
        elif data in search_list:
            with sr.Microphone() as source: #sets microphone
                print("Searching Print > What do you want to lookup!") #prints to screen
                Speak("What would you like to look for?")
                time.sleep(3)
                engine.endLoop()
                playsound('./audio/online.mp3')
                audio1 = r.listen(source) #sets variable 'audio'
            data1 = "" #assigns user voice entry to variable 'data'
            print(data1)
            try:
                data1 = r.recognize_google(audio1) #now uses Google speech recognition
                data1.lower()
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
                time_taken = len(text.split()) / (speech_rate / 60.0)
                Speak(text)
                time.sleep(time_taken)
                engine.endLoop()
            except:
                print("idk")
        elif data in downloadFiles_list:
            with sr.Microphone() as source: #sets microphone
                print("Searching Print > What do you want to lookup!") #prints to screen
                Speak("What would you like to look for?")
                time.sleep(3)
                engine.endLoop()
                playsound('./audio/online.mp3')
                audio1 = r.listen(source) #sets variable 'audio'
            data1 = "" #assigns user voice entry to variable 'data'
            print(data1)
            try:
                data1 = r.recognize_google(audio1) #now uses Google speech recognition
                data1.lower()
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
                time_taken = len(text.split()) / (speech_rate / 60.0)
                Speak(text)
                time.sleep(time_taken)
                engine.endLoop()
                with sr.Microphone() as source: #sets microphone
                    print("Select a Print you would Like to download!") #prints to screen
                    text1 = f"Print 1 is called {PrintName1}, Print 2 is called {PrintName2}, Print 3 is called {PrintName3}. Pick a number 1-3."
                    time_taken1 = len(text1.split()) / (speech_rate / 60.0)
                    Speak(text1)
                    time.sleep(time_taken1)
                    engine.endLoop()
                    playsound('./audio/online.mp3')
                    audio2 = r.listen(source) #sets variable 'audio'
                data2 = "" #assigns user voice entry to variable 'data'
                print(data2)
                try:
                    data2 = r.recognize_google(audio2)
                    data2.lower()
                    print("You said: " + data2)
                    if data in printOne_list:
                        thv.downloadFiles(0)
                    elif data in printTwo_list:
                        thv.downloadFiles(1)
                    elif data in printThree_list:
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