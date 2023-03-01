# Derek Bergman
# sort.py -- builds on filter.py, sorts list alphabetically
import sys

names = list()
for line in sys.stdin:
  names.append(line.strip())
  names.sort()

for name in names:
  print(name)
