import string

import pytesseract
from antihate.collector_task.screen_capture import ScreenCapture


class TextRecognition:
    def __init__(self, tesseract_path: string, screen_capture: ScreenCapture):
        self.__screen_capture = screen_capture
        pytesseract.pytesseract.tesseract_cmd = tesseract_path

    def recognize(self):
        self.__screen_capture.grab()
        return pytesseract.image_to_string(self.__screen_capture.get_image_path()).split("\n")
