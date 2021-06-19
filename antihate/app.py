from time import sleep

from antihate.analysis_task.analysis_task import AnalysisTask
from antihate.analysis_task.email_sender import EmailSender
from antihate.collector_task.collector_task import CollectorTask
from antihate.collector_task.hate_analyzer import HateAnalyzer
from antihate.collector_task.screen_capture import ScreenCapture
from antihate.collector_task.text_recognition import TextRecognition
from antihate.settings.settings import get_parm


class App:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            cls._instance.__init_val()
            # Put any initialization here.
        return cls._instance

    def __init_val(self):
        self.__analysis_task = AnalysisTask(
            email_sender=EmailSender(
                system_email=get_parm("server_email"),
                system_pass=get_parm("server_pass"),
                user_mail=get_parm("user_email")
            ),
            hate_sum_limit=get_parm("limit_hate_sum"),
            hate_ratio_limit=get_parm("limit_hate_ratio"),
            interval=get_parm("analysis_interval"),
            path_to_raw_data=get_parm("csv_file_name"),
            path_to_stats_file=get_parm("stats_file")
        )
        self.__collector_task = CollectorTask(
            hate_analyzer=HateAnalyzer(
                max_list_size=get_parm("list_len"),
                text_recognition=TextRecognition(
                    screen_capture=ScreenCapture(
                        image_path=get_parm("picture_path")
                    ),
                    tesseract_path="C:/Program Files/Tesseract-OCR/tesseract",
                )
            ),
            interval=get_parm("collect_interval"),
            path_to_raw_data=get_parm("csv_file_name")
        )

    def start(self):
        print("Start antiHate app...")
        self.__analysis_task.start()
        self.__collector_task.start()

    def stop(self):
        print("Stop antiHate app.")
        self.__analysis_task.stop()
        self.__collector_task.stop()

    def reset(self):
        self.stop()
        self.__init_val()
        self.start()


if __name__ == "__main__":
    app = App.instance()
    app.start()
    sleep(200)
    app.stop()
