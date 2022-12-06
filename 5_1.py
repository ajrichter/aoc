def moveCrates():   
  infile = "5.in"
  # f = open(file, "r")
  data = open(infile).read()
  lines = data.split('\n')

  blank = 0
  for x in range(len(lines)):
    print("clean: " + lines[x].rstrip())
    # read until char[0] != '['
    if(lines[x].rstrip() == ''):
      print("blank is: " + str(x))
      blank = x
      break
  # make dict of empty stacks until  stacks for break-1 line
  #  1   2   3 


  # iterate to until blank line
  


#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

moveCrates()