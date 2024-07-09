from PIL import Image
from imageToAscii import convertFrame
import cv2
import os
import sys

path = input("path to video: ")

if (not os.path.isfile(path)):
    print("file not found")
    os._exit(0)

shouldHaveColour = input("render with colour? Y/N: ").lower()

if (shouldHaveColour == "y"):
    shouldHaveColour = True
else:
    shouldHaveColour = False

cam = cv2.VideoCapture(path)

convertedFrames = []
while(True):
    ret,frame = cam.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        frame = convertFrame(image, shouldHaveColour)

        sys.stdout.write("\x1b[H")
        print(frame)
    else:
        break

    cv2.waitKey(60)

cam.release()
cv2.destroyAllWindows()
