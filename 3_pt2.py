def searchRucksack():
  file = "3.in"
  f = open(file, "r")

  # NJvhJcQWTJWTNTFFMTqqGqfTmB
  totalPriority = 0
  while(1==1):
    l1 = ''
    l1 = sorted(f.readline())
    if(l1 == ''):
        break
    l2 = sorted(f.readline())
    l3 = sorted(f.readline())

    match1 = ''
    for x in l1:
      for y in l2:
        if(x is y):
          match1 += x
          print(x)
    
    match2 = ''
    for m1 in match1:
      for m2 in l2:
        if(m1 is m2):
          match2+=m1
          print(m1)

    totalPriority = 0
    for a in match2:
      print("new letter: " + a)
      totalPriority += ord(a)-38
      if(a.islower()):
        totalPriority-=58    
    # add ord() -96 to the total
    # add the ord of the letter to total
    print(match2)

  print("Sum of Ls: " + str(totalPriority))


# print(ord('a')-64-32)
searchRucksack()
