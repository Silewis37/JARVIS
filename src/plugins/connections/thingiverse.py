# File Name: thingiverse.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[*] Connect to and then run a search on the Thingiverse API
#[*] Successfully pull the top 3 most popular 3D Prints From the Thingiverse API
#[] Find a way to allow the user to cycle through the queried data from the Thingiverse API and view the next 3 Most Popular 3D Prints
#[] Allow the user to select a print and download the STL Files from the Thingiverse API


#* Libraries *#

import requests
import json
import time
import os

#* Custom Libraries *#

import plugins.mongoDB.mongoIN as mongoIN

#^ Variables ^#



#& Functions &#

def getPrints(search):
  api_url = f"https://api.thingiverse.com/search/{search}"
  params = {"type": "thing", "page": "1", "per_page": "3", "sort":"popular"}
  header = {"Content-Type": "application/json", "Authorization": mongoIN.jarvisSettings("ThingiVerse.ConnectionInfo", "API Key")}
  response = requests.get(api_url, params=params, headers=header)


def getPrintInfo():
  inputFile = open("./data/thingiverse/data1.json", "r")
  data = json.load(inputFile)
  header = {"Content-Type": "application/json", "Authorization": mongoIN.jarvisSettings("ThingiVerse.ConnectionInfo", "API Key")}
  
  printInfo = []
  for i in range(len(data["hits"])):
    thing_id = data["hits"][i]["id"]
    printName = data["hits"][i]["name"]
    printAuthor = data["hits"][i]["creator"]["name"]
    stl_api_url = f"https://api.thingiverse.com/things/{thing_id}/files"
    response = requests.get(stl_api_url, headers=header)
    data3 = response.json()
    with open("./data/thingiverse/data2.json", "w") as f:
      data4 = json.dumps(data3, indent=4)
      f.write(data4)
      f.close()
    numOfPrintFiles = len(data3)
    output = {"Print_Name": printName, "Print_Author": printAuthor, "Number_Of_Files": numOfPrintFiles}
    printInfo.append(output)
  return printInfo

def downloadFiles(selected):
  inputFile = open("./data/thingiverse/data1.json", "r")
  data = json.load(inputFile)
  print_name = data["hits"][selected]["name"]
  printName = print_name.replace(" ", "-")
  header = {"Content-Type": "application/json", "Authorization": mongoIN.jarvisSettings("ThingiVerse.ConnectionInfo", "API Key")}
  thing_id = data["hits"][selected]["id"]
  stl_api_url = f"https://api.thingiverse.com/things/{thing_id}/files"
  response = requests.get(stl_api_url, headers=header)
  data1= response.json()
  with open("./data/thingiverse/data2.json", "w") as f:
    data2 = json.dumps(data1, indent=4)
    f.write(data2)
    f.close()
  if os.path.exists(f"./data/thingiverse/stl-Files/{printName}/") == False:
    os.mkdir(f"./data/thingiverse/stl-Files/{printName}/")
    for i in range(len(data1)):
      download_url = data1[i]["download_url"]
      file_name = data1[i]["name"]
      download_response = requests.get(download_url, headers=header)
      with open(f"./data/thingiverse/stl-Files/{printName}/{file_name}", "wb") as file:
        file.write(download_response.content)

#= Classes =#

#~ define and build classes here

#! Main Program !#

#~ the main program goes here



#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#