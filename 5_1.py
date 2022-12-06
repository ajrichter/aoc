def starSearch():   
  infile = "5.in"
  # f = open(file, "r")
  data = open(infile).read()
  lines = data.split('\n]')

  for l in lines:
    print("clean: " + l.rstrip())
    # read until char[0] != '['



starSearch()