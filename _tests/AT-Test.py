# File Name: AT-Test.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] TO-DO List Item

#* Libraries *#

import copy
import time
import argparse
import cv2 as cv
import numpy as np
from pupil_apriltags import Detector
from playsound import playsound
import pyttsx3
import json

#* Custom Libraries *#

#~ import custom made libraries here

#^ Variables ^#

global past_tags
global tag_id
global tag_ids
global board_found
past_tags = []
tag_ids = []
board_found = 0
engine = pyttsx3.init('nsss')

#& Functions &#

def Speak(text):
    rate = 100 #Sets the default rate of speech
    engine.setProperty('rate', rate+50) #Adjusts the rate of speech
    engine.say(text) #tells Python to speak variable 'text'
    engine.runAndWait()

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--device", type=int, default=0)
    parser.add_argument("--width", help='cap width', type=int, default=960)
    parser.add_argument("--height", help='cap height', type=int, default=540)

    parser.add_argument("--families", type=str, default='tag36h11')
    parser.add_argument("--nthreads", type=int, default=1)
    parser.add_argument("--quad_decimate", type=float, default=2.0)
    parser.add_argument("--quad_sigma", type=float, default=0.0)
    parser.add_argument("--refine_edges", type=int, default=1)
    parser.add_argument("--decode_sharpening", type=float, default=0.25)
    parser.add_argument("--debug", type=int, default=0)

    args = parser.parse_args()

    return args


def main():
    global past_tag
    past_tag = 100000
    args = get_args()

    cap_device = args.device
    cap_width = args.width
    cap_height = args.height

    families = args.families
    nthreads = args.nthreads
    quad_decimate = args.quad_decimate
    quad_sigma = args.quad_sigma
    refine_edges = args.refine_edges
    decode_sharpening = args.decode_sharpening
    debug = args.debug

    cap = cv.VideoCapture(cap_device)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, cap_width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, cap_height)

    at_detector = Detector(
        families=families,
        nthreads=nthreads,
        quad_decimate=quad_decimate,
        quad_sigma=quad_sigma,
        refine_edges=refine_edges,
        decode_sharpening=decode_sharpening,
        debug=debug,
    )

    elapsed_time = 0

    while True:
        start_time = time.time()

        ret, image = cap.read()
        if not ret:
            break
        debug_image = copy.deepcopy(image)

        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        tags = at_detector.detect(
            image,
            estimate_tag_pose=False,
            camera_params=None,
            tag_size=None,
        )

        debug_image = draw_tags(debug_image, tags, elapsed_time)

        elapsed_time = time.time() - start_time

        key = cv.waitKey(1)
        if key == 27:  # ESC
            break


        cv.imshow('AprilTag Demo', debug_image)

    cap.release()
    cv.destroyAllWindows()


def draw_tags(
    image,
    tags,
    elapsed_time,
):
    global past_tag
    global board_found
    global tag_ids
    for tag in tags:
        tag_family = tag.tag_family
        tag_id = tag.tag_id
        center = tag.center
        corners = tag.corners

        center = (int(center[0]), int(center[1]))
        corner_01 = (int(corners[0][0]), int(corners[0][1]))
        corner_02 = (int(corners[1][0]), int(corners[1][1]))
        corner_03 = (int(corners[2][0]), int(corners[2][1]))
        corner_04 = (int(corners[3][0]), int(corners[3][1]))

        cv.circle(image, (center[0], center[1]), 5, (0, 0, 255), 2)

        cv.line(image, (corner_01[0], corner_01[1]),
                (corner_02[0], corner_02[1]), (255, 0, 0), 2)
        cv.line(image, (corner_02[0], corner_02[1]),
                (corner_03[0], corner_03[1]), (255, 0, 0), 2)
        cv.line(image, (corner_03[0], corner_03[1]),
                (corner_04[0], corner_04[1]), (0, 255, 0), 2)
        cv.line(image, (corner_04[0], corner_04[1]),
                (corner_01[0], corner_01[1]), (0, 255, 0), 2)

        # cv.putText(image,
        #            str(tag_family) + ':' + str(tag_id),
        #            (corner_01[0], corner_01[1] - 10), cv.FONT_HERSHEY_SIMPLEX,
        #            0.6, (0, 255, 0), 1, cv.LINE_AA)
        cv.putText(image, str(tag_id), (center[0] - 10, center[1] - 10),
                   cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2, cv.LINE_AA)
        
        if tag_id in tag_ids:
            pass
        else:
            tag_ids.append(tag_id)
        
        distance_pixels = np.linalg.norm(np.array(center[0]) - np.array(center[1]))
        pixel_to_inch_ratio = 0.1 # adjust this value based on your camera setup
        distance_inches = distance_pixels * pixel_to_inch_ratio
        f = open("./AT-TEST.txt", "w+")
        f.write(str(tag))
        # print("Distance between AprilTag points: {:.2f} inches".format(distance_inches))   
        # if distance_inches >= 11:
        #     print("Distance between AprilTag points: {:.2f} inches".format(distance_inches))   
        #     pass
        if tag_id == 582:
            tag_ids.clear()
        if board_found == 0:
            if len(tag_ids) == 4:
                print("Board Found.")
                playsound('../audio/online.mp3')
                board_found = 1
                print(board_found)
            else:
                pass
        if board_found == 1:
            if tag_id == 582:
                tag_ids.clear()
                board_found = 0
                print(board_found)
        # if tag_id == 586 and tag_id == 585 and tag_id == 584 and tag_id == 583
        #     print("Board Found.")
        #     playsound('./audio/online.mp3')
        
        # if tag_id != past_tag:
        #     past_tag = tag_id
        #     if tag_id == 0:
        #         playsound('./audio/online.mp3')
        #         print("Hello World, From April Tag ID:0!")
        #     elif tag_id == 1:
        #         print("Hello World, From April Tag ID:1!")
    if board_found == 1:
        cv.putText(image,
                            "Board Found",
                            (10, 50), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2,
                            cv.LINE_AA)
    if board_found == 0:
        cv.putText(image,
                            "",
                            (10, 50), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2,
                            cv.LINE_AA)
    cv.putText(image,
               "Elapsed Time:" + '{:.1f}'.format(elapsed_time * 1000) + "ms",
               (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2,
               cv.LINE_AA)
    # print(tag_id)
    # if tag_id == "0":
    #   print("Hello World!")
    #print(tag_ids)

    return image

#= Classes =#

#~ define and build classes here

#! Main Program !#

if __name__ == '__main__':
    main()



#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#