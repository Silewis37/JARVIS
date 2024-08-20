# File Name: voiceBox.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[*] Fix Wakeup Callback Looping and Fucking its self
#[] 


#* Libraries *#

import pyttsx3
import speech_recognition as sr
import time
import random #to allow random replies to questions
import datetime
from playsound import playsound
import os

#* Custom Libraries *#

import plugins.connections.thingiverse as thingiverse
import interfaces.desktop.projectMode as projectMode
import plugins.mongoDB.mongoIN as mongoIN
import plugins.Ollama.mainJarvis as MJ

#^ Variables ^#

keywords = [("jarvis", 0), ("hey jarvis", 1)]
source = sr.Microphone()
engine = pyttsx3.init('nsss') #Initialises the speech engine

#& Functions &#

def clear():
    os.system("clear")
def Speak(text, ver):
    if ver == 0:
        rate = 100 #Sets the default rate of speech
        engine.setProperty('rate', rate+50) #Adjusts the rate of speech
        engine.say(text) #tells Python to speak variable 'text'
        engine.startLoop()
    elif ver == 1:
        rate = 100 #Sets the default rate of speech
        engine.setProperty('rate', rate+25) #Adjusts the rate of speech
        engine.say(text) #tells Python to speak variable 'text'
        engine.startLoop()
def callback(recognizer, audio):
    try:
        speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=keywords) #Uses Sphinx to recognise speech
        #print(speech_as_text) #prints what was said on the screen
        if "jarvis" in speech_as_text or "hey jarvis": #starter names
            Speak("Yes sir?", 1) #Calls 'Speak' and acknowledges user
            time.sleep(2)
            engine.endLoop()
            recognize_main() #Runs the function recognize_main
    except sr.UnknownValueError: #if there is nothing understood
        pass
def start_recognizer(): #initial keyword call
    clear()
    global r
    r = sr.Recognizer()
    playsound('./audio/online.mp3')
    #print("Waiting for a keyword...Jarvis or Hey Jarvis") #Prints to screen
    r.listen_in_background(source, callback) #Sets off recognition sequence
    time.sleep(10000) #keeps loop running
def recognize_main(): #Main reply call function
    speech_rate = engine.getProperty('rate')
    
    #| User Requests
    hello_list = mongoIN.userReq("Hello")
    how_are_you = mongoIN.userReq("Greetings")
    time_list = mongoIN.userReq("Time")
    day_list = mongoIN.userReq("Date")
    printing_list = mongoIN.userReq("ProjectMode.Access")
    dismissed_list = mongoIN.userReq("Dismiss")
    stem_list = mongoIN.userReq("STEM")
    stem_team_list = mongoIN.userReq("STEM.Teams")
    say_hello_list = mongoIN.userReq("SayHello")
    
    #@ Jarvis Responses
    
    reply_hello_list = mongoIN.jarvisResp("Hellos")
    reply_how_are_you = mongoIN.jarvisResp("Greetings")
    reply_stem_list = mongoIN.jarvisResp("STEM")
    reply_stem_team_list = mongoIN.jarvisResp("STEM.Teams")
    reply_say_hello_list = mongoIN.jarvisResp("SayHello")
    
    
    with sr.Microphone() as source: #sets microphone
        playsound('./audio/online.mp3')
        print("Online")
        audio = r.listen(source) #sets variable 'audio'
    data = "" #assigns user voice entry to variable 'data'
    try:
        date = datetime.datetime.now()
        data = r.recognize_google(audio) #now uses Google speech recognition
        data.lower() # makes all voice entries show as lower case
        print("You said: " + data) #shows what user said and what was recognised
        #- Speech Aliases -#
        if "hello" in data:
            hour = date.hour
            weekday = date.strftime("%A")
            day_of_month = date.day
            monthName = date.strftime("%B")
            year = date.year
            current_time = date.strftime("%H:%M")
            if hour>=0 and hour<=12:
                text = f"Good Morning, Sir! Today's Date is {monthName} {day_of_month}, {year}. It is a {weekday}."
                time_taken = len(text.split()) / (speech_rate / 60.0)
                Speak(text, 0)
                time.sleep(time_taken+1)
                engine.endLoop()
            elif hour>=12 and hour<=18:
                text = f"Good Afternoon, Sir! The Time is {current_time}"
                time_taken = len(text.split()) / (speech_rate / 60.0)
                Speak(text, 0)
                time.sleep(time_taken+1)
                engine.endLoop()
            else:
                text = "Good Evening, Sir!"
                time_taken = len(text.split()) / (speech_rate / 60.0)
                Speak(text, 0)
                time.sleep(time_taken+1)
                engine.endLoop()
        
        elif data in how_are_you: #if statement for specific user speech
            text = random.choice(reply_how_are_you) #calls Speak function and says something
            time_taken = len(text.split()) / (speech_rate / 60.0)
            Speak(text, 0)
            time.sleep(time_taken+1)
            engine.endLoop()
        
        elif data in time_list:
            hour = date.hour
            current_time = date.strftime("%H:%M")
            if hour >= 0 and hour <= 12:
                text = f"The Time is {current_time} AM"
                time_taken = len(text.split()) / (speech_rate / 60.0)
                Speak(text, 0)
                time.sleep(time_taken+1)
                engine.endLoop()
            elif hour >= 12 and hour <= 24:
                text = f"The Time is {current_time} PM"
                time_taken = len(text.split()) / (speech_rate / 60.0)
                Speak(text, 0)
                time.sleep(time_taken+1)
                engine.endLoop()
        
        elif data in day_list:
            weekday = date.strftime("%A")
            day_of_month = date.day
            monthName = date.strftime("%B")
            year = date.year
            text = f"Today's Date is {monthName} {day_of_month}, {year}. It is a {weekday}"  
            time_taken = len(text.split()) / (speech_rate / 60.0)
            Speak(text, 0)
            time.sleep(time_taken+1)
            engine.endLoop()
        
        elif data in printing_list:
            projectMode.projectMode_main()
        
        elif data in dismissed_list:
            text = "Have a good evening, Sir!"
            time_taken = len(text.split()) / (speech_rate / 60.0)
            Speak(text, 0)
            time.sleep(time_taken+1)
            engine.endLoop()
            text2 = "Goodbye, Sir!"
            time_taken2 = len(text2.split()) / (speech_rate / 60.0)
            Speak(text2, 0)
            time.sleep(time_taken2+1)
            engine.endLoop()
        
        elif "lock" in data:
            os.system('pmset displaysleepnow.')
        
        elif data in stem_list:
            speech_rate2 = 125
            text = random.choice(reply_stem_list) #calls Speak function and says something
            time_taken = len(text.split()) / (speech_rate2 / 60.0)
            print(text)
            Speak(text, 1)
            time.sleep(time_taken+3)
            engine.endLoop()
        
        elif data in stem_team_list:
            speech_rate2 = 125
            text = random.choice(reply_stem_team_list) #calls Speak function and says something
            time_taken = len(text.split()) / (speech_rate2 / 60.0)
            print(text)
            Speak(text, 1)
            time.sleep(time_taken+3)
            engine.endLoop()

        elif data in say_hello_list: #if statement for specific user speech
            text = random.choice(reply_say_hello_list) #calls Speak function and says something
            time_taken = len(text.split()) / (speech_rate / 60.0)
            Speak(text, 0)
            time.sleep(time_taken+1)
            engine.endLoop()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        else: #what happens if none of the if statements are true
            MJ.send_message(data)
            f = open("./outputText.txt", "r")
            text = f.read()
            time_taken = len(text.split()) / (speech_rate / 60.0)
            print("\n"+text)
            Speak(text, 0)
            time.sleep(time_taken+1)
            engine.endLoop()
            playsound('./audio/online.mp3')
            #start_recognizer()
    except sr.UnknownValueError: #whenever you have a try statement you have an exception rule
        Speak("I'm sorry sir, I did not understand your request", 0) #calls Speak function and says something
        time.sleep(5)
        engine.endLoop()
        print("Jarvis did not understand your request")    
    except sr.RequestError as e: # if you get a request error from Google speech engine
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

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