import cv2 as cv
import numpy as np
from time import time
import pyautogui as pg
import windowcapture




loop_time = time()
while(True):

    screenshot1 = windowcapture.screenshot
    
    cv.imshow('Computer Vision', screenshot1)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('...')