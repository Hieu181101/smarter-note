import PIL.Image
import shutil
import os

def resize_image(image, new_width=100):
    width, height = image.size
    new_height = int(new_width * (height / width))
    resized_image = image.resize((new_width, new_height))
    return resized_image

def CheckColor(image_path):
    img = PIL.Image.open(image_path)
    
    # Convert image to RGB if it's not already in that mode
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    img = resize_image(img, 100)
    w, h = img.size
    check = img.load()

    # Define color ranges( change the color range here to make it more accurate or sensitive to which shade you using)
    isBlue = [range(50, 130), range(50, 180), range(150, 255)]
    isRed = [range(180, 255), range(0, 100), range(0, 100)]
    isGreen = [range(0, 100), range(180, 255), range(0, 100)]
    isYellow = [range(200, 255), range(200, 255), range(0, 100)]
    isPink = [range(200, 255), range(150, 200), range(150, 200)]

    # Check each pixel's color and print it for debugging
    for y in range(h):
        for x in range(w):
            r, g, b = check[x, y]
            if r in isBlue[0] and g in isBlue[1] and b in isBlue[2]:
                return "Blue"
                break
            elif r in isRed[0] and g in isRed[1] and b in isRed[2]:
                return "Red"
                break
            elif r in isGreen[0] and g in isGreen[1] and b in isGreen[2]:
                return "Green"
                break
            elif r in isYellow[0] and g in isYellow[1] and b in isYellow[2]:
                return "Yellow"
                break
            elif r in isPink[0] and g in isPink[1] and b in isPink[2]:
                return "Pink"
                break
            else:
                pass

    return "No color found"

def MoveImage(image_path):
    color = CheckColor(image_path)
    base_path = "C:/Hieu/OneDrive/Documents/smarter-note"
    if color != "No color found":
        dest_path = os.path.join(base_path, color)
        shutil.move(image_path, dest_path)
        print(f"Moved {image_path} to {dest_path}")
    else:
        print(f"No color found in {image_path}")


