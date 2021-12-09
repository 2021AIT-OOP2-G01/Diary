from diaries.AbstractDiary import AbstractDiary

class NagataniDiary(AbstractDiary):

    def get_date(self):
        return"2021-12-09"

    def get_summary(self):
        return"""座りっぱなしでお尻が痛い"""
        
    def get_author(self):
        return"Shogo"
