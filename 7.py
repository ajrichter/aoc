def noSpace():
  infile = "7.in"
  data = open(infile).read()
  lines = data.split('\n')

  parent_dirs = {}
  dirs = {}
  current_dir = '/'

  # $ cd /
  # 012345
  for l in lines:
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
        
    elif command == 'l':



    

    #   add in files
    # map value to size
    # if $ then do x
    # if # then
# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k



noSpace()