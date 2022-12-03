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
    letter = '?'
    for x in comp1:
      for y in comp2:
        if(x is y):
          letter = x
          print(letter)
          print(ord(letter)-96)
          found = True
          break
      if(found):
        break
    totalPriority += ord(letter)-96
    
    # add ord() -96 to the total
    # add the ord of the letter to total
  print("total: " + str(totalPriority))

print(ord('p')-96)
print(ord('A')-96)
searchRucksack()
# print(ord('p')-96)