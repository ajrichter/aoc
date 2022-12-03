import requests

def searchRucksack():
  file = "3.in"
  f = open(file, "r")

  # NJvhJcQWTJWTNTFFMTqqGqfTmB
  totalPriority = 0
  for l in f:
    l = l.strip()
    print(l)
    print(len(l))
    length = int(len(l)/2)
    print(length)
    
    comp1 = sorted(l[:length])
    comp2 = sorted(l[length:])
    found = false
    letter = '?'
    for x in comp1:
      for y in comp2:
        if(x is y):
          letter = '?'
          print(letter)
          print(ord(letter)-96)
          found = true
          break
      if(found):
        break
    totalPriority += ord(letter)-96
    
    # add ord() -96 to the total
    # add the ord of the letter to total
  print("total: " + str(totalPriority))

searchRucksack()
# print(ord('p')-96)