# File Name: cliVoiceBox.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] Convert all of the main voiceBox.py code into code that can be used only in a CLI Prompt
#[] Make sure that all of the commands and procedures that happen in the voiceBox.py code are properly interpreted in a CLI Prompt format

#* Libraries *#

import pyttsx3
import speech_recognition as sr
import time
import random #to allow random replies to questions
import datetime
from playsound import playsound
import os

#* Custom Libraries *#

import plugins.mongoDB.mongoIN as mongoIN
import plugins.connections.thingiverse as thingiverse
import interfaces.command.cliProjectMode as projectMode
import plugins.Ollama.mainJarvis as MJ

#^ Variables ^#

keywords = [("jarvis", 0), ("hey jarvis", 1)]

#& Functions &#

def Speak(text):
    print(text)

def clear():
    os.system("clear")

def recognize_main(): #Main reply call function
    print("Online")
    data = input("$User > ") #assigns user voice entry to variable 'data'
    
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
    try:
        date = datetime.datetime.now()
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
                Speak(f"Good Morning, Sir! Today's Date is {monthName} {day_of_month}, {year}. It is a {weekday}.")
                time.sleep(3)
                clear()
            elif hour>=12 and hour<=18:
                Speak(f"Good Afternoon, Sir! The Time is {current_time}")
                time.sleep(3)
                clear()
            else:
                Speak("Good Evening, Sir!")
                time.sleep(3)
                clear()
        elif data in how_are_you: #if statement for specific user speech
            Speak (random.choice(reply_how_are_you)) #calls Speak function and says something
        elif data in time_list:
            hour = date.hour
            current_time = date.strftime("%H:%M")
            if hour >= 0 and hour <= 12:
                Speak(f"The Time is {current_time} AM")
                time.sleep(3)
                clear()
            elif hour >= 12 and hour <= 24:
                Speak(f"The Time is {current_time} PM")
                time.sleep(3)
                clear()
        elif data in day_list:
            weekday = date.strftime("%A")
            day_of_month = date.day
            monthName = date.strftime("%B")
            year = date.year
            Speak(f"Today's Date is {monthName} {day_of_month}, {year}. It is a {weekday}") 
            time.sleep(3)
            clear()   
        elif data in printing_list:
            clear()
            projectMode.projectMode_main()
        elif "dismissed" in data:
            Speak("Have a good evening, Sir!")
            time.sleep(4)
            Speak("Goodbye, Sir!")
            time.sleep(3)
            clear()
            exit()
        
        
        
        
        
        
        
        
        
        else: #what happens if none of the if statements are true
            Speak("I'm sorry sir, I did not understand your request") #calls Speak function and says something
            time.sleep(5)
    except sr.UnknownValueError: #whenever you have a try statement you have an exception rule
        Speak("I'm sorry sir, I did not understand your request") #calls Speak function and says something
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