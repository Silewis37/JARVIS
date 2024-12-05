# File Name: RequestHandler.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] TO-DO List Item

#* Libraries *#

import requests
import os
import json

#* Custom Libraries *#

#~ import custom made libraries here

#^ Variables ^#

#~ create and store variables here

#& Functions &#

#~ define and build functions here

#= Classes =#

class RequestPuller():
  def GET(url, filePath):
    response = requests.get(url)
    with open(filePath, "w+") as f:
      json.dump(response.json(), f, indent=4)

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