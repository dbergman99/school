# Derek Bergman
# uniq.py -- takes a sorted list and removes duplicate entries
import sys

names = list()
for line in sys.stdin:
  names.append(line.strip()) # build list without whitespace 

for i in range(len(names)):
  if names[i] !=  names[i-1]: # if cur != prev, then print
    print(names[i])

