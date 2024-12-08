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
  
)

#& Functions &#

#~ define and build functions here

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
