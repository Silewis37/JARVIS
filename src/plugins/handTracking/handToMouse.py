# File Name: handToMouse.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] TO-DO List Item
#[*] Completed TO-DO List Item

#* Libraries *#

import cv2
import mediapipe as mp
import pyautogui as pag
import sys
import os
import numpy as np


#* Custom Libraries *#

sys.path.append(os.path.abspath("./src"))
import plugins.handTracking.handFunctions as handFunc


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

def clear():
    os.system("cls")

# Button Class with Action Binding
class Button:
    def __init__(self, x, y, width, height, label, on_click, color_idle=(0, 200, 0), color_active=(0, 0, 200)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.on_click = on_click
        self.color_idle = color_idle
        self.color_active = color_active
        self.pressed = False
        self.was_pressed = False

    def draw(self, frame):
        color = self.color_active if self.pressed else self.color_idle
        cv2.rectangle(frame, (self.x, self.y),
                      (self.x + self.width, self.y + self.height),
                      color, -1)
        cv2.putText(frame, self.label, 
                    (self.x + 10, self.y + self.height // 2 + 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    def is_point_inside(self, px, py):
        return self.x <= px <= self.x + self.width and self.y <= py <= self.y + self.height

    def update(self, px, py, pinch):
        if pinch and self.is_point_inside(px, py):
            self.pressed = True
            if not self.was_pressed:
                self.on_click()
                self.was_pressed = True
        else:
            self.pressed = False
            self.was_pressed = False


def say_hello():
    print("hello fucker")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def mouse2():
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, screen_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, screen_height)

    # Create buttons
    send_button = Button(x=100, y=100, width=200, height=80, label="Say Hello", on_click=say_hello)
    clear_button = Button(x=100, y=220, width=200, height=80, label="Clear Terminal", on_click=clear_terminal)

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        frame_height, frame_width, _ = frame.shape

        # Solid black background
        canvas = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)

        px, py = 0, 0
        pinch = False

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

                midpoint_x = (index_tip.x + thumb_tip.x) / 2
                midpoint_y = (index_tip.y + thumb_tip.y) / 2
                distance = np.sqrt((index_tip.x - thumb_tip.x) ** 2 +
                                   (index_tip.y - thumb_tip.y) ** 2)

                px = int(midpoint_x * frame_width)
                py = int(midpoint_y * frame_height)
                pinch = distance < 0.05

        # Draw buttons first
        send_button.update(px, py, pinch)
        clear_button.update(px, py, pinch)

        send_button.draw(canvas)
        clear_button.draw(canvas)

        # Draw the midpoint dot LAST so it's on top of everything
        if results.multi_hand_landmarks:
            cv2.circle(canvas, (px, py), 8, (0, 255, 255), -1)  # yellow dot on top

        # Display result
        cv2.imshow("Midpoint on Top", canvas)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()




def mouse():
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, screen_width)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, screen_height)
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



#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#