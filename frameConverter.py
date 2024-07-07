from PIL import Image

def colorizedText(char, rgb) -> str:
    return f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m" + char + ENDC

def modifyFrame(frame: Image.Image) -> Image.Image:
    frame = frame.convert("L")
    frame = frame.quantize(colors=LIGHTLEVELS)
    return frame
    

def convertFrame(frame: Image.Image, shouldHaveColour: bool) -> str:
    frame = frame.resize((IMAGEX, IMAGEY))
    modifiedFrame = modifyFrame(frame)
    renderedAscii = ""

    for y in range(IMAGEY):
        for x in range(IMAGEX):
    
            gradient = modifiedFrame.getpixel((x, y))
            char = chr(asciiChars[gradient]) * 2

            if (shouldHaveColour):
                rgb = frame.getpixel((x,y))
                char = colorizedText(char, rgb)

            renderedAscii += char
    
    return renderedAscii

asciiChars = [64, 37, 35, 42, 43, 61, 45, 58, 46, 32]
ENDC = "\033[0m"
IMAGEX = 120
IMAGEY = 80
LIGHTLEVELS = 10

