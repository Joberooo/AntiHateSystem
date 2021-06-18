from textRecognitionFromImage.TextRecognition import TextRecognition

if __name__ == '__main__':
    file = open("tesseractPath.txt", "r")
    tesseractPath = file.read()
    print(tesseractPath)
    file.close()
    imagePathToRecognition = r'recognizedPhoto.png'

    textRecognition = TextRecognition(tesseractPath, imagePathToRecognition)
    print(TextRecognition.recognize(textRecognition))
