def getID():   
  file = "4.in"
  f = open(file, "r")

#   2-4,6-8
  inside = 0
  for l in f:
    x = l.split(",")
    a = x[0].split("-")
    b = x[1].split("-")
    b[1] = b[1].rstrip()

    contains = False
    if(int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1])):
      inside+=1
      print(str(a) + " > " + str(b))
    elif(int(a[0]) >= int(b[0]) and int(a[1]) <= int(b[1])):
      inside+=1
      print(str(a) + " < " + str(b))
      

  print(inside)
    
getID()