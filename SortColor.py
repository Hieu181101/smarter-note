import PIL.Image
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload



def CheckColor(image):
    img = PIL.Image.open(image)
    w,h = img.size

    check = img.load()

    isBlue = [range(60,90),range(110,140),range(110,140)]
    isRed = [range(180,230), range(70,115), range(30,70)]
    isGreen = [range(130,170),range(140,180), range(60,85)]
    isYellow = [range(200,235), range(180,210), range(95,120)]
    isPink = [range(210,240), range(150,180), range(110,130)]

    for y in range(image.height):
        for x in range(image.width):
            if check[x,y] in isBlue:
                return "Blue"
            elif check[x,y] in isRed:
                return "Red"
            elif check[x,y] in isGreen:
                return "Green"
            elif check[x,y] in isYellow:
                return "Yellow"
            elif check[x,y] in isPink:
                return "Pink"
            else:
                return "No color found"

    return "No color found"

def UploadToDrive(image):
    






