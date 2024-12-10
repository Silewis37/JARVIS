# File Name: 
# Author: Samuel Lewis

#$ TO-DO List $#
#[] TO-DO List Item
#[*] Completed TO-DO List Item

#* Libraries *#

import sys
import os
#~ import pip installed libraries here

#* Custom Libraries *#

sys.path.append(os.path.abspath("src/"))

import plugins.aprilTags.aprilTagDecoder as at
import plugins.handTracking.handToMouse as hTm
import plugins.handTracking.handTracker as hT
import plugins.connections.weather as weather
import plugins.mongoDB.mongoIN as mongoIN
import plugins.mongoDB.outBound as mongoOUT
import plugins.sql.Inbound as sqlInbound

#^ Variables ^#

#~ create and store variables here

#& Functions &#

#~ define and build functions here

#= Classes =#

#~ define and build classes here

#! Main Program !#


print("1. April Tags")
print("2. Hand To Mouse")
print("3. Hand Tracker")
print("4. Weather")
print("5. MongoIN")
print("6. MongoOUT")
print("7. sqlInbound")
print("8. Not yet implemented")
test_selector = input("Select which Test:")

if test_selector == 1:
  at.main()



#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#
