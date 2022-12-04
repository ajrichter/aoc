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
    if(a[0] <= b[0] and a[1] >= b[1]):
      inside+=1
      print("a: " + str(a))
      print("b: " + str(b))
    elif(a[0] >= b[0] and a[1] <= b[1]):
      inside+=1
      print("a: " + str(a))
      print("b: " + str(b))
    

  print(inside)
    
getID()