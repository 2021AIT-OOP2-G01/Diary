from diaries.DiarySample import DiarySample
from diaries.NagataniDiary import NagataniDiary
from diaries.AihataDiary import AihataDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
  DiarySample(),
  NagataniDiary(),
  AihataDiary(),
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()