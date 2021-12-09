from diaries.AbstractDiary import AbstractDiary

class YamamotoDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "眠い"

    def get_author(self):
        return "Yamamoto"