# File Name: outBound.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] TO-DO List Item
#[*] Completed TO-DO List Item

#* Libraries *#

import requests
import pymongo
from pymongo.server_api import ServerApi
import os
from tkinter import messagebox
import json
from tkinter import *
import tkinter as tk

#* Custom Libraries *#

#~ import custom made libraries here

#^ Variables ^#

root = Tk()
myClient = pymongo.MongoClient("mongodb://localhost:27017/?retryWrites=true&w=majority")

#& Functions &#

def show_popup():
    user_input = messagebox.askyesno("Create", "Would you like to assign a Task to this April Tag?")
    return user_input

def assign_AT(AT_id, assignment_type, assignment):
    # Specify the database and collection
    db = myClient['jarvis']
    mycol = db['aprilTags']
    myDict = { "aprilTag_id": AT_id, "aprilTag_assignment_Type": f"{assignment_type}", "aprilTag_assignment": f"{assignment}" }
    x = mycol.insert_one(myDict)
    myClient.close()

def show_creator(AT_id):
    
  root2=tk.Tk()
  root2.title(f"Creation of {AT_id}'s Assignment Task")
  # setting the windows size
  root2.geometry("500x300")
    
  # declaring string variable
  # for storing name and password
  type_var=tk.StringVar()
  assignment_var=tk.StringVar()
  
    
  # defining a function that will
  # get the name and password and 
  # print them on the screen
  def submit():
  
      type=type_var.get()
      assignment=assignment_var.get()
      
      print("Type of April Tag: " + type)
      print("April Tags Assignment : " + assignment)
      
      assign_AT(AT_id, type, assignment)
      root2.destroy()
      type_var.set("")
      assignment_var.set("")
      return type, assignment
      
      
  # creating a label for 
  # name using widget Label
  type_label = tk.Label(root2, text = 'April Tag Type', font=('calibre',10, 'bold'))
    
  # creating a entry for input
  # name using widget Entry
  type_entry = tk.Entry(root2,textvariable = type_var, font=('calibre',10,'normal'))
    
  # creating a label for password
  assignment_label = tk.Label(root2, text = 'April Tags Assignment', font = ('calibre',10,'bold'))
    
  # creating a entry for password
  assignment_entry =tk.Entry(root2, textvariable = assignment_var, font = ('calibre',10,'normal'))
    
  # creating a button using the widget 
  # Button that will call the submit function 
  sub_btn=tk.Button(root2,text = 'Submit', command = submit)
    
  # placing the label and entry in
  # the required position using grid
  # method
  type_label.grid(row=0,column=0)
  type_entry.grid(row=0,column=1)
  assignment_label.grid(row=1,column=0)
  assignment_entry.grid(row=1,column=1)
  sub_btn.grid(row=2,column=1)
    
  # performing an infinite loop 
  # for the window to display
  root2.mainloop()

def AT_assignment(AT_id):
  db = myClient['jarvis']
  mycol = db['aprilTags']
  data = mycol.find_one({"aprilTag_id": AT_id})
  if data == None:
    print("THIS AprilTag does not Have an Assignment")
    create_new = show_popup()
    if create_new == False:
      pass
    if create_new == True:
      show_creator(AT_id=AT_id)
    else:
      pass
  if data != None:
    tagType = data["aprilTag_assignment_Type"]
    assignment = data["aprilTag_assignment"]
    print(f"Tag Id: {AT_id}")
    print(f"Tag Type: {tagType}")
    print(f"Tag Assignment: {assignment}")

def AT_unassign(AT_id):
  db = myClient['jarvis']
  mycol = db['aprilTags']
  data = mycol.find_one({"aprilTag_id": AT_id})
  mycol.delete_one(data)

def addPassword(websiteURL, username, password):
  db = myClient['jarvis']
  col = db["passwords"]
  root2=tk.Tk()
  root2.title(f"Adding password to Password Database")
  # setting the windows size
  root2.geometry("1000x300")
    
  # declaring string variable
  # for storing name and password
  type_var=tk.StringVar()
  assignment_var=tk.StringVar()
  
    
  # defining a function that will
  # get the name and password and 
  # print them on the screen
  def submit():
  
      type=type_var.get()
      assignment=assignment_var.get()
      
      print("Password Type: " + type)
      print("Password Name : " + assignment)
      
      myDict = { "passwordType": type, "passwordName": f"{assignment}", "websiteURL": f"{websiteURL}", "username": f"{username}", "password": f"{password}" }
      x = col.insert_one(myDict)
      root2.destroy()
      type_var.set("")
      assignment_var.set("")
      return type, assignment
  
  def skipBTN():
    print("skipped")
    root2.destroy()
    return None
  
  # creating a label for 
  # name using widget Label
  passwordURL = tk.Label(root2, text = f"URL: {websiteURL}", font=('calibre',10, 'bold'))
  passwordUN = tk.Label(root2, text = f"Username: {username}", font=('calibre',11, 'bold'))
  passwordPS = tk.Label(root2, text = f"Password: {password}", font=('calibre',11, 'bold'))
  
  type_label = tk.Label(root2, text = 'Password Type', font=('calibre',10, 'bold'))
    
  # creating a entry for input
  # name using widget Entry
  type_entry = tk.Entry(root2, textvariable = type_var, font=('calibre',10,'normal'))
    
  # creating a label for password
  assignment_label = tk.Label(root2, text = 'Password Name', font = ('calibre',10,'bold'))
    
  # creating a entry for password
  assignment_entry =tk.Entry(root2, textvariable = assignment_var, font = ('calibre',10,'normal'))
    
  # creating a button using the widget 
  # Button that will call the submit function 
  sub_btn=tk.Button(root2, text = 'Submit', command = submit)
  skip_btn = tk.Button(root2, text = 'Skip', command = skipBTN)
    
  # placing the label and entry in
  # the required position using grid
  # method
  passwordURL.grid(row=0, column=0)
  passwordUN.grid(row=1, column=0)
  passwordPS.grid(row=2, column=0)
  
  type_label.grid(row=4,column=0)
  type_entry.grid(row=4,column=1)
  assignment_label.grid(row=5,column=0)
  assignment_entry.grid(row=5,column=1)
  sub_btn.grid(row=7,column=1)
  skip_btn.grid(row=7, column=3)
    
  # performing an infinite loop 
  # for the window to display
  root2.mainloop()

#= Classes =#

#~ define and build classes here

#! Main Program !#

root.mainloop()



#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#