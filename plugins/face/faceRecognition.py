# File Name: faceRecognition.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] TO-DO List Item
#[*] Completed TO-DO List Item

#* Libraries *#

import cv2
import mediapipe as mp
import time

#* Custom Libraries *#

#~ import custom made libraries here

#^ Variables ^#

#~ create and store variables here

#& Functions &#

def main():
    cap = cv2.VideoCapture(0)
    detector = FaceDetection()
    ptime=0
    while True:
        success, img = cap.read()
        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        img = detector.faceDetect(img)

        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (36, 23, 21), 3)
        cv2.imshow('Image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

#= Classes =#

class FaceDetection():

    def __init__(self,min_detection_confidence= 0.6,model_selection= 0):
        self.min_detection_confidence = min_detection_confidence
        self.model_selection = model_selection
        self.mpFace = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFace.FaceDetection(self.min_detection_confidence,self.model_selection)

    def faceDetect(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)

        if self.results.detections:
            for id, det in enumerate(self.results.detections):
                # mpDraw.draw_detection(img,det)
                # print(id,det)
                # print(det.score)
                # print(det.location_data.relative_bounding_box)
                bbox = det.location_data.relative_bounding_box
                h, w, c = img.shape
                bb = int(bbox.xmin * w), int(bbox.ymin * h), \
                     int(bbox.width * w), int(bbox.height * h)
                cv2.rectangle(img, bb, (255, 219, 50), 2)
                cv2.putText(img, f'{int(det.score[0] * 100)}%',
                            (bb[0], bb[1] - 20), cv2.FONT_HERSHEY_PLAIN,
                            2, (230, 199, 0), 3)

        return img

#! Main Program !#

if __name__ =='__main__':
    main()



#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#