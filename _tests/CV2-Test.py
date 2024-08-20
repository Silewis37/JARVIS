import torch
import cv2
import os
from os.path import join


model_path = "yolov5s.pt" # sudoyour model path

# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)  

SCORE_THRESH = 0.4

cap = cv2.VideoCapture(0)

while True:
    ret, image = cap.read()
    i+=1    
        
    if not ret:
        break
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    df = results.pandas().xyxy[0]

    df = df[df.confidence > SCORE_THRESH]
    
    if len(df) > 0:
        # Bounding box
        start_point = (int(df.xmin[0]), int(df.ymin[0]))
        end_point = (int(df.xmax[0]), int(df.ymax[0]))
        image = cv2.rectangle(image, start_point, end_point, (0, 0, 255), 5) 
        
        cv2.imshow('video',image)
cv2.waitKey(0)

cap.release()