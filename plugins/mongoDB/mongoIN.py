# File Name: mongoIN.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] TO-DO List Item
#[*] Completed TO-DO List Item

#* Libraries *#

import requests
import pymongo
from pymongo.server_api import ServerApi

#* Custom Libraries *#

#~ import custom made libraries here

#^ Variables ^#

myClient = pymongo.MongoClient("mongodb://localhost:27017/?retryWrites=true&w=majority")

#& Functions &#

def userReq(requestType):
  db = myClient["jarvis"]
  col = db["requests"]
  data = col.find_one({"requestType": requestType})
  dataOUT = []
  for items in data["request"]:
    dataOUT.append(items)
  return dataOUT


def jarvisResp(responseType):
  db = myClient["jarvis"]
  col = db["responses"]
  data = col.find_one({"responseType": responseType})
  dataOUT = []
  for items in data["responses"]:
    dataOUT.append(items)
  return dataOUT


def jarvisSettings(settingType, settingName):
  db = myClient["jarvis"]
  col = db["settings"]
  data = col.find_one({"settingType": settingType})
  dataOUT = data["settings"][settingName]
  return dataOUT

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