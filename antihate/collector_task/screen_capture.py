import string
import pyscreenshot as ImageGrab


class ScreenCapture:
    def __init__(self, image_path: string):
        self.__image_path = image_path

    def grab(self):
        im = ImageGrab.grab()
        # save image file
        im.save(self.__image_path)

    def get_image_path(self):
        return self.__image_path
