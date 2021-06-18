from textRecognitionFromImage.TextRecognition import TextRecognition
from hatesonar import Sonar


class HateAnalyzer:
    def __init__(self):
        file = open("../textRecognitionFromImage/tesseractPath.txt", "r")
        tesseract_path = file.read()
        file.close()

        self.text_rec = TextRecognition(tesseract_path)

        self.sonar = Sonar()

    def get_stats(self):
        output_dicts = []
        text_rows = self.text_rec.recognize()
        for row in text_rows:
            row_data = self.sonar.ping(row)
            output_data = {}
            for analyze_class in row_data['classes']:
                output_data[analyze_class['class_name']] = \
                    analyze_class['confidence']
            output_dicts.append(output_data)

        return output_dicts



