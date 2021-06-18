import string
import pyscreenshot as ImageGrab
class ScreenCapture:
    def grab(self,path_with_png:string):
        im = ImageGrab.grab()
        # save image file
        im.save(path_with_png)
