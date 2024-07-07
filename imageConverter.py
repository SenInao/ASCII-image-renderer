from PIL import Image
from frameConverter import convertFrame
import os

path = input("path to image: ")

if (not os.path.isfile(path)):
    print("file not found!")
    os._exit(0)

shouldHaveColour = input("render with colour? Y/N: ").lower()

if (shouldHaveColour == "y"):
    shouldHaveColour = True
else:
    shouldHaveColour = False

image = Image.open(path)

convertedFrame = convertFrame(image, shouldHaveColour)

print(convertedFrame)
