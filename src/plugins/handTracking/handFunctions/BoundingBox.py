# File Name: BoundingBox.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] TO-DO List Item
#[*] Completed TO-DO List Item

#* Libraries *#

import sys
import os
import json
import cv2

#* Custom Libraries *#

sys.path.append(os.path.abspath("../../../../"))

#~ import custom made libraries here

#^ Variables ^#

#~ create and store variables here

#& Functions &#

#~ define and build functions here

#= Classes =#

class CalibratingMessage():
    def Start(frame1):
      path = "DeadZone Calibration.Active"
      new_value = True
      with open(" ../../../../../_settings/deadZoneSettings.json", 'r') as f:
          data = json.load(f)

      # Split the path into individual keys
      keys = path.split('.')

      # Update the value at the specified path
      current_object = data
      for key in keys[:-1]:
          if key not in current_object:
              current_object[key] = {}
          current_object = current_object[key]
      current_object[keys[-1]] = new_value

      with open("../../../../../_settings/deadZoneSettings.json", 'w') as f:
          json.dump(data, f, indent=4)
      cv2.putText(frame1, "Calibrating...", (360, 550), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
      
    def Stop():
      path = "DeadZone Calibration.Active"
      new_value = False
      with open("../../../../../_settings/deadZoneSettings.json", 'r') as f:
          data = json.load(f)

      # Split the path into individual keys
      keys = path.split('.')

      # Update the value at the specified path
      current_object = data
      for key in keys[:-1]:
          if key not in current_object:
              current_object[key] = {}
          current_object = current_object[key]
      current_object[keys[-1]] = new_value

      with open("../../../../../_settings/deadZoneSettings.json", 'w') as f:
          json.dump(data, f, indent=4)
  
class DeadZoneChecking():
    def CheckActiveZones():
      with open("../../../../../_settings/deadZoneSettings.json", 'r') as f:
        data = json.load(f)
      TopZone = data["DeadZones"]["Top"]["Active"]
      RightZone = data["DeadZones"]["Right"]["Active"]
      LeftZone = data["DeadZones"]["Left"]["Active"]
      BottomZone = data["DeadZones"]["Bottom"]["Active"]
      return TopZone, RightZone, LeftZone, BottomZone
    def CalibrationCheck():
      with open("../../../../../_settings/deadZoneSettings.json", 'r') as f:
        data = json.load(f)
      calibrating = data["DeadZone Calibration"]["Active"]
      return calibrating
  
class DeadZoneActivation():
    def Activate(Area):
      if Area == "Top":
        path = "DeadZones.Top.Active"
      elif Area == "Right":
        path = "DeadZones.Right.Active"
      elif Area == "Left":
        path = "DeadZones.Left.Active"
      elif Area == "Bottom":
        path = "DeadZones.Bottom.Active"
      new_value = True
      with open("../../../../../_settings/deadZoneSettings.json", 'r') as f:
          data = json.load(f)

      # Split the path into individual keys
      keys = path.split('.')

      # Update the value at the specified path
      current_object = data
      for key in keys[:-1]:
          if key not in current_object:
              current_object[key] = {}
          current_object = current_object[key]
      current_object[keys[-1]] = new_value

      with open("../../../../../_settings/deadZoneSettings.json", 'w') as f:
          json.dump(data, f, indent=4)
    
    def DeActivation(Area):
      if Area == "Top":
        path = "DeadZones.Top.Active"
      elif Area == "Right":
        path = "DeadZones.Right.Active"
      elif Area == "Left":
        path = "DeadZones.Left.Active"
      elif Area == "Bottom":
        path = "DeadZones.Bottom.Active"
      new_value = False
      with open("../../../../../_settings/deadZoneSettings.json", 'r') as f:
          data = json.load(f)

      # Split the path into individual keys
      keys = path.split('.')

      # Update the value at the specified path
      current_object = data
      for key in keys[:-1]:
          if key not in current_object:
              current_object[key] = {}
          current_object = current_object[key]
      current_object[keys[-1]] = new_value

      with open("../../../../../_settings/deadZoneSettings.json", 'w') as f:
          json.dump(data, f, indent=4)
  
class DeadZone():
    def Top(frame1, fWidth):
      with open("../../../../../_settings/deadZoneSettings.json", 'r') as f:
          data = json.load(f)
      width = data["DeadZone Sizing"]["Width"]
      cv2.rectangle(frame1, (0,0), (fWidth,width), (0,0,255), -1)
    def Bottom(frame1, fWidth):
      with open("../../../../../_settings/deadZoneSettings.json", 'r') as f:
          data = json.load(f)
      width = data["DeadZone Sizing"]["Width"]
      cv2.rectangle(frame1, (0,720), (fWidth,720-width),(0,0,255), -1)
    def Left(frame1, fHeight):
      with open("../../../../../_settings/deadZoneSettings.json", 'r') as f:
          data = json.load(f)
      width = data["DeadZone Sizing"]["Width"]
      cv2.rectangle(frame1, (0,0), (width,fHeight), (0,0,255), -1)
    def Right(frame1, fHeight):
      with open("../../../../../_settings/deadZoneSettings.json", 'r') as f:
          data = json.load(f)
      width = data["DeadZone Sizing"]["Width"]
      cv2.rectangle(frame1, (1280,0), (1280-width,fHeight), (0,0,255), -1)
  

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
