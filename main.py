from diaries.DiarySample import DiarySample
from diaries.FumaDaiary import FumaDaiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
  DiarySample(),
  FumaDaiary()
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()