# ------------------------------------------------------------------------
# StonePaperPi
# Please review ReadMe for instructions on how to build and run the program
# 
# (c) 2020 by Balaji
# MIT License
# paper
# scissor
# stone
# --------------------------------------------------------------------------
#Random is used for PC's gameplay
import random
#import Pi GPIO library button class
from picamera import PiCamera
from time import sleep

from lobe import ImageModel

#Create input, output, and camera objects
camera = PiCamera()

# Load Lobe TF model
# --> Change model file path as needed
model = ImageModel.load('/home/pi/lobe/model')

# Take Photo
def take_photo():
    # Quickly blink status light
    sleep(2)
    # Start the camera preview
    camera.start_preview()
    # wait 2s or more for light adjustment
    sleep(3) 
    # Optional image rotation for camera
    # --> Change or comment out as needed
    #camera.rotation = 270
    #Input image file path here
    # --> Change image path as needed
    camera.capture('/home/pi/Pictures/image.jpg')
    #Stop camera
    camera.stop_preview()
    sleep(1)

# Identify prediction and turn on appropriate LED
def ml_predict(label):
    if label == "paper":
        print("PAPER is detected")
        sleep(1)
    if label == "stone":
        print("STONE is detected")
        sleep(1)
    if label == "scissor":
        print("SCISSOR is detected")
        sleep(1)
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
            print(":D yoU WON :) ")
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
while True:
    temp = input("Enter any key")
    gameplay = ['paper','stone','scissor']
    computer = random.choice(gameplay)
    take_photo()
    # Run photo through Lobe TF model
    ml_result = model.predict_from_file('/home/pi/Pictures/image.jpg')
    # --> Change image path
    ml_predict(ml_result.prediction)
    # Pulse status light
    game(computer,ml_result.prediction)
    sleep(1)
