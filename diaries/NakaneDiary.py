from diaries.AbstractDiary import AbstractDiary

class NakaneDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "お昼ご飯を食べ損ねた、オブジェクトちょっと遅れた、かなしい"

    def get_author(self):
        return "Nakane"