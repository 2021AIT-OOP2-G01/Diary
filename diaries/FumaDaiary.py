from diaries.AbstractDiary import AbstractDiary

class FumaDaiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "グループワーク頑張ります"

    def get_author(self):
        return "FumaKato"