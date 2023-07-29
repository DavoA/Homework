#!/usr/bin/python3
def mystrip(mstr):
  if type(mstr) != str:
    print("Shuld be string")
    return None
  for i in range(len(mstr)):
    if mstr[i].isalpha():
      index1 = i
      break
  for i in range(len(mstr)-1,0,-1):
    if mstr[i].isalpha():
      index2 = i
      break
  return mstr[index1:index2+1]
sentence = "    Hello  World "
print(mystrip(sentence))
