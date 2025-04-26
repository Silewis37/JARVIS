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

# import plugins.aprilTags.aprilTagDecoder as at
# import plugins.handTracking.handToMouse as hTm
# import plugins.handTracking.handTracker as hT
# import plugins.connections.weather as weather
# import plugins.mongoDB.mongoIN as mongoIN
# import plugins.mongoDB.outBound as mongoOUT
# import plugins.sql.Inbound as sqlInbound

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
print("8. Hand to Mouse 2")
test_selector = int(input("Select which Test:"))

if test_selector == 1:
  import plugins.aprilTags.aprilTagDecoder as at
  at.main()
elif test_selector == 2:
  import plugins.handTracking.handToMouse as hTm
  hTm.mouse()
elif test_selector == 3:
  import plugins.handTracking.handTracker as hT
  hT.main()
elif test_selector == 4:
  import plugins.connections.weather as weather
  weather.main()
elif test_selector == 5:
  import plugins.mongoDB.mongoIN as mongoIN
  mongoIN.main()
elif test_selector == 6:
  import plugins.mongoDB.outBound as mongoOUT
  mongoOUT.main()
elif test_selector == 7:
  import plugins.sql.Inbound as sqlInbound
  sqlInbound.main()
elif test_selector == 8:
  import plugins.handTracking.handToMouse as hTm
  hTm.mouse2()
else:
  print("Invalid input, please select a number between 1 and 8\n Selected Number Was: " + str(test_selector))
#* End of Main Program *#



#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#
