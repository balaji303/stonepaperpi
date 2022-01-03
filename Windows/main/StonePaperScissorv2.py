# ------------------------------------------------------------------------
# StonePaperPi
# Please review ReadMe for instructions on how to build and run the program
# 
# (c) 2022 by Balaji
# MIT License
# paper
# scissor
# stone
# pip install lobe
# pip3 install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime
# --------------------------------------------------------------------------
#Random is used for PC's gameplay
import random
import time
from lobe import ImageModel
import cv2
import os

# Load Lobe TF model
# --> Change model file path as needed
currentDir = os.path.dirname(__file__)
print(currentDir)
os.chdir(currentDir)
modelPath = currentDir+"\\..\\lobe\\model"
model = ImageModel.load(modelPath)

# Take Photo
def take_photo():
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        return 0
    cv2.imshow("StonePaperPi", frame)
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        cam.release()
        cv2.destroyAllWindows()
        return 0
    elif k%256 == 32:
        # SPACE pressed
        img_name = "StonePapaerPiv2.png"
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
    return 1

# Identify prediction and turn on appropriate LED
def ml_predict(label):
    if label == "paper":
        print("PAPER is detected")
        # sleep(1)
    elif label == "stone":
        print("STONE is detected")
        # sleep(1)
    elif label == "scissor":
        print("SCISSOR is detected")
        # sleep(1)
    else:
        print("Not Known")


def game(pc,human):
    print("Human:")
    print(human)
    print("PC: ")
    print(pc)
    if human == "paper":
        if pc == "paper":
            print("draw")
        elif pc == "stone":
            print(":D *** yoU WON *** :) ")
        elif pc == "scissor":
            print("You Lost :( ")
        else:
            print("Try Again!")
    elif human == "stone":
        if pc == "paper":
            print("You Lost :( ")
        elif pc == "stone":
            print("draw")
        elif pc == "scissor":
            print(":D *** yoU WON *** :) ")
        else:
            print("Try Again!")
    elif human == "scissor":
        if pc == "paper":
            print(":D *** yoU WON *** :) ")
        elif pc == "stone":
            print("You Lost :( ")
        elif pc == "scissor":
            print("draw")
        else:
            print("Try Again!")
    else:
        print("Enter again")
# Main Function
cam = cv2.VideoCapture(0)
cv2.namedWindow("StonePaperPiv2")
while True:
    gameplay = ['paper','stone','scissor']
    computer = random.choice(gameplay)
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("StonePaperPiv2", frame)

    KeyboardInput = cv2.waitKey(1)
    if KeyboardInput%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        cv2.destroyAllWindows()
        cam.release()
        break
    elif KeyboardInput%256 == 32:
        # SPACE pressed
        img_name = "StonePapaerPiv2.png"
        cv2.imwrite(img_name, frame)
        print("{} Saved!".format(img_name))
        # Run photo through Lobe TF model
        ml_result = model.predict_from_file('C:\\Users\\Balaji\\Documents\\GitHub\\stonepaperpi\\Windows\\main\\StonePapaerPiv2.png')
        # --> Change image path
        ml_predict(ml_result.prediction)
        # Pulse status light
        game(computer,ml_result.prediction)
        time.sleep(1)
