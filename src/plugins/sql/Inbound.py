# File Name: Inbound.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] TO-DO List Item
#[*] Completed TO-DO List Item

#* Libraries *#

import mysql.connector as mysql
import json
from dotenv import load_dotenv
import os

#* Custom Libraries *#

#~ import custom made libraries here

#^ Variables ^#

load_dotenv()

sqlHost = os.getenv('MYSQL_HOST')
sqlUser = os.getenv('MYSQL_USER')
sqlPwd = os.getenv('MYSQL_PASSWORD')
sqlDB = os.getenv('MYSQL_DATABASE')
conn = mysql.connect(
  host = sqlHost,
  user = sqlUser,
  password = sqlPwd,
  database= sqlDB
)
cursor = conn.cursor()

#& Functions &#

def userReq(requestType):
  query = f"SELECT REQUEST FROM user_requests WHERE REQUESTTYPE='{requestType}'"
  cursor.execute(query)
  rows = cursor.fetchall()
  for row in rows:
    json_data = row[0]  # Assuming the JSON data is in the first column
    parsed_data = json.loads(str(json_data))  # Parse JSON to a Python dictionary
    requestList = parsed_data.get('request', [])
    return requestList

def jarvisResp(responseType):
  query = f"SELECT RESPONSE FROM jarvis_responses WHERE RESPONSETYPE='{responseType}'"
  cursor.execute(query)
  rows = cursor.fetchall()
  for row in rows:
    json_data = row[0]  # Assuming the JSON data is in the first column
    parsed_data = json.loads(str(json_data))  # Parse JSON to a Python dictionary
    responseList = parsed_data.get('responses', [])
    return responseList

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
