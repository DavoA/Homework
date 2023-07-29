#!/usr/bin/python3
import random
def quest_option(arr):
  quest = []
  opp = []
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if arr[i][j] == "?":
        quest.append(arr[i][0:j+1])
        opp.append(arr[i][j+1:len(arr[i])].split())
  return quest,opp

def myanswer(arr1,arr2):
  cnt = 0
  for i in range(len(arr1)):
    print(arr1[i])
    opt2 = arr2[i].copy()
    for j in range(4):
      opt = random.sample(arr2[i],1)
      print(*opt)
      arr2[i].remove(*opt)
    answer = input("Enter a option: ")
    if answer == opt2[0]:
      cnt+=1
      print("Correct")
    else:
      print("Incorrect")
  print("You have", cnt, "correct answers")
  return cnt

all = ["What is the capital of France?Paris Erevan Madrid Tokyo",
       "What is the capital of Armenia?Erevan Artik Madison Moscow",
       "What is the capital of Russia?Moscow Washington Madrid Clinton",
       "What is the capital of Italy?Rome Erevan Madison Artik",
       "What is the capital of Norway?Oslo Bergen Madrid Milan",
       "What is the capital of the US?Washington Phoenix Orlando Denver",
       "What is the capital of the UK?London Cambridge Rome Bergen",
       "What is the capital of Iran?Tehran Kashan Moscow Denver",
       "What is the capital of Kazakhstan?Astana Phoenix Artik Tokyo",
       "What is the capital of Canada?Ottawa London Madrid Madison",
       "What is the capital of Sweden?Stockholm Ottawa Milan Washington",
       "What is the capital of Switzerland?Bern Artik Oslo Kashan",
       "What is the capital of Ukraine?Kyiv Cambridge London Tokyo",
       "What is the capital of Belgium?Brussels Erevan Madrid Tokyo"]
game = random.sample(all,10)
questions,options = quest_option(game)
cnt = myanswer(questions,options)
