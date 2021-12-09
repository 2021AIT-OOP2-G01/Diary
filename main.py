from diaries.DiarySample import DiarySample
from diaries.NakaneDiary import NakaneDiary
from diaries.YamamotoDiary import YamamotoDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
  DiarySample(),
  YamamotoDiary(),
  NakaneDiary(),
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()