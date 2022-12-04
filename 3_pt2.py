def searchRucksack():
  file = "3.in"
  f = open(file, "r")

  # NJvhJcQWTJWTNTFFMTqqGqfTmB
  totalPriority = 0
  
  l1 = f.readline()
  counter = 0
  while(l1 != ''):
    print("og: " + l1)
    l1 = sorted(l1)
    print(l1)

    l2 = sorted(f.readline())
    l3 = sorted(f.readline())

    mset = set()
    for x in l1:
      for y in l2:
        if(x == y and x != '\n'):
          mset.add(x)
          print("x: " + x + " y: " + y)
          break
    
    match2 = ''
    for m1 in mset:
      for m2 in l3:
        if(m1 == m2):
          match2+=m1
          print("3rd pair: " + m1)
          break

    totalPriority = 0
    for a in match2:
      # print("new letter: " + a)
      totalPriority += ord(a)-38
      if(a.islower()):
        totalPriority-=58    
    # add ord() -96 to the total
    # add the ord of the letter to total
    print("secondM " + match2)
    # get line 1 again
    l1 = f.readline()


  print("Sum of Ls: " + str(totalPriority))


# print(ord('a')-64-32)
searchRucksack()
