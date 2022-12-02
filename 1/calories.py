def getLargestElf():
  in_file = "1.in"
  print("opening file: " + in_file)
  f = open(in_file, "r")  
  max = 0
  currCal = 0
  all_elves = []

  for l in f:
    if l == '\n':
      print("I am carrying " + str(currCal) + " calories!")
      all_elves.append(currCal)
      # if currCal > max:
      #   max = currCal
      currCal = 0
    else:
      print("Added " + l + " calories!")
      currCal += int(l)

  all_elves.sort(reverse=True)
  print("top 3 elves are: " + str(all_elves[0:3]))
  print("sum is: " + str(sum(all_elves[0:3])))


getLargestElf()