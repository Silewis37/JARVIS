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
elif test_selector == 2:
  hTm.main()
elif test_selector == 3:
  hT.main()
elif test_selector == 4:
  weather.main()
elif test_selector == 5:
  mongoIN.main()
elif test_selector == 6:
  mongoOUT.main()
elif test_selector == 7:
  sqlInbound.main()
elif test_selector == 8:
  print("Not yet implemented")
else:
  print("Invalid input, please select a number between 1 and 8")
#* End of Main Program *#



#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#
