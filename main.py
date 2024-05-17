import PIL.Image
import SortColor

def main():
    
    path = input("Enter the path of the image: ")
    try:
        image = PIL.Image.open(path)
        image.close()  
    except Exception as e:
        print("Invalid path:", e)
        return  

    # Call the MoveImage function with the image path (string)
    SortColor.MoveImage(path)

if __name__ == "__main__":
    main()
