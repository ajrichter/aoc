def moveCrates():
  infile = "5.in"
  # f = open(file, "r")
  data = open(infile).read()
  lines = data.split('\n')
  blank = 0
  for x in range(len(lines)):
    print("clean:" + lines[x].rstrip())
    # read until char[0] != '['
    if(lines[x].rstrip() == ''):
      print("blank is: " + str(x))
      blank = x
      break
  # make dict of empty stacks until stacks for blank-2 line
  #  1   2   3
  # d= {}
  # sorted(d): [1,2,3]
  numL = len(lines[blank-1].split())
  print("stacks count: " + str(numL))
# list = []
# list.append(list_1)
  stacks = []
  for x in range(numL):
    newL = []
    stacks.append(newL)


  # class range(100, -1, -1)
  for r in reversed(range(blank-1)):
    x = 1
    line = list(lines[r])
    print("stackL: " + str(line))
    for p in range(numL):
      c = line[x].strip()
      if(c != ''):
        stacks[p].append(c)
      x+=4

  # print(stacks)
  # this should be regex for the word 'move'...
  #move 1 from 2 to 1
  #012345678901234567
  #     5     12   17
  # move = 5
  from = 12
  # to = 17 
  for l in range(blank+1, len(lines)):
    

  # parse this bs as a list
  # [Z] [M] [P]
  #0123456789012
  #  2   6  10
  #x->list->every 4th char->push()->stack
  # iterate to blank line      
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3

moveCrates()