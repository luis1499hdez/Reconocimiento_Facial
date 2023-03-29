import cv2 as cv
from cv_operations import take_photo
from ui_interface import invok_ui

if '__main__' == __name__:
    callback = invok_ui(lambda name: take_photo(name))
    print(callback)