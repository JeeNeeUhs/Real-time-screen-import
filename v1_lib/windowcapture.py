import cv2 as cv
import numpy as np
import pyautogui as pg


def screenshot():
    while(True):

        screenshot1 = pg.screenshot()
        screenshot1 = np.array(screenshot1)
        screenshot1 = cv.cvtColor(screenshot1, cv.COLOR_RGB2BGR)