import requests

def searchRucksack():
  file = "3.in"
  f = open(file, "r")

  # NJvhJcQWTJWTNTFFMTqqGqfTmB
  totalPriority = 0
  while(1==1):
    l1 = sorted(f.readline())
    if(l1 is ''):
        break
    l2 = sorted(f.readline())
    l3 = sorted(f.readline())

    match1 = ''
    for x in l1:
      for y in l2:
        if(x is y):
          match1 += x
    
    match2 = ''
    for m1 in match1:
      for y in l2:
        if(x is y):
          match1 += x

          
          print(x)
    totalPriority += ord(letter)-38
    # print(ord(letter)-38)
    if(letter.islower()):
      # print("lower: " + str(ord(letter)-96))
      totalPriority-=58
    
    # add ord() -96 to the total
    # add the ord of the letter to total
  print("total: " + str(totalPriority))

# print(ord('a')-64-32)
searchRucksack()
