def noSpace():
  infile = "7.in"
  data = open(infile).read()
  lines = data.split('\n')

  parent_dirs = {}
  dirs = {}
  current_dir = '/'

  # $ cd /
  # 012345
  for i in sizeof(lines):
    l = lines[i]
    command = l[0]
    if command == '$':
      newCmd = str(l[2:4])
      print("found cmd: " + newCmd)

      if newCmd == 'cd':
        newDir = str(l[5:])
        if newDir == '..':
          parent = parent_dirs[current_dir]
          current_dir = parent
        else:
          parent_dirs[newDir] = current_dir
          current_dir = newDir
      elif newCmd == 'ls':
        # iterate through dirs until next $
        temp = i+1
        l_temp = lines[temp]
        while()
        if 

    elif command == 'd':



    

    #   add in files
    # map value to size
    # if $ then do x
    # if # then



noSpace()