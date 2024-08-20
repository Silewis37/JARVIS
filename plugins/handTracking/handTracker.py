# File Name: handTracker.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] 

#* Libraries *#

import cv2
import mediapipe as mp
import mediapipe.python.solutions.face_mesh as mpD
import numpy as np
from google.protobuf.json_format import MessageToDict 
import json

#* Custom Libraries *#

import plugins.handTracking.handFunctions as handFunc

#^ Variables ^#

mp_hands = mp.solutions.hands


hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=2,
                       min_detection_confidence=0.75,
                       min_tracking_confidence=0.99)

mp_drawing = mp.solutions.drawing_utils

# Open The Camera
cap = cv2.VideoCapture(0)



#& Functions &#
def Draw_TrackingBox(frame1):
    shapes = np.zeros_like(frame1, np.uint8)
    
    cv2.line(frame1, (80,80), (80,640), (0,0,0) , 2)
    cv2.line(frame1, (80,80), (1200,80), (0,0,0) , 2)
    cv2.line(frame1, (80,640), (1200,640), (0,0,0) , 2)
    cv2.line(frame1, (1200,80), (1200,640), (0,0,0) , 2)
    cv2.rectangle(frame1, (80,80), (1200,640), (0,0,255), -1)
    out = frame1.copy()
    alpha = 0.5
    mask = shapes.astype(bool)
    out[mask] = cv2.addWeighted(frame1, alpha, shapes, 1 - alpha, 0)[mask]

def Draw_TrackingBox2(frame1):
    shapes = np.zeros_like(frame1, np.uint8)
    
    cv2.line(frame1, (160,160), (160,580), (0,0,0) , 2)
    cv2.line(frame1, (160,160), (1120,160), (0,0,0) , 2)
    cv2.line(frame1, (160,580), (1120,580), (0,0,0) , 2)
    cv2.line(frame1, (1120,160), (1120,580), (0,0,0) , 2)
    cv2.rectangle(frame1, (160,160), (1120,580), (0,0,255), -1)
    out = frame1.copy()
    alpha = 0.5
    mask = shapes.astype(bool)
    out[mask] = cv2.addWeighted(frame1, alpha, shapes, 1 - alpha, 0)[mask]
    cv2.add(frame1,out)


def main():
  # Both Hands
  index = False
  middle = False
  ring = False  
  pinky = False
  # Right Hand
  right_index = False
  right_middle = False
  right_ring = False 
  right_pinky = False
  # Left Hand
  left_index = False
  left_middle = False
  left_ring = False  
  left_pinky = False
  
  frame_width = 1280
  frame_height = 720

  
  
    # Error Check to Make Sure The Camera is Open
  if not cap.isOpened():
      
      print("Error")
  # Main Loop
  while True:
      # Capture Frame by Frame From The Camera
      success, frame = cap.read()
      if not success:
          break
      
      # Flip The Frame Horizontally 
      frame = cv2.flip(frame, 1)
      
      TopZone, RightZone, LeftZone, BottomZone = handFunc.BoundingBox.DeadZoneChecking.CheckActiveZones()
      
      RightHandActiveLayer = handFunc.RightHand.CheckingLayers.CheckActiveLayer()
      LeftHandActiveLayer = handFunc.LeftHand.CheckingLayers.CheckActiveLayer()
      
      if TopZone == True:
        handFunc.BoundingBox.DeadZone.Top(frame, frame_width)
      if RightZone == True:
        handFunc.BoundingBox.DeadZone.Right(frame, frame_height)
      if LeftZone == True:
        handFunc.BoundingBox.DeadZone.Left(frame, frame_height)
      if BottomZone == True:
        handFunc.BoundingBox.DeadZone.Bottom(frame, frame_width)
      #Draw_TrackingBox(frame)
      #Draw_TrackingBox2(frame)

      # Convert The Frame Color From BGR to RGB
      rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

      # Process Rhe RGB Frame with MediaPipe Hands
      results = hands.process(rgb_frame)
    #   print("Frame Width: " + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
    #   print("Frame Height: " + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))) 

      cv2.putText(frame, "FPS: " + str(cap.get(cv2.CAP_PROP_FPS)), (1100,50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)

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
              
              
              if len(results.multi_handedness) == 2:
                cv2.putText(frame, 'Both Hands', (20, 50), 
                        cv2.FONT_HERSHEY_COMPLEX, 
                        0.9, (0, 255, 0), 2) 
                # Get The Distance Between The Thumb and Index Finger
                distance_index = np.sqrt((index_finger_tip.x - thumb_tip.x)**2 + (index_finger_tip.y - thumb_tip.y)**2)
                distance_middle = np.sqrt((middle_finger_tip.x - thumb_tip.x)**2 + (middle_finger_tip.y - thumb_tip.y)**2)
                distance_ring = np.sqrt((ring_finger_tip.x - thumb_tip.x)**2 + (ring_finger_tip.y - thumb_tip.y)**2)
                distance_pinky = np.sqrt((pinky_finger_tip.x - thumb_tip.x)**2 + (pinky_finger_tip.y - thumb_tip.y)**2)
                
                
                #- Both Hands Text Display
                
                if distance_index < 0.05 and index == False:
                    index = True
                    handFunc.BothHands.Layer1.option1()
                    cv2.putText(frame, "Index Connected", 
                                (20, 80), 
                                cv2.FONT_HERSHEY_COMPLEX,  
                                0.9, (0, 255, 0), 2) 
                if distance_index > 0.051 and index == True:
                    index = False
                if distance_middle < 0.05 and middle == False:
                    # Mouse Double Click
                    middle = True
                    handFunc.BothHands.Layer1.option2()
                    cv2.putText(frame, "Middle Connected", 
                                (20, 80), 
                                cv2.FONT_HERSHEY_COMPLEX,  
                                0.9, (0, 255, 0), 2) 
                if distance_middle > 0.051 and middle == True:
                    # Mouse Double Click
                    middle = False
                if distance_ring < 0.05 and ring == False:
                    # Mouse Right Click
                    ring = True
                    handFunc.BothHands.Layer1.option3()
                    cv2.putText(frame, "Ring Connected", 
                                (20, 80), 
                                cv2.FONT_HERSHEY_COMPLEX,  
                                0.9, (0, 255, 0), 2) 
                if distance_ring > 0.051 and ring == True:
                    # Mouse Right Click
                    ring = False
                if distance_pinky < 0.06 and pinky == False:
                    # Mouse Right Click
                    pinky = True
                    handFunc.BothHands.Layer1.option4()
                    cv2.putText(frame, "Pinky Connected", 
                                (20, 80), 
                                cv2.FONT_HERSHEY_COMPLEX,  
                                0.9, (0, 255, 0), 2) 
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
                    # Display 'Both Hands' on the image 
              
            # Both Hands are present in image(frame) 
          #- Both Hands Dictator
          if len(results.multi_handedness) == 2:
              #f = open("./test.txt", "w+")
              #f.write(str(results.HandLandmarkerResult))
              cv2.putText(frame, 'Both Hands', (20, 50), 
                        cv2.FONT_HERSHEY_COMPLEX, 
                        0.9, (0, 255, 0), 2) 
  
          else: 
            for i in results.multi_handedness: 
                
                # Return whether it is Right or Left Hand 
                data = MessageToDict(i)
                label = data['classification'][0]['label']
                f = open("./output.json", "w")
                data1 = json.dumps(data, indent=4)
                f.write(data1)

                #- Left Hand Dictator

                if label == 'Left': 
                    right_index = False
                    right_middle = False
                    right_ring = False 
                    right_pinky = False
                    distance_index_left = np.sqrt((index_finger_tip.x - thumb_tip.x)**2 + (index_finger_tip.y - thumb_tip.y)**2)
                    distance_middle_left = np.sqrt((middle_finger_tip.x - thumb_tip.x)**2 + (middle_finger_tip.y - thumb_tip.y)**2)
                    distance_ring_left = np.sqrt((ring_finger_tip.x - thumb_tip.x)**2 + (ring_finger_tip.y - thumb_tip.y)**2)
                    distance_pinky_left = np.sqrt((pinky_finger_tip.x - thumb_tip.x)**2 + (pinky_finger_tip.y - thumb_tip.y)**2)
                    
                    
                    if distance_index_left < 0.5 and left_index == False:
                        left_index = True
                    if distance_index_left > 0.051 and left_index == True:
                        left_index = False
                    
                    if distance_middle_left < 0.5 and left_middle == False:
                        left_middle = True
                    if distance_middle_left > 0.051 and left_middle == True:
                        left_middle = False
                    
                    if distance_ring_left < 0.5 and left_ring == False:
                        left_ring = True
                    if distance_ring_left > 0.051 and left_ring == True:
                        left_ring = False
                    
                    if distance_pinky_left < 0.5 and left_pinky == False:
                        left_pinky = True
                    if distance_pinky_left > 0.051 and left_pinky == True:
                        left_pinky = False
                    
                    if layer == 1:
                        handFunc.LeftHand.Layer1.color(frame, thumb_coord_real, index_finger_coord_real, middle_finger_real, ring_finger_real, pinky_finger_real, midpoint_index, midpoint_ring, midpoint_middle, midpoint_pinky)
                    elif layer == 2:
                        handFunc.LeftHand.Layer2.color(frame, thumb_coord_real, index_finger_coord_real, middle_finger_real, ring_finger_real, pinky_finger_real, midpoint_index, midpoint_ring, midpoint_middle, midpoint_pinky)                    
                    elif layer == 3:
                        handFunc.LeftHand.Layer3.color(frame, thumb_coord_real, index_finger_coord_real, middle_finger_real, ring_finger_real, pinky_finger_real, midpoint_index, midpoint_ring, midpoint_middle, midpoint_pinky)
                    
                    #: Left Hand Index :#
                    if left_index:
                        # Draw a Circle at The Midpoint with Radius 10
                        cv2.circle(frame, (int(midpoint_x_index * frame_width), int(midpoint_y_index * frame_height)), 10, (0, 255, 255), -1)
                    else:
                        # Draw a Circle at The Midpoint with Radius 10
                        cv2.circle(frame, (int(midpoint_x_index * frame_width), int(midpoint_y_index * frame_height)), 10, (0, 255, 255), 1)
                    #: Left Hand Middle :#
                    if left_middle:
                        # Draw a Circle at The Midpoint with Radius 10
                        cv2.circle(frame, (int(midpoint_x_middle * frame_width), int(midpoint_y_middle * frame_height)), 10, (204, 0, 153), -1)
                    else:
                        # Draw a Circle at The Midpoint with Radius 10
                        cv2.circle(frame, (int(midpoint_x_middle * frame_width), int(midpoint_y_middle * frame_height)), 10, (204, 0, 153), 1)
                    #: Left Hand Ring :#
                    if left_ring:
                        # Draw a Circle at The Midpoint with Radius 10
                        cv2.circle(frame, (int(midpoint_x_ring * frame_width), int(midpoint_y_ring * frame_height)), 10, (51, 51, 255), -1)
                    else:
                        # Draw a Circle at The Midpoint with Radius 10
                        cv2.circle(frame, (int(midpoint_x_ring * frame_width), int(midpoint_y_ring * frame_height)), 10, (51, 51, 255), 1)
                    #: Left Hand Pinky :#
                    if left_pinky:
                        # Draw a Circle at The Midpoint with Radius 10
                        cv2.circle(frame, (int(midpoint_x_pinky * frame_width), int(midpoint_y_pinky * frame_height)), 10, (0, 153, 51), -1)
                    else:
                        # Draw a Circle at The Midpoint with Radius 10
                        cv2.circle(frame, (int(midpoint_x_pinky * frame_width), int(midpoint_y_pinky * frame_height)), 10, (0, 153, 51), 1)
                    
                    cv2.putText(frame, label+' Hand || Layer: '+str(LeftHandActiveLayer), 
                                (20, 50), 
                                cv2.FONT_HERSHEY_COMPLEX,  
                                0.9, (0, 255, 0), 2) 

                #- Right Hand Dictator

                if label == 'Right': 
                    left_index = False
                    left_middle = False
                    left_ring = False  
                    left_pinky = False
                    # Get The Distance Between The Thumb and Index Finger
                    distance_index_right = np.sqrt((index_finger_tip.x - thumb_tip.x)**2 + (index_finger_tip.y - thumb_tip.y)**2)
                    distance_middle_right = np.sqrt((middle_finger_tip.x - thumb_tip.x)**2 + (middle_finger_tip.y - thumb_tip.y)**2)
                    distance_ring_right = np.sqrt((ring_finger_tip.x - thumb_tip.x)**2 + (ring_finger_tip.y - thumb_tip.y)**2)
                    distance_pinky_right = np.sqrt((pinky_finger_tip.x - thumb_tip.x)**2 + (pinky_finger_tip.y - thumb_tip.y)**2)
                    
                    if distance_index_right < 0.05 and right_index == False:
                        # Mouse Down
                        right_index = True
                    if distance_index_right > 0.051 and right_index == True:
                        # Mouse Up
                        right_index = False
                    if distance_middle_right < 0.05 and right_middle == False:
                        # Mouse Double Click
                        right_middle = True
                    if distance_middle_right > 0.051 and right_middle == True:
                        # Mouse Double Click
                        right_middle = False
                    if distance_ring_right < 0.05 and right_ring == False:
                        # Mouse Right Click
                        right_ring = True
                    if distance_ring_right > 0.051 and right_ring == True:
                        # Mouse Right Click
                        right_ring = False
                    if distance_pinky_right < 0.06 and right_pinky == False:
                        # Mouse Right Click
                        right_pinky = True
                    if distance_pinky_right > 0.061 and right_pinky == True:
                        # Mouse Right Click
                        right_pinky = False
                    
                    layer = handFunc.RightHand.CheckingLayers.CheckActiveLayer()
                    
                    if layer == 1:
                        handFunc.RightHand.Layer1.color(frame, thumb_coord_real, index_finger_coord_real, middle_finger_real, ring_finger_real, pinky_finger_real, midpoint_index, midpoint_ring, midpoint_middle, midpoint_pinky)
                    elif layer == 2:
                        handFunc.RightHand.Layer2.color(frame, thumb_coord_real, index_finger_coord_real, middle_finger_real, ring_finger_real, pinky_finger_real, midpoint_index, midpoint_ring, midpoint_middle, midpoint_pinky)                    
                    elif layer == 3:
                        handFunc.RightHand.Layer3.color(frame, thumb_coord_real, index_finger_coord_real, middle_finger_real, ring_finger_real, pinky_finger_real, midpoint_index, midpoint_ring, midpoint_middle, midpoint_pinky)
                    
                    
                    # cv2.line(frame, (thumb_coord_real[0], thumb_coord_real[1]), (midpoint_index[0], midpoint_index[1]), (102, 255, 102), 2)
                    # cv2.line(frame, (index_finger_coord_real[0], index_finger_coord_real[1]), (midpoint_index[0], midpoint_index[1]), (102, 255, 102), 2)
                    
                    # cv2.line(frame, (thumb_coord_real[0], thumb_coord_real[1]), (midpoint_middle[0], midpoint_middle[1]), (255, 102, 255), 2)
                    # cv2.line(frame, (middle_finger_real[0], middle_finger_real[1]), (midpoint_middle[0], midpoint_middle[1]), (255, 102, 255), 2)
                    
                    # cv2.line(frame, (thumb_coord_real[0], thumb_coord_real[1]), (midpoint_ring[0], midpoint_ring[1]), (51, 102, 255), 2)
                    # cv2.line(frame, (ring_finger_real[0], ring_finger_real[1]), (midpoint_ring[0], midpoint_ring[1]), (51, 102, 255), 2)
                    
                    # cv2.line(frame, (thumb_coord_real[0], thumb_coord_real[1]), (midpoint_pinky[0], midpoint_pinky[1]), (255, 102, 102), 2)
                    # cv2.line(frame, (pinky_finger_real[0], pinky_finger_real[1]), (midpoint_pinky[0], midpoint_pinky[1]), (255, 102, 102), 2)
                    
                    
                    
                    #: Right Hand Index :#
                    if right_index:
                        # Draw a Circle at The Midpoint with Radius 10
                        cv2.circle(frame, (int(midpoint_x_index*frame_width), int(midpoint_y_index * frame_height)), 10, (102, 255, 102), -1)
                    else:
                        # Draw a Circle at The Midpoint with Radius 10
                        cv2.circle(frame, (int(midpoint_x_index*frame_width), int(midpoint_y_index * frame_height)), 10, (102, 255, 102), 1)
                    #: Right Hand Middle :#
                    if right_middle:
                        # Draw a Circle at The Midpoint with Radius 10
                        cv2.circle(frame, (int(midpoint_x_middle*frame_width), int(midpoint_y_middle * frame_height)), 10, (255, 102, 255), -1)
                    else:
                        # Draw a Circle at The Midpoint with Radius 10
                        cv2.circle(frame, (int(midpoint_x_middle*frame_width), int(midpoint_y_middle * frame_height)), 10, (255, 102, 255), 1)
                    #: Right Hand Ring :#
                    if right_ring:
                        # Draw a Circle at The Midpoint with Radius 10
                        cv2.circle(frame, (int(midpoint_x_ring*frame_width), int(midpoint_y_ring * frame_height)), 10, (51, 102, 255), -1)
                    else:
                        # Draw a Circle at The Midpoint with Radius 10
                        cv2.circle(frame, (int(midpoint_x_ring*frame_width), int(midpoint_y_ring * frame_height)), 10, (51, 102, 255), 1)
                    #: Right Hand Pinky :#
                    if right_pinky:
                        # Draw a Circle at The Midpoint with Radius 10
                        cv2.circle(frame, (int(midpoint_x_pinky*frame_width), int(midpoint_y_pinky * frame_height)), 10, (255, 102, 102), -1)
                    else:
                        # Draw a Circle at The Midpoint with Radius 10
                        cv2.circle(frame, (int(midpoint_x_pinky*frame_width), int(midpoint_y_pinky * frame_height)), 10, (255, 102, 102), 1)
                    #| On left side of window 
                    cv2.putText(frame, label+' Hand || Layer: '+str(RightHandActiveLayer), (20, 50), 
                                cv2.FONT_HERSHEY_COMPLEX, 
                                0.9, (0, 255, 0), 2) 
                
                #- Right Hand Text Display
                
                RightActiveLayer = handFunc.RightHand.CheckingLayers.CheckActiveLayer()
                
                #: Right Hand Index :#
                if right_index == True:
                    handFunc.RightHand.Fingers.Index(RightActiveLayer)
                    cv2.putText(frame, "Right Hand Index Connected", 
                                (20, 80), 
                                cv2.FONT_HERSHEY_COMPLEX,  
                                0.9, (0, 255, 0), 2) 
                #: Right Hand Middle :#
                if right_middle == True:
                    handFunc.RightHand.Fingers.Middle(RightActiveLayer)
                    cv2.putText(frame, "Right Hand Middle Connected", 
                                (20, 80), 
                                cv2.FONT_HERSHEY_COMPLEX,  
                                0.9, (0, 255, 0), 2) 
                #: Right Hand Ring :#
                if right_ring == True:
                    handFunc.RightHand.Fingers.Ring(RightActiveLayer)
                    cv2.putText(frame, "Right Hand Ring Connected", 
                                (20, 80), 
                                cv2.FONT_HERSHEY_COMPLEX,  
                                0.9, (0, 255, 0), 2) 
                #: Right Hand Pinky :#
                if right_pinky == True:
                    handFunc.RightHand.Fingers.Pinky(RightActiveLayer)
                    cv2.putText(frame, "Right Hand Pinky Connected", 
                                (20, 80), 
                                cv2.FONT_HERSHEY_COMPLEX,  
                                0.9, (0, 255, 0), 2) 
                
                #- Left Hand Text Display
                
                LeftActiveLayer = handFunc.LeftHand.CheckingLayers.CheckActiveLayer()
                
                #: Left Hand Index :#
                if left_index == True:
                        handFunc.LeftHand.Fingers.Index(LeftActiveLayer)
                        cv2.putText(frame, "Left Hand Index Connected", 
                                (20, 80), 
                                cv2.FONT_HERSHEY_COMPLEX,  
                                0.9, (0, 255, 0), 2) 
                #: Left Hand Middle :#
                if left_middle == True:
                        handFunc.LeftHand.Fingers.Middle(LeftActiveLayer)
                        cv2.putText(frame, "Left Hand Middle Connected", 
                                (20, 80), 
                                cv2.FONT_HERSHEY_COMPLEX,  
                                0.9, (0, 255, 0), 2) 
                #: Left Hand Ring :#
                if left_ring == True:
                        handFunc.LeftHand.Fingers.Ring(LeftActiveLayer)
                        cv2.putText(frame, "Left Hand Ring Connected", 
                                (20, 80), 
                                cv2.FONT_HERSHEY_COMPLEX,  
                                0.9, (0, 255, 0), 2) 
                #: Left Hand Pinky :#
                if left_pinky == True:
                        handFunc.LeftHand.Fingers.Pinky(LeftActiveLayer)
                        cv2.putText(frame, "Left Hand Pinky Connected", 
                                (20, 80), 
                                cv2.FONT_HERSHEY_COMPLEX,  
                                0.9, (0, 255, 0), 2) 







      # Draw The Hand Annotations on The Frame.
      if results.multi_hand_landmarks:
          for hand_landmarks in results.multi_hand_landmarks:
              #Draw Landmarks
              mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

      # Display The Resulting Frame
      cv2.imshow("Frame", frame)
      cv2.waitKey(1)

  cap.release()
  cv2.destroyAllWindows()

#= Classes =#

#~ define and build classes here

#! Main Program !#

main() 

#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#


#@ Other Functions @#

def handRecgonData(result):
    for i in result.multi_handedness:
                        hand = MessageToDict(i)
    land = str(result.multi_hand_landmarks)
    fil = open("./output.json", "w")
    data = json.dumps(hand, indent=4)
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