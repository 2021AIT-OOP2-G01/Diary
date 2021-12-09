from diaries.DiarySample import DiarySample
from diaries.ShogoDiary import ShogoDiary
from diaries.AoyamaiDiary import AoyamaiDiary
from diaries.GotoDiary import GotoDiary
from diaries.YamamotoDiary import YamamotoDiary
from diaries.TsunodaDiary import TsunodaDiary
from diaries.AihataDiary import AihataDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
  DiarySample(),
  ShogoDiary(),
  AoyamaiDiary(),
  GotoDiary(),
  YamamotoDiary(),
  k20077_diary
  TsunodaDiary(),
  AihataDiary(),
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()