def moveCrates():
  infile = "5.in"
  # f = open(file, "r")
  data = open(infile).read()
  lines = data.split('\n')
  blank = 0
  for x in range(len(lines)):
    # print("clean:" + lines[x].rstrip())
    # read until char[0] != '['
    if(lines[x].rstrip() == ''):
      # print("blank is: " + str(x))
      blank = x
      break
  # make dict of empty stacks until stacks for blank-2 line
  #  1   2   3
  # d= {}
  # sorted(d): [1,2,3]
  numL = len(lines[blank-1].split())
  # print("stacks count: " + str(numL))
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

  print()
  print("stack::")
  print(stacks)
  # this should be regex for the word 'move'...
  #move 1 from 2 to 1
  #012345678901234567
  #     5     12   17
  # move = 5
  # from = 12
  # to = 17 
  for l in range(blank+1, len(lines)):
    #move 1 from 2 to 1
    # 0   1   2  3  4 5
    print(lines[l])
    spl = lines[l].split()
    for s in spl:
      print("split: " + s)
    cnt = int(spl[1])
    frm = int(spl[3])
    to =  int(spl[5])
    print("cnt: " + str(cnt))
    print("frm: " + str(to))
    print("to: " + str(to))

    for i in range(cnt):
      print()
      temp = stacks[frm-1].pop()
      stacks[to-1].append(temp)


  print("new stacks::")
  print(stacks)
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