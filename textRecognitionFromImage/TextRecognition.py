import pytesseract
from capture_screen.capturer import ScreenCapture


class TextRecognition:
    def __init__(self, tesseractPath, imagePathToRecognition):
        self.tesseractPath = tesseractPath
        self.imagePathToRecognition = imagePathToRecognition


    def recognize(self):
        ScreenCapture().grab(self.imagePathToRecognition)
        pytesseract.pytesseract.tesseract_cmd = self.tesseractPath
        textFromImage = []
        textFromImage.append(pytesseract.image_to_string(self.imagePathToRecognition).split("\n"))
        return textFromImage
