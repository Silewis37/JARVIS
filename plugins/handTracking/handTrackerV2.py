# File Name: handTrackerV2.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] TO-DO List Item
#[*] Completed TO-DO List Item

#* Libraries *#

import cv2
import mediapipe as mp
import pyautogui as pag
from google.protobuf.json_format import MessageToDict 
import json
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

def main():
  index = False
  middle = False
  ring = False  
  pinky = False       
  # Error Check to Make Sure The Camera is Open
  if not cap.isOpened():
      print("Error")
      exit()

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
              pinky_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

              # Get The Midpoint Between The Thumb and Index Finger
              midpoint_x_index = (index_finger_tip.x + thumb_tip.x) /2
              midpoint_y_index = (index_finger_tip.y + thumb_tip.y) /2
              midpoint_x_middle = (middle_finger_tip.x + thumb_tip.x) /2
              midpoint_y_middle = (middle_finger_tip.y + thumb_tip.y) /2
              midpoint_x_ring = (ring_finger_tip.x + thumb_tip.x) /2
              midpoint_y_ring = (ring_finger_tip.y + thumb_tip.y) /2
              midpoint_x_pinky = (pinky_finger_tip.x + thumb_tip.x) /2
              midpoint_y_pinky = (pinky_finger_tip.y + thumb_tip.y) /2
              
              index_finger_coord_real = [int(index_finger_tip.x*frame.shape[1]),
                                           int(index_finger_tip.y*frame.shape[0])]
              
              thumb_coord_real = [int(thumb_tip.x*frame.shape[1]),
                                           int(thumb_tip.y*frame.shape[0])]
              
              middle_finger_real = [int(middle_finger_tip.x*frame.shape[1]),
                                           int(middle_finger_tip.y*frame.shape[0])]
              
              ring_finger_real = [int(ring_finger_tip.x*frame.shape[1]),
                                           int(ring_finger_tip.y*frame.shape[0])]
              
              pinky_finger_real = [int(pinky_finger_tip.x*frame.shape[1]),
                                           int(pinky_finger_tip.y*frame.shape[0])]
              
              midpoint_index = [int(midpoint_x_index*frame.shape[1]),
                                           int(midpoint_y_index*frame.shape[0])]
              
              midpoint_middle = [int(midpoint_x_middle*frame.shape[1]),
                                           int(midpoint_y_middle*frame.shape[0])]
              
              midpoint_ring = [int(midpoint_x_ring*frame.shape[1]),
                                           int(midpoint_y_ring*frame.shape[0])]
              
              midpoint_pinky = [int(midpoint_x_pinky*frame.shape[1]),
                                           int(midpoint_y_pinky*frame.shape[0])]
              
              cv2.line(frame, (index_finger_coord_real[0]-10, index_finger_coord_real[1]),
                         (index_finger_coord_real[0]+10, index_finger_coord_real[1]), (255, 255, 255), 2)
              cv2.line(frame, (index_finger_coord_real[0], index_finger_coord_real[1]-10),
                         (index_finger_coord_real[0], index_finger_coord_real[1]+10), (255, 255, 255), 2)
              
              cv2.line(frame, (middle_finger_real[0]-10, middle_finger_real[1]),
                         (middle_finger_real[0]+10, middle_finger_real[1]), (255, 255, 255), 2)
              cv2.line(frame, (middle_finger_real[0], middle_finger_real[1]-10),
                         (middle_finger_real[0], middle_finger_real[1]+10), (255, 255, 255), 2)
              
              cv2.line(frame, (ring_finger_real[0]-10, ring_finger_real[1]),
                         (ring_finger_real[0]+10, ring_finger_real[1]), (255, 255, 255), 2)
              cv2.line(frame, (ring_finger_real[0], ring_finger_real[1]-10),
                         (ring_finger_real[0], ring_finger_real[1]+10), (255, 255, 255), 2)
              
              cv2.line(frame, (pinky_finger_real[0]-10, pinky_finger_real[1]),
                         (pinky_finger_real[0]+10, pinky_finger_real[1]), (255, 255, 255), 2)
              cv2.line(frame, (pinky_finger_real[0], pinky_finger_real[1]-10),
                         (pinky_finger_real[0], pinky_finger_real[1]+10), (255, 255, 255), 2)
              
              cv2.line(frame, (thumb_coord_real[0]-10, thumb_coord_real[1]),
                         (thumb_coord_real[0]+10, thumb_coord_real[1]), (255, 255, 255), 2)
              cv2.line(frame, (thumb_coord_real[0], thumb_coord_real[1]-10),
                         (thumb_coord_real[0], thumb_coord_real[1]+10), (255, 255, 255), 2)

              # Get The Distance Between The Thumb and Index Finger
              distance_index = np.sqrt((index_finger_tip.x - thumb_tip.x)**2 + (index_finger_tip.y - thumb_tip.y)**2)
              distance_middle = np.sqrt((middle_finger_tip.x - thumb_tip.x)**2 + (middle_finger_tip.y - thumb_tip.y)**2)
              distance_ring = np.sqrt((ring_finger_tip.x - thumb_tip.x)**2 + (ring_finger_tip.y - thumb_tip.y)**2)
              distance_pinky = np.sqrt((pinky_finger_tip.x - thumb_tip.x)**2 + (pinky_finger_tip.y - thumb_tip.y)**2)

              if distance_index < 0.05 and index == False:
                    # Mouse Down
                    handed = []
                    for i in results.multi_handedness:
                        hand = MessageToDict(i)
                        handed.append(hand)
                    land = str(mp_hands.HAND_CONNECTIONS)
                    fil = open("./output.json", "w")
                    data = json.dumps(handed, indent=4)
                    fil.write(data)
                    fil2 = open("./output2.json", "w")
                    print(str(land))
                    data2 = []
                    landmarks = land.strip("[]").split("landmark {")
                    for landmark in landmarks:
                        if not landmark:
                            continue
                        fields = landmark.strip().split("\n")
                        x = fields[0]
                        y = fields[1]
                        z = fields[2]
                        data2.append({"x": x, "y": y, "z": z})
                    data3 = json.dumps(data2, indent=4)
                    print(land)
                    fil2.write(data3)
                    index = True
                    cv2.putText(frame, "Index Connected", 
                                (20, 80), 
                                cv2.FONT_HERSHEY_COMPLEX,  
                                0.9, (0, 255, 0), 2) 
              if distance_index > 0.051 and index == True:
                    # Mouse Up
                    index = False
              if distance_middle < 0.05 and middle == False:
                    # Mouse Double Click
                    middle = True
              if distance_middle > 0.051 and middle == True:
                    # Mouse Double Click
                    middle = False
              if distance_ring < 0.05 and ring == False:
                    # Mouse Right Click
                    ring = True
              if distance_ring > 0.051 and ring == True:
                    # Mouse Right Click
                    ring = False
              if distance_pinky < 0.06 and pinky == False:
                    # Mouse Right Click
                    pinky = True
              if distance_pinky > 0.061 and pinky == True:
                    # Mouse Right Click
                    pinky = False
              
              
              cv2.line(frame, (thumb_coord_real[0], thumb_coord_real[1]), (midpoint_index[0], midpoint_index[1]), (0, 255,0), 2)
              cv2.line(frame, (index_finger_coord_real[0], index_finger_coord_real[1]), (midpoint_index[0], midpoint_index[1]), (0, 255,0), 2)
                
              cv2.line(frame, (thumb_coord_real[0], thumb_coord_real[1]), (midpoint_middle[0], midpoint_middle[1]), (0, 0, 255), 2)
              cv2.line(frame, (middle_finger_real[0], middle_finger_real[1]), (midpoint_middle[0], midpoint_middle[1]), (0, 0, 255), 2)
                
              cv2.line(frame, (thumb_coord_real[0], thumb_coord_real[1]), (midpoint_ring[0], midpoint_ring[1]), (255, 0, 0), 2)
              cv2.line(frame, (ring_finger_real[0], ring_finger_real[1]), (midpoint_ring[0], midpoint_ring[1]), (255, 0, 0), 2)
                
              cv2.line(frame, (thumb_coord_real[0], thumb_coord_real[1]), (midpoint_pinky[0], midpoint_pinky[1]), (255, 0, 255), 2)
              cv2.line(frame, (pinky_finger_real[0], pinky_finger_real[1]), (midpoint_pinky[0], midpoint_pinky[1]), (255, 0, 255), 2)
              
              
              if index:
                    # Draw a Circle at The Midpoint with Radius 10
                    cv2.circle(frame, (int(midpoint_x_index*frame_width), int(midpoint_y_index * frame_height)), 10, (0, 255,0), -1)
              else:
                    # Draw a Circle at The Midpoint with Radius 10
                    cv2.circle(frame, (int(midpoint_x_index*frame_width), int(midpoint_y_index * frame_height)), 10, (0, 255,0), 1)
                
              if middle:
                    # Draw a Circle at The Midpoint with Radius 10
                    cv2.circle(frame, (int(midpoint_x_middle*frame_width), int(midpoint_y_middle * frame_height)), 10, (0, 0, 255), -1)
              else:
                    # Draw a Circle at The Midpoint with Radius 10
                    cv2.circle(frame, (int(midpoint_x_middle*frame_width), int(midpoint_y_middle * frame_height)), 10, (0, 0, 255), 1)
                
              if ring:
                    # Draw a Circle at The Midpoint with Radius 10
                    cv2.circle(frame, (int(midpoint_x_ring*frame_width), int(midpoint_y_ring * frame_height)), 10, (255, 0, 0), -1)
              else:
                    # Draw a Circle at The Midpoint with Radius 10
                    cv2.circle(frame, (int(midpoint_x_ring*frame_width), int(midpoint_y_ring * frame_height)), 10, (255, 0, 0), 1)
                
              if pinky:
                    # Draw a Circle at The Midpoint with Radius 10
                    cv2.circle(frame, (int(midpoint_x_pinky*frame_width), int(midpoint_y_pinky * frame_height)), 10, (255, 0, 255), -1)
              else:
                    # Draw a Circle at The Midpoint with Radius 10
                    cv2.circle(frame, (int(midpoint_x_pinky*frame_width), int(midpoint_y_pinky * frame_height)), 10, (255, 0, 255), 1)

              
      # Display The Resulting Frame
      cv2.imshow("Mediapipe Hands", frame)
      cv2.waitKey(1)

  # When Everything Done, Release The Capture
  cap.release()
  cv2.destroyAllWindows()


#= Classes =#

#~ define and build classes here

#! Main Program !#

main()


#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#