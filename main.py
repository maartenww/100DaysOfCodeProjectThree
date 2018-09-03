import pyautogui
import time
import keyboard
from PIL import Image
from PIL import ImageGrab
import cv2 as cv
import numpy as np

running = True
def main():
    # Press Space to start the program
    GameStart = True
    hasNotStarted = False
    while GameStart:
        if keyboard.is_pressed('space'):
            hasNotStarted = True
            GameStart = False
            print('Program has started')
    while hasNotStarted:
        # Gameloop
        while running:
            game1.handle_Events()
            game1.gameState()
            #game1.capScreen()
            #game1.compareTemplate()
            game1.restartGame()
class Game:
    dinoLife = None
    def __init__(self):
        pass

    #Todo: this OpenCV (Optimzie it)
    # Compares template to image
    def compareTemplate(self):
        #cv.imshow("frame",self.capScreen())
        #cv.waitKey()

        #img_gray = cv.imread('frame.png')

        # Grayscale image of the template, 0 stands for load in grayscale
        template = cv.imread('Cactus2.png', 0)

        #w, h = template.shape[::-1]

        # Screenshots a RGB image
        img1 = ImageGrab.grab(bbox=(212,539,1919,715))
        # Makes the RGB image to an array
        img1_np = np.array(img1)

        # Matches templates
        result = cv.matchTemplate(self.capScreen(), template,cv.TM_CCOEFF_NORMED)
        # Threshold
        threshold = 0.29
        # If match is greater than threshold, show location?
        loc = np.where(result >= threshold)

        # Draw a red rect around the match(es)
        for pt in zip(*loc[::-1]):
            cv.rectangle(img1_np, pt, (pt[0] + 100, pt[1] + 150), (0, 0, 255), 2)

        # Shows an image of the detected matches (Optional)
        cv.imshow('Detected', img1_np)
        cv.waitKey()

    # Screenshots the path of the dino each frame and converts it
    # To a numpy array and then to a grayscale image
    def capScreen(self):
        img1 = ImageGrab.grab(bbox=(212,539,1919,715))
        img1_np = np.array(img1)
        frame = cv.cvtColor(img1_np, cv.COLOR_BGRA2GRAY)
        #frame1 = cv.imwrite('frame.png', frame)
        return frame

    # Checks the dinosaurs eye to see if he's alive or not
    def gameState(self):
        if pyautogui.pixelMatchesColor(158,589,(255,255,255)):
            self.dinoLife = True
            print('alive')
        elif pyautogui.pixelMatchesColor(158,589,(83,83,83)):
            self.dinoLife = False
            print('dead')

    # Makes the cursor click the restart button if the dinosaur is dead
    def restartGame(self):
        if self.dinoLife == False:
            #time.sleep(1)
            pyautogui.click(960,564)
            print('Restarted')

    # Quits the program as soon as the player holds esc
    def handle_Events(self):
        if keyboard.is_pressed('esc'):
            quit()

game1 = Game()

class Player:
    dinoCordX = 213
    dinoCordY = 574
    dinoCordAbs = (dinoCordX, dinoCordY)

    def __init__(self):
        dinoCordX = self.dinoCordX
        dinoCordY = self.dinoCordY
        dinoCordAbs = self.dinoCordAbs

if __name__ == "__main__":
    main()



