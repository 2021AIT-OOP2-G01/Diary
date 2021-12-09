from diaries.DiarySample import DiarySample
from diaries.NakaneDiary import NakaneDiary
from diaries.FumaDaiary import FumaDaiary
from diaries.AoyamaiDiary import AoyamaiDiary
from diaries.GotoDiary import GotoDiary
from diaries.YamamotoDiary import YamamotoDiary
from diaries.TsunodaDiary import TsunodaDiary
from diaries.AihataDiary import AihataDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
  DiarySample(),
  FumaDaiary(),
  AoyamaiDiary(),
  GotoDiary(),
  YamamotoDiary(),
  TsunodaDiary(),
  AihataDiary(),
  ] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()