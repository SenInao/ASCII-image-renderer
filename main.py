from PIL import Image

def colorizedText(char, rgb) -> str:
    return f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m" + char + ENDC

ENDC = "\033[0m"

imagePath = input("Image name (png, jpg, jpeg): ")
imageX = 120
imageY = 80

originalImage = Image.open(imagePath).resize((imageX, imageY))
image = originalImage.convert("L")
image = image.quantize(colors=10)

asciiChars = [32, 46, 58, 45, 61, 43, 42, 35, 37, 64]
asciiChars.reverse()

asciiRender = ""
asciiRender_Colorized = ""

for y in range(imageY):
    for x in range(imageX):

        gradient = image.getpixel((x, y))
        rgb = originalImage.getpixel((x,y))

        char = chr(asciiChars[gradient]) * 2
        asciiCharColor = colorizedText(char, rgb)

        asciiRender+=char
        asciiRender_Colorized+=asciiCharColor

print(asciiRender_Colorized)
print(asciiRender)
