from textRecognitionFromImage.TextRecognition import TextRecognition

if __name__ == '__main__':
    file = open("tesseractPath.txt", "r")
    tesseractPath = file.read()
    file.close()
    imagePathToRecognition = r'recognizedPhoto.png'

    textRecognition = TextRecognition(tesseractPath, imagePathToRecognition)
    list = TextRecognition.recognize(textRecognition)
    for element in list:
        print(element)
