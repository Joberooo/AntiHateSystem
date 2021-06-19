from textRecognitionFromImage.TextRecognition import TextRecognition
from settings.settings import get_parm

from hatesonar import Sonar
import re


class HateAnalyzer:
    def __init__(self):
        file = open("../textRecognitionFromImage/tesseractPath.txt", "r")
        tesseract_path = file.read()
        file.close()

        self.text_rec = TextRecognition(tesseract_path)

        self.sonar = Sonar()

        self.dictionary = []

    def _check_dict(self, string):
        MAX_LEN = get_parm('list_len')
        ret_value = False
        if string in self.dictionary:
            self.dictionary.remove(string)
            self.dictionary = [string] + self.dictionary
            ret_value = True
        else:
            self.dictionary = [string] + self.dictionary

        if len(self.dictionary) > MAX_LEN:
            self.dictionary.pop(MAX_LEN)

        return ret_value

    def get_stats(self):
        output_dicts = []
        text_rows = self.text_rec.recognize()
        for row in text_rows:
            is_not_whitespace = re.search("\S\S\S", row)
            if is_not_whitespace and not self._check_dict(row):
                row_data = self.sonar.ping(row)
                output_data = {}
                for analyze_class in row_data['classes']:
                    output_data[analyze_class['class_name']] = \
                        analyze_class['confidence']
                output_data['text'] = row_data['text']
                output_dicts.append(output_data)

        return output_dicts



