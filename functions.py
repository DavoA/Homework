#!/usr/bin/python3
# def mystrip(mstr):
#   if type(mstr) != str:
#     print("Shuld be string")
#     return None
#   for i in range(len(mstr)):
#     if mstr[i].isalpha():
#       index1 = i
#       break
#   for i in range(len(mstr)-1,0,-1):
#     if mstr[i].isalpha():
#       index2 = i
#       break
#   return mstr[index1:index2+1]
# sentence = "    Hello  World "
# print(mystrip(sentence))

# def mytitle(mstr):
#   if type(mstr) != str:
#     print("Shuld be string")
#     return None
#   nmstr = ""
#   for i in range(len(mstr)):
#     if mstr[i] == mstr[0] or mstr[i-1] == " ":
#       nmstr+=mstr[i].upper()
#     else:
#       nmstr+=mstr[i]
#   return nmstr
# sentence = "hello  world"
# print(mytitle(sentence))

# def myupper(mstr):
#   if type(mstr) != str:
#     print("Shuld be string")
#     return None
#   nmstr = ""
#   for i in mstr:
#     if i.isalpha():
#       if ord(i) >= 97 and ord(i)<=122:
#         nmstr+=chr(ord(i)-32)
#       else:
#         nmstr+=i
#     else:
#       nmstr+=i
#   return nmstr
# sentence = "hello world"
# print(myupper(sentence))

# def myreplace(mstr,ol,nl,cnt):
#   if type(mstr) != str:
#     print("Shuld be string")
#     return None
#   nmstr = ""
#   for i in mstr:
#     if cnt!=0 and i==ol:
#       nmstr+=nl
#       cnt-=1
#     else:
#       nmstr+=i
#   return nmstr
# sentence = "hello world"
# cnt = 2
# nletter = "k"
# oletter = "l"
# print(myreplace(sentence,oletter,nletter,cnt))

# def myfind(mstr,obj):
#   if type(mstr) != str:
#     print("Shuld be string")
#     return None
#   for i in range(len(mstr)):
#     if mstr[i] == object:
#       return i
#   return -1
# sentence = "hello world"
# object = "k"
# print(myfind(sentence,object))

# def myswap(mstr):
#   if type(mstr) != str:
#     print("Shuld be string")
#     return None
#   nmstr = ""
#   for i in mstr:
#     if i.isalpha():
#       if ord(i) >= 97 and ord(i)<=122:
#         nmstr+=chr(ord(i)-32)
#       elif ord(i) >= 65 and ord(i)<=90:
#         nmstr+=chr(ord(i)+32)
#     else:
#       nmstr+=i
#   return nmstr
# sentence = "heLLo wOrlD"
# print(myswap(sentence))

# def mycapitalize(mstr):
#   if type(mstr) != str:
#     print("Shuld be string")
#     return None
#   nmstr = ""
#   for i in range(len(mstr)):
#     if mstr[i].isalpha():
#       if mstr[i].isupper():
#         return mstr
#       nmstr+=chr(ord(mstr[i])-32)
#       nmstr+=mstr[i+1:len(mstr)]
#       break
#     else:
#       nmstr+=mstr[i]
#   return nmstr
# sentence = "hello world"
# print(mycapitalize(sentence))

# def mycount(mstr,obj):
#   if type(mstr) != str:
#     print("Shuld be string")
#     return None
#   cnt=0
#   for i in mstr:
#     if i == letter:
#       cnt+=1
#   return cnt
# sentence = "hello world"
# letter = "o"
# print(mycount(sentence,letter))

# def myindex(mstr,obj):
#   if type(mstr) != str:
#     print("Shuld be string")
#     return None
#   for i in range(len(mstr)):
#     if mstr[i] == object:
#       return i
#   return None
# sentence = "hello world"
# object = "l"
# print(myindex(sentence,object))

def mylower(mstr):
  if type(mstr) != str:
    print("Shuld be string")
    return None
  nmstr = ""
  for i in mstr:
    if i.isalpha():
      if ord(i) >= 65 and ord(i)<=90:
        nmstr+=chr(ord(i)+32)
      else:
        nmstr+=i
    else:
      nmstr+=i
  return nmstr
sentence = "HELLO WORLD"
print(mylower(sentence))
