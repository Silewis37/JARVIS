import cv2
import apriltag
import numpy as np

# Load the image
image = cv2.imread('image.jpg') 

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define the AprilTags detector options and detect the AprilTags
print("[INFO] detecting AprilTags...")
options = apriltag.DetectorOptions(families="tag36h11")
detector = apriltag.Detector(options)
results = detector.detect(gray)
print("[INFO] {} total AprilTags detected".format(len(results)))

# Calculate the distance between the two AprilTag points
if len(results) >= 2:
    # Get the centers of the two AprilTags
    center1 = results[0].center
    center2 = results[1].center

    # Calculate the distance in pixels
    distance_pixels = np.linalg.norm(np.array(center1) - np.array(center2))

    # Convert the distance from pixels to inches (assuming a known pixel-to-inch ratio)
    pixel_to_inch_ratio = 0.01  # adjust this value based on your camera setup
    distance_inches = distance_pixels * pixel_to_inch_ratio

    print("Distance between AprilTag points: {:.2f} inches".format(distance_inches))
else:
    print("Not enough AprilTags detected")