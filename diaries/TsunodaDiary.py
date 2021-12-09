from diaries.AbstractDiary import AbstractDiary

class TsunodaDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "オブジェクト演習でチーム開発の準備した"

    def get_author(self):
        return "Tsunoda"