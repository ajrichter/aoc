import requests

def searchRucksack():
  file = "3.in"
  f = open(file, "r")

  # NJvhJcQWTJWTNTFFMTqqGqfTmB
  totalPriority = 0
  for l in f:
    length = int(len(l)/2)
    comp1 = sorted(l[:length])
    comp2 = sorted(l[length:])
    found = False
    letter = ''
    for x in comp1:
      for y in comp2:
        if(x is y):
          letter = x
          print(letter)
          found = True
          break
      if(found):
        break
    totalPriority += ord(letter)-38
    # print(ord(letter)-38)
    if(letter.islower()):
      # print("lower: " + str(ord(letter)-96))
      totalPriority-=58
    
    # add ord() -96 to the total
    # add the ord of the letter to total
  print("total: " + str(totalPriority))

# print(ord('a')-64-32)

print(ord('A')-38)
print(ord('L')-64)
print(ord('P')-64)
searchRucksack()
