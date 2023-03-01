# Derek Bergman
# pig_latin.py -- takes sorted unique list of names, output names converted to pig latin
import sys

names = list()
for line in sys.stdin:
  names.append(line.strip()) # build list without whitespace 

for name in names:
  name = name.lower() # conver name to lower case
  for i in range(len(name)):
    ch = name[i]
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'): 
      break # if ch is vowel, then we found "split" point so break
  if(i == 0): # if first char is vowel
    print(f'{name:s}-yay')
  else: # all other cases
    print(f'{name[i:]:s}-{name[:i]:s}ay')
