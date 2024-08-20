# File Name: handToMouse.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] TO-DO List Item
#[*] Completed TO-DO List Item

#* Libraries *#

import cv2
import mediapipe as mp
import pyautogui as pag
import numpy as np


#* Custom Libraries *#

#~ import custom made libraries here

#^ Variables ^#

# Initialize Mediapipe Hand solution
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=2,
                       min_detection_confidence=0.85,
                       min_tracking_confidence=0.95)

mp_drawing = mp.solutions.drawing_utils

#open the camera
cap = cv2.VideoCapture(0)
# Set the screen resolution (width, height)
screen_width, screen_height = pag.size()

# global mouseDown
# global mouseDownDB
# global mouseRight
# mouseDown = False
# mouseDownDB = False
# mouseRight = False

global circle
circle = 0


#& Functions &#

def mouse():
  mouseDown = False
  mouseDownDB = False
  mouseRight = False        
  # Error Check to Make Sure The Camera is Open
#   if not cap.isOpened():
#       print("Error")
#       exit()

  # Main loop
  while True:

      # Capture Frame by Frame From The Camera
      success, frame = cap.read()
      if not success:
          break
      
      # Flip The Frame Horizontally 
      frame = cv2.flip(frame, 1)

      # Convert The Frame Color From BGR to RGB
      rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

      # Process The RGB Frame with MediaPipe Hands
      results = hands.process(rgb_frame)

      # Frame Resolution
      frame_height, frame_width, _ = frame.shape

      if results.multi_hand_landmarks:
          for hand_landmarks in results.multi_hand_landmarks:
              # Draw Landmarks
              mp_drawing.draw_landmarks(frame, hand_landmarks,mp_hands.HAND_CONNECTIONS)

              index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
              thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
              middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
              ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]

              # Get The Midpoint Between The Thumb and Index Finger
              midpoint_x = (index_finger_tip.x + thumb_tip.x) /2
              midpoint_y = (index_finger_tip.y + thumb_tip.y) /2
              midpoint_xdb = (middle_finger_tip.x + thumb_tip.x) /2
              midpoint_ydb = (middle_finger_tip.y + thumb_tip.y) /2
              midpoint_xrc = (ring_finger_tip.x + thumb_tip.x) /2
              midpoint_yrc = (ring_finger_tip.y + thumb_tip.y) /2
              
              

              # Get The Distance Between The Thumb and Index Finger
              distance = np.sqrt((index_finger_tip.x - thumb_tip.x)**2 + (index_finger_tip.y - thumb_tip.y)**2)
              distance_db = np.sqrt((middle_finger_tip.x - thumb_tip.x)**2 + (middle_finger_tip.y - thumb_tip.y)**2)
              distance_rc = np.sqrt((ring_finger_tip.x - thumb_tip.x)**2 + (ring_finger_tip.y - thumb_tip.y)**2)

              if distance < 0.05 and mouseDown == False:
                  # Mouse Down
                  pag.mouseDown()
                  mouseDown = True
              if distance > 0.051 and mouseDown == True:
                  # Mouse Up
                  pag.mouseUp()
                  mouseDown = False
              if distance_db < 0.05 and mouseDownDB == False:
                  # Mouse Double Click
                  pag.doubleClick()
                  mouseDownDB = True
              if distance_db > 0.051 and mouseDownDB == True:
                  # Mouse Double Click
                  mouseDownDB = False
              if distance_rc < 0.05 and mouseRight == False:
                  # Mouse Right Click
                  pag.rightClick()
                  mouseRight = True
              if distance_rc > 0.051 and mouseRight == True:
                  # Mouse Right Click
                  mouseRight = False
              
              
              
              if mouseDown:
                  # Draw a Circle at The Midpoint with Radius 10
                  cv2.circle(frame, (int(midpoint_x*frame_width), int(midpoint_y * frame_height)), 10, (0, 255,0), -1)

              else:
                  # Draw a Circle at The Midpoint with Radius 10
                  cv2.circle(frame, (int(midpoint_x*frame_width), int(midpoint_y * frame_height)), 10, (0, 255,0), 1)
              
              if mouseDownDB:
                  # Draw a Circle at The Midpoint with Radius 10
                  cv2.circle(frame, (int(midpoint_x*frame_width), int(midpoint_y * frame_height)), 10, (0, 0, 255), -1)

              else:
                  # Draw a Circle at The Midpoint with Radius 10
                  cv2.circle(frame, (int(midpoint_x*frame_width), int(midpoint_y * frame_height)), 10, (0, 0, 255), 1)
              
              if mouseRight:
                  # Draw a Circle at The Midpoint with Radius 10
                  cv2.circle(frame, (int(midpoint_x*frame_width), int(midpoint_y * frame_height)), 10, (255, 0, 0), -1)

              else:
                  # Draw a Circle at The Midpoint with Radius 10
                  cv2.circle(frame, (int(midpoint_x*frame_width), int(midpoint_y * frame_height)), 10, (255, 0, 0), 1)
              

              # Map The Position to The Screen Resolution
              x_mapped = np.interp(midpoint_x, (0,1), (0, 1680))
              y_mapped = np.interp(midpoint_y, (0,1), (0, 1050))

              # Set The Mouse Position
              pag.moveTo(x_mapped, y_mapped+50, duration= 0.1)
              
      # Display The Resulting Frame
      cv2.imshow("Mediapipe Hands", frame)
      cv2.waitKey(1)

  # When Everything Done, Release The Capture
  cap.release()
  cv2.destroyAllWindows()


#= Classes =#

#~ define and build classes here

#! Main Program !#

mouse()


#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#