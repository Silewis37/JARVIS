# File Name: handFunctions.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] TO-DO List Item

#* Libraries *#

import cv2
import mediapipe as mp
import mediapipe.python.solutions.face_mesh as mpD
import numpy as np
import os
import json
import time

#* Custom Libraries *#

#~ import custom made libraries here

#^ Variables ^#

#~ create and store variables here

#& Functions &#

#~ define and build functions here

#= Classes =#

class BoundingBox():
  
  class CalibratingMessage():
    def Start(frame1):
      path = "DeadZone Calibration.Active"
      new_value = True
      with open("_settings/deadZoneSettings.json", 'r') as f:
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

      with open("_settings/deadZoneSettings.json", 'w') as f:
          json.dump(data, f, indent=4)
      cv2.putText(frame1, "Calibrating...", (360, 550), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
      
    def Stop():
      path = "DeadZone Calibration.Active"
      new_value = False
      with open("_settings/deadZoneSettings.json", 'r') as f:
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

      with open("_settings/deadZoneSettings.json", 'w') as f:
          json.dump(data, f, indent=4)
  
  class DeadZoneChecking():
    def CheckActiveZones():
      with open("_settings/deadZoneSettings.json", 'r') as f:
        data = json.load(f)
      TopZone = data["DeadZones"]["Top"]["Active"]
      RightZone = data["DeadZones"]["Right"]["Active"]
      LeftZone = data["DeadZones"]["Left"]["Active"]
      BottomZone = data["DeadZones"]["Bottom"]["Active"]
      return TopZone, RightZone, LeftZone, BottomZone
    def CalibrationCheck():
      with open("_settings/deadZoneSettings.json", 'r') as f:
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
      with open("_settings/deadZoneSettings.json", 'r') as f:
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

      with open("_settings/deadZoneSettings.json", 'w') as f:
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
      with open("_settings/deadZoneSettings.json", 'r') as f:
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

      with open("_settings/deadZoneSettings.json", 'w') as f:
          json.dump(data, f, indent=4)
  
  
  
  class DeadZone():
    def Top(frame1, fWidth):
      with open("_settings/deadZoneSettings.json", 'r') as f:
          data = json.load(f)
      width = data["DeadZone Sizing"]["Width"]
      cv2.rectangle(frame1, (0,0), (fWidth,width), (0,0,255), -1)
    def Bottom(frame1, fWidth):
      with open("_settings/deadZoneSettings.json", 'r') as f:
          data = json.load(f)
      width = data["DeadZone Sizing"]["Width"]
      cv2.rectangle(frame1, (0,720), (fWidth,720-width),(0,0,255), -1)
    def Left(frame1, fHeight):
      with open("_settings/deadZoneSettings.json", 'r') as f:
          data = json.load(f)
      width = data["DeadZone Sizing"]["Width"]
      cv2.rectangle(frame1, (0,0), (width,fHeight), (0,0,255), -1)
    def Right(frame1, fHeight):
      with open("_settings/deadZoneSettings.json", 'r') as f:
          data = json.load(f)
      width = data["DeadZone Sizing"]["Width"]
      cv2.rectangle(frame1, (1280,0), (1280-width,fHeight), (0,0,255), -1)


class LeftHand():
  class CheckingLayers():
    def CheckActiveLayer():
      with open("_settings/handLayer.json", 'r') as f:
        data = json.load(f)
      layer1 = data["Left Hand"]["Layer 1"]
      layer2 = data["Left Hand"]["Layer 2"]
      layer3 = data["Left Hand"]["Layer 3"]
      LayerChanger = data["Left Hand"]["Changer"]
      
      if layer1 == True:
        layer = 1
        return layer
      if layer2 == True:
        layer = 2
        return layer
      if layer3 == True:
        layer = 3
        return layer
      if LayerChanger == True:
        layer = 0
        return layer
  
  class ChangingLayers():
    class PinkyChangingMenu():
      def color(frame1, thumb_coord_real1, index_finger_coord_real1, middle_finger_real1, ring_finger_real1, pinky_finger_real1, midpoint_index1, midpoint_ring1, midpoint_middle1, midpoint_pinky1):
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_index1[0], midpoint_index1[1]), (102, 255, 102), 2)
                    cv2.line(frame1, (index_finger_coord_real1[0], index_finger_coord_real1[1]), (midpoint_index1[0], midpoint_index1[1]), (102, 255, 102), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_middle1[0], midpoint_middle1[1]), (255, 102, 255), 2)
                    cv2.line(frame1, (middle_finger_real1[0], middle_finger_real1[1]), (midpoint_middle1[0], midpoint_middle1[1]), (255, 102, 255), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_ring1[0], midpoint_ring1[1]), (51, 102, 255), 2)
                    cv2.line(frame1, (ring_finger_real1[0], ring_finger_real1[1]), (midpoint_ring1[0], midpoint_ring1[1]), (51, 102, 255), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_pinky1[0], midpoint_pinky1[1]), (255, 102, 102), 2)
                    cv2.line(frame1, (pinky_finger_real1[0], pinky_finger_real1[1]), (midpoint_pinky1[0], midpoint_pinky1[1]), (255, 102, 102), 2)
      def ChangetoLayer1():
        LeftHand.ChangingLayers.ChangeHandLayer(1, "Changer")
        LeftHand.ChangingLayers.ChangeHandLayer(1, 2)
        LeftHand.ChangingLayers.ChangeHandLayer(1, 3)
      def ChangetoLayer2():
        LeftHand.ChangingLayers.ChangeHandLayer(2, "Changer")
        LeftHand.ChangingLayers.ChangeHandLayer(2, 1)
        LeftHand.ChangingLayers.ChangeHandLayer(2, 3)
      def ChangetoLayer3():
        LeftHand.ChangingLayers.ChangeHandLayer(3, "Changer")
        LeftHand.ChangingLayers.ChangeHandLayer(3, 2)
        LeftHand.ChangingLayers.ChangeHandLayer(3, 1)
    def ChangeHandLayer(layer, lastLayer):
      if layer == 1:
        path = "Left Hand.Layer 1"
      elif layer == 2:
        path = "Left Hand.Layer 2"
      elif layer == 3:
        path = "Left Hand.Layer 3"
      elif layer == "Changer":
        path = "Left Hand.Changer"
      
      if lastLayer == 1:
        pathL = "Left Hand.Layer 1"
      elif lastLayer == 2:
        pathL = "Left Hand.Layer 2"
      elif lastLayer == 3:
        pathL = "Left Hand.Layer 3"
      elif lastLayer == "Changer":
        pathL = "Left Hand.Changer"
      new_value = True
      new_valueL = False
      with open("_settings/handLayer.json", 'r') as f:
          data = json.load(f)

      # Split the path into individual keys
      keys = path.split('.')
      keysL = pathL.split('.')

      # Update the value at the specified path
      current_object = data
      for key in keys[:-1]:
          if key not in current_object:
              current_object[key] = {}
          current_object = current_object[key]
      current_object[keys[-1]] = new_value
      current_object[keysL[-1]] = new_valueL

      with open("_settings/handLayer.json", 'w') as f:
          json.dump(data, f, indent=4)
  
  class Layer1():
    def color(frame1, thumb_coord_real1, index_finger_coord_real1, middle_finger_real1, ring_finger_real1, pinky_finger_real1, midpoint_index1, midpoint_ring1, midpoint_middle1, midpoint_pinky1):
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_index1[0], midpoint_index1[1]), (0, 255, 255), 2)
                    cv2.line(frame1, (index_finger_coord_real1[0], index_finger_coord_real1[1]), (midpoint_index1[0], midpoint_index1[1]), (0, 255, 255), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_middle1[0], midpoint_middle1[1]), (204, 0, 153), 2)
                    cv2.line(frame1, (middle_finger_real1[0], middle_finger_real1[1]), (midpoint_middle1[0], midpoint_middle1[1]), (204, 0, 153), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_ring1[0], midpoint_ring1[1]), (51, 51, 255), 2)
                    cv2.line(frame1, (ring_finger_real1[0], ring_finger_real1[1]), (midpoint_ring1[0], midpoint_ring1[1]), (51, 51, 255), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_pinky1[0], midpoint_pinky1[1]), (0, 153, 51), 2)
                    cv2.line(frame1, (pinky_finger_real1[0], pinky_finger_real1[1]), (midpoint_pinky1[0], midpoint_pinky1[1]), (0, 153, 51), 2)
                    
    def swapToDesktop1():
      print("Swapping to Desktop 1")
    def swapToDesktop2():
      print("Swapping to Desktop 2")
    def swapToDesktop3():
      print("Swapping to Desktop 3")
    def layerChanger(frame1):
      LeftHand.ChangingLayers.ChangeHandLayer("Changer", 1)
      LeftHand.ChangingLayers.PinkyChangingMenu.color(frame1)
  
  class Layer2():
    def color(frame1, thumb_coord_real1, index_finger_coord_real1, middle_finger_real1, ring_finger_real1, pinky_finger_real1, midpoint_index1, midpoint_ring1, midpoint_middle1, midpoint_pinky1):
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_index1[0], midpoint_index1[1]), (0, 255, 255), 2)
                    cv2.line(frame1, (index_finger_coord_real1[0], index_finger_coord_real1[1]), (midpoint_index1[0], midpoint_index1[1]), (0, 255, 255), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_middle1[0], midpoint_middle1[1]), (204, 0, 153), 2)
                    cv2.line(frame1, (middle_finger_real1[0], middle_finger_real1[1]), (midpoint_middle1[0], midpoint_middle1[1]), (204, 0, 153), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_ring1[0], midpoint_ring1[1]), (51, 51, 255), 2)
                    cv2.line(frame1, (ring_finger_real1[0], ring_finger_real1[1]), (midpoint_ring1[0], midpoint_ring1[1]), (51, 51, 255), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_pinky1[0], midpoint_pinky1[1]), (0, 153, 51), 2)
                    cv2.line(frame1, (pinky_finger_real1[0], pinky_finger_real1[1]), (midpoint_pinky1[0], midpoint_pinky1[1]), (0, 153, 51), 2)
    def toggleTop():
      print("Toggle Top")
    def toggleRight():
      print("Toggle Right")
    def toggleLeft():
      print("Toggle Left")
    def toggleBottom():
      print("Toggle Bottom")

  #! FIXME this code class is not completed correctly
  class Layer3():
    def color(frame1, thumb_coord_real1, index_finger_coord_real1, middle_finger_real1, ring_finger_real1, pinky_finger_real1, midpoint_index1, midpoint_ring1, midpoint_middle1, midpoint_pinky1):
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_index1[0], midpoint_index1[1]), (130, 224, 170), 2)
                    cv2.line(frame1, (index_finger_coord_real1[0], index_finger_coord_real1[1]), (midpoint_index1[0], midpoint_index1[1]), (130, 224, 170), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_middle1[0], midpoint_middle1[1]), (187, 143, 206), 2)
                    cv2.line(frame1, (middle_finger_real1[0], middle_finger_real1[1]), (midpoint_middle1[0], midpoint_middle1[1]), (187, 143, 206), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_ring1[0], midpoint_ring1[1]), (174, 214, 241), 2)
                    cv2.line(frame1, (ring_finger_real1[0], ring_finger_real1[1]), (midpoint_ring1[0], midpoint_ring1[1]), (174, 214, 241), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_pinky1[0], midpoint_pinky1[1]), (245, 183, 177), 2)
                    cv2.line(frame1, (pinky_finger_real1[0], pinky_finger_real1[1]), (midpoint_pinky1[0], midpoint_pinky1[1]), (245, 183, 177), 2)
    def toggleTop():
      print("Toggle Top")
    def toggleRight():
      print("Toggle Right")
    def toggleLeft():
      print("Toggle Left")
    def toggleBottom():
      print("Toggle Bottom")

  class Fingers():
    def Index(layer):
      if layer == 0:
        LeftHand.ChangingLayers.PinkyChangingMenu.ChangetoLayer1()
      if layer == 1:
        LeftHand.Layer1.swapToDesktop1()
      if layer == 2:
        LeftHand.Layer2.toggleTop()
      if layer == 3:
        LeftHand.Layer3.toggleTop()
    def Middle(layer):
      if layer == 0:
        LeftHand.ChangingLayers.PinkyChangingMenu.ChangetoLayer2()
      if layer == 1:
        LeftHand.Layer1.swapToDesktop2()
      if layer == 2:
        LeftHand.Layer2.toggleRight()
      if layer == 3:
        LeftHand.Layer3.toggleRight()
    def Ring(layer):
      if layer == 0:
        LeftHand.ChangingLayers.PinkyChangingMenu.ChangetoLayer3()
      if layer == 1:
        LeftHand.Layer1.swapToDesktop3()
      if layer == 2:
        LeftHand.Layer2.toggleLeft()
      if layer == 3:
        LeftHand.Layer3.toggleLeft()
    def Pinky(layer):
      if layer == 0:
        print("fuck you0")
      if layer == 1:
        print("fuck you1")
        LeftHand.ChangingLayers.ChangeHandLayer("Changer",1)
      if layer == 2:
        print("fuck you2")
        LeftHand.ChangingLayers.ChangeHandLayer("Changer",2)
      if layer == 3:
        print("fuck you3")
        LeftHand.ChangingLayers.ChangeHandLayer("Changer",3)


class RightHand():
  class CheckingLayers():
    def CheckActiveLayer():
      with open("_settings/handLayer.json", 'r') as f:
        data = json.load(f)
      layer1 = data["Right Hand"]["Layer 1"]
      layer2 = data["Right Hand"]["Layer 2"]
      layer3 = data["Right Hand"]["Layer 3"]
      LayerChanger = data["Right Hand"]["Changer"]
      
      if layer1 == True:
        layer = 1
        return layer
      if layer2 == True:
        layer = 2
        return layer
      if layer3 == True:
        layer = 3
        return layer
      if LayerChanger == True:
        layer = 0
        return layer
  
  class ChangingLayers():
    class PinkyChangingMenu():
      def color(frame1, thumb_coord_real1, index_finger_coord_real1, middle_finger_real1, ring_finger_real1, pinky_finger_real1, midpoint_index1, midpoint_ring1, midpoint_middle1, midpoint_pinky1):
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_index1[0], midpoint_index1[1]), (102, 255, 102), 2)
                    cv2.line(frame1, (index_finger_coord_real1[0], index_finger_coord_real1[1]), (midpoint_index1[0], midpoint_index1[1]), (102, 255, 102), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_middle1[0], midpoint_middle1[1]), (255, 102, 255), 2)
                    cv2.line(frame1, (middle_finger_real1[0], middle_finger_real1[1]), (midpoint_middle1[0], midpoint_middle1[1]), (255, 102, 255), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_ring1[0], midpoint_ring1[1]), (51, 102, 255), 2)
                    cv2.line(frame1, (ring_finger_real1[0], ring_finger_real1[1]), (midpoint_ring1[0], midpoint_ring1[1]), (51, 102, 255), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_pinky1[0], midpoint_pinky1[1]), (255, 102, 102), 2)
                    cv2.line(frame1, (pinky_finger_real1[0], pinky_finger_real1[1]), (midpoint_pinky1[0], midpoint_pinky1[1]), (255, 102, 102), 2)
      def ChangetoLayer1():
        RightHand.ChangingLayers.ChangeHandLayer(1, "Changer")
        RightHand.ChangingLayers.ChangeHandLayer(1, 2)
        RightHand.ChangingLayers.ChangeHandLayer(1, 3)
      def ChangetoLayer2():
        RightHand.ChangingLayers.ChangeHandLayer(2, "Changer")
        RightHand.ChangingLayers.ChangeHandLayer(2, 1)
        RightHand.ChangingLayers.ChangeHandLayer(2, 3)
      def ChangetoLayer3():
        RightHand.ChangingLayers.ChangeHandLayer(3, "Changer")
        RightHand.ChangingLayers.ChangeHandLayer(3, 2)
        RightHand.ChangingLayers.ChangeHandLayer(3, 1)
    def ChangeHandLayer(layer, lastLayer):
      if layer == 1:
        path = "Right Hand.Layer 1"
      elif layer == 2:
        path = "Right Hand.Layer 2"
      elif layer == 3:
        path = "Right Hand.Layer 3"
      elif layer == "Changer":
        path = "Right Hand.Changer"
      
      if lastLayer == 1:
        pathL = "Right Hand.Layer 1"
      elif lastLayer == 2:
        pathL = "Right Hand.Layer 2"
      elif lastLayer == 3:
        pathL = "Right Hand.Layer 3"
      elif lastLayer == "Changer":
        pathL = "Right Hand.Changer"
      new_value = True
      new_valueL = False
      with open("_settings/handLayer.json", 'r') as f:
          data = json.load(f)

      # Split the path into individual keys
      keys = path.split('.')
      keysL = pathL.split('.')

      # Update the value at the specified path
      current_object = data
      for key in keys[:-1]:
          if key not in current_object:
              current_object[key] = {}
          current_object = current_object[key]
      current_object[keys[-1]] = new_value
      current_object[keysL[-1]] = new_valueL

      with open("_settings/handLayer.json", 'w') as f:
          json.dump(data, f, indent=4)
  
  class Layer1():
    def color(frame1, thumb_coord_real1, index_finger_coord_real1, middle_finger_real1, ring_finger_real1, pinky_finger_real1, midpoint_index1, midpoint_ring1, midpoint_middle1, midpoint_pinky1):
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_index1[0], midpoint_index1[1]), (102, 255, 102), 2)
                    cv2.line(frame1, (index_finger_coord_real1[0], index_finger_coord_real1[1]), (midpoint_index1[0], midpoint_index1[1]), (102, 255, 102), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_middle1[0], midpoint_middle1[1]), (255, 102, 255), 2)
                    cv2.line(frame1, (middle_finger_real1[0], middle_finger_real1[1]), (midpoint_middle1[0], midpoint_middle1[1]), (255, 102, 255), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_ring1[0], midpoint_ring1[1]), (51, 102, 255), 2)
                    cv2.line(frame1, (ring_finger_real1[0], ring_finger_real1[1]), (midpoint_ring1[0], midpoint_ring1[1]), (51, 102, 255), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_pinky1[0], midpoint_pinky1[1]), (255, 102, 102), 2)
                    cv2.line(frame1, (pinky_finger_real1[0], pinky_finger_real1[1]), (midpoint_pinky1[0], midpoint_pinky1[1]), (255, 102, 102), 2)
    def leftClick():
      print("Left Click")
    def doubleLeftClick():
      print("Double Left Click")
    def middleClick():
      print("Middle Click")
    def rightClick():
      print("Right Click")
    def layerChanger(frame1):
      RightHand.ChangingLayers.ChangeHandLayer("Changer", 1)
      RightHand.ChangingLayers.PinkyChangingMenu.color(frame1)
  
  class Layer2():
    def color(frame1, thumb_coord_real1, index_finger_coord_real1, middle_finger_real1, ring_finger_real1, pinky_finger_real1, midpoint_index1, midpoint_ring1, midpoint_middle1, midpoint_pinky1):
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_index1[0], midpoint_index1[1]), (130, 224, 170), 2)
                    cv2.line(frame1, (index_finger_coord_real1[0], index_finger_coord_real1[1]), (midpoint_index1[0], midpoint_index1[1]), (130, 224, 170), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_middle1[0], midpoint_middle1[1]), (187, 143, 206), 2)
                    cv2.line(frame1, (middle_finger_real1[0], middle_finger_real1[1]), (midpoint_middle1[0], midpoint_middle1[1]), (187, 143, 206), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_ring1[0], midpoint_ring1[1]), (174, 214, 241), 2)
                    cv2.line(frame1, (ring_finger_real1[0], ring_finger_real1[1]), (midpoint_ring1[0], midpoint_ring1[1]), (174, 214, 241), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_pinky1[0], midpoint_pinky1[1]), (245, 183, 177), 2)
                    cv2.line(frame1, (pinky_finger_real1[0], pinky_finger_real1[1]), (midpoint_pinky1[0], midpoint_pinky1[1]), (245, 183, 177), 2)
    def toggleTop():
      TopZone = BoundingBox.DeadZoneChecking.CheckActiveZones()
      if TopZone[0] == True:
        BoundingBox.DeadZoneActivation.DeActivation("Top")
      elif TopZone[0] == False:
        BoundingBox.DeadZoneActivation.Activate("Top")
    def toggleRight():
      RightZone = BoundingBox.DeadZoneChecking.CheckActiveZones()
      if RightZone[1] == True:
        BoundingBox.DeadZoneActivation.DeActivation("Right")
      elif RightZone[1] == False:
        BoundingBox.DeadZoneActivation.Activate("Right")
    def toggleLeft():
      LeftZone = BoundingBox.DeadZoneChecking.CheckActiveZones()
      if LeftZone[2] == True:
        BoundingBox.DeadZoneActivation.DeActivation("Left")
      elif LeftZone[2] == False:
        BoundingBox.DeadZoneActivation.Activate("Left")
    def toggleBottom():
      BottomZone = BoundingBox.DeadZoneChecking.CheckActiveZones()
      if BottomZone[3] == True:
        BoundingBox.DeadZoneActivation.DeActivation("Bottom")
      elif BottomZone[3] == False:
        BoundingBox.DeadZoneActivation.Activate("Bottom")

  #! FIXME this code class is not completed correctly
  class Layer3():
    def color(frame1, thumb_coord_real1, index_finger_coord_real1, middle_finger_real1, ring_finger_real1, pinky_finger_real1, midpoint_index1, midpoint_ring1, midpoint_middle1, midpoint_pinky1):
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_index1[0], midpoint_index1[1]), (130, 224, 170), 2)
                    cv2.line(frame1, (index_finger_coord_real1[0], index_finger_coord_real1[1]), (midpoint_index1[0], midpoint_index1[1]), (130, 224, 170), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_middle1[0], midpoint_middle1[1]), (187, 143, 206), 2)
                    cv2.line(frame1, (middle_finger_real1[0], middle_finger_real1[1]), (midpoint_middle1[0], midpoint_middle1[1]), (187, 143, 206), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_ring1[0], midpoint_ring1[1]), (174, 214, 241), 2)
                    cv2.line(frame1, (ring_finger_real1[0], ring_finger_real1[1]), (midpoint_ring1[0], midpoint_ring1[1]), (174, 214, 241), 2)
                    
                    cv2.line(frame1, (thumb_coord_real1[0], thumb_coord_real1[1]), (midpoint_pinky1[0], midpoint_pinky1[1]), (245, 183, 177), 2)
                    cv2.line(frame1, (pinky_finger_real1[0], pinky_finger_real1[1]), (midpoint_pinky1[0], midpoint_pinky1[1]), (245, 183, 177), 2)
    def toggleTop():
      print("Toggle Top")
    def toggleRight():
      print("Toggle Right")
    def toggleLeft():
      print("Toggle Left")
    def toggleBottom():
      print("Toggle Bottom")

  class Fingers():
    def Index(layer):
      if layer == 0:
        RightHand.ChangingLayers.PinkyChangingMenu.ChangetoLayer1()
      if layer == 1:
        RightHand.Layer1.leftClick()
      if layer == 2:
        RightHand.Layer2.toggleTop()
      if layer == 3:
        RightHand.Layer3.toggleTop()
    def Middle(layer):
      if layer == 0:
        RightHand.ChangingLayers.PinkyChangingMenu.ChangetoLayer2()
      if layer == 1:
        RightHand.Layer1.doubleLeftClick()
      if layer == 2:
        RightHand.Layer2.toggleRight()
      if layer == 3:
        RightHand.Layer3.toggleRight()
    def Ring(layer):
      if layer == 0:
        RightHand.ChangingLayers.PinkyChangingMenu.ChangetoLayer3()
      if layer == 1:
        RightHand.Layer1.middleClick()
      if layer == 2:
        RightHand.Layer2.toggleLeft()
      if layer == 3:
        RightHand.Layer3.toggleLeft()
    def Pinky(layer):
      if layer == 0:
        print("fuck you0")
      if layer == 1:
        print("fuck you1")
        RightHand.ChangingLayers.ChangeHandLayer("Changer",1)
      if layer == 2:
        print("fuck you2")
        RightHand.ChangingLayers.ChangeHandLayer("Changer",2)
      if layer == 3:
        print("fuck you3")
        RightHand.ChangingLayers.ChangeHandLayer("Changer",3)


class BothHands():
  def ChangeHandLayer(layer):
      if layer == 1:
        Rpath = "Right Hand.Layer 1"
        Lpath = "Left Hand.Layer 1"
      elif layer == 2:
        Rpath = "Right Hand.Layer 2"
        Lpath = "Left Hand.Layer 2"
      elif layer == 3:
        Rpath = "Right Hand.Layer 3"
        Lpath = "Left Hand.Layer 3"
      elif layer == 4:
        Rpath = "Right Hand.Layer 4"
        Lpath = "Left Hand.Layer 4"
      new_value = True
      with open("_settings/handLayer.json", 'r') as f:
          data = json.load(f)

      # Split the path into individual keys
      Rkeys = Rpath.split('.')
      Lkeys = Lpath.split('.')

      # Update the value at the specified path
      current_object = data
      for key in Rkeys[:-1]:
          if key not in current_object:
              current_object[key] = {}
          current_object = current_object[key]
      current_object[Rkeys[-1]] = new_value
      for key in Lkeys[:-1]:
          if key not in current_object:
              current_object[key] = {}
          current_object = current_object[key]
      current_object[Lkeys[-1]] = new_value

      with open("_settings/handLayer.json", 'w') as f:
          json.dump(data, f, indent=4)
          
  class Layer1():
    def option1():
      print("Option 1")
    def option2():
      print("Option 2")
    def option3():
      print("Option 3")
    def option4():
      print("Option 4")

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