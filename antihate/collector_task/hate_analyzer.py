from hatesonar import Sonar
import re


class HateAnalyzer:
    def __init__(self, text_recognition, max_list_size):
        self.__text_rec = text_recognition
        self.__max_list_size = max_list_size
        self.__sonar = Sonar()
        self.__dictionary = []

    def _check_dict(self, string):
        ret_value = False
        if string in self.__dictionary:
            self.__dictionary.remove(string)
            self.__dictionary = [string] + self.__dictionary
            ret_value = True
        else:
            self.__dictionary = [string] + self.__dictionary

        if len(self.__dictionary) > self.__max_list_size:
            self.__dictionary.pop(self.__max_list_size)

        return ret_value

    def get_stats(self):
        output_dicts = []
        text_rows = self.__text_rec.recognize()
        for row in text_rows:
            is_not_whitespace = re.search("\S\S\S", row)
            if is_not_whitespace and not self._check_dict(row):
                row_data = self.__sonar.ping(row)
                output_data = {}
                for analyze_class in row_data['classes']:
                    output_data[analyze_class['class_name']] = \
                        analyze_class['confidence']
                output_data['text'] = row_data['text']
                output_dicts.append(output_data)

        return output_dicts
