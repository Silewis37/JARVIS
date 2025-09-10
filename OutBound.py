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
  host = "127.0.0.1",
  user = "root",
  password = f"{sqlPwd}",
  database= "jarvis-system",
  port = 3307
)
cursor = conn.cursor()

#& Functions &#



#= Classes =#

#~ define and build classes here

#! Main Program !#
ID = int(input("Enter ID: "))
TOKEN_NAME = str(input("Enter Token Name: "))
TOKEN_VALUE = str(input("Enter Token Value: "))
query = f"INSERT INTO `api_tokens` (`ID`, `TOKEN_NAME`, `TOKEN_VALUE`) VALUES ('{ID}', '{TOKEN_NAME}', '{TOKEN_VALUE}');"
print(query)
#query = f"INSERT INTO `api_tokens` (`ID`, `TOKEN_NAME`, `TOKEN_VALUE`) VALUES ('1', 'Github API', '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');'"
cursor.execute(query)
conn.commit()
cursor.close()
conn.close()


# 


#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#
