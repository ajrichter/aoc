def getID():   
  file = "4.in"
  f = open(file, "r")

#   2-4,6-8
  inside = 0
  for l in f:
    x = l.split(",")
    a = x[0].split("-")
    b = x[1].split("-")

    contains = False
    if(a[0] <= b[0] and a[1] >= b[1]):
      inside+=1
      print("a: " + a)
      print("b: " + b)
    elif(a[0] >= b[0] and a[1] <= b[1]):
      inside+=1
      print("a: " + a)
      print("b: " + b)
    

  print(inside)
    
getID()