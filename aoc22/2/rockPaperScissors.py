def playRps():
  in_file = "2.in"
  print("opening file: " + in_file)
  f = open(in_file, "r")

  score = 0
  for l in f:
    you = ord(l[0].lower()) -96
    me = ord(l[2].lower()) -96-23
    # print("you: " + l[0] + " uNum: " +str(you))
    # print("me: " + l[2] + " mNum " +str(me))

        # 1= L, 2=D, 3=W
    # part2 logic
    # lose
    if(me == 1):
      if(you == 1): score+=3
      elif(you == 2): score+=1
      else: score+=2
    # draw+3
    elif(me == 2): 
      score+=you
      score+=3
    # win+6
    else:
      if(you == 1): score+=8
      elif(you == 2): score+=9
      else: score+=7
      
# 1 > 3 && 2 > 1
# 2 > 1 && 3 > 2
# 3 > 2

    # part1 logic 
    # score += me
    # if(me == you):
    #   score += 3
    # elif((me==1 and you==3) or (me==2 and you==1) or (me==3 and you==2)):
    #   score += 6
  print("EndScore is: "  + str(score))

# ord('a')-96 for xyz-23
# 1 > 3
# 2 > 1
# 3 > 2
# r 1 a x ord(x) -24
# p 2 b y
# s 3 c z
# l0 -d3 -w6

import requests


playRps()
# print(ord('z')-96-23)
# print("2:: " + str(ord('y')-96-23))

# URL = "https://adventofcode.com/2022/day/2/input"
# response = requests.get(URL)
# f = open(response, "r")
# print("new: " + f.readline())