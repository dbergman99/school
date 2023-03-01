# Derek Bergman
# filter.py -- take in CSV and print each value on its own line with no whitespace
import sys

for line in sys.stdin:
  line = ''.join(line.split()) # remove all whitespace
  names = line.split(',') # seperate bases on ','

for name in names:
  if name: # if name not '' (empty)
    print(name)
