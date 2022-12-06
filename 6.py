def mc():   
    infile = "6.in"
    # f = open(file, "r")
    data = open(infile).read()
    # str.split(sep=None, maxsplit=-1)
    print(data)
    print(len(data))
    arr = list(data)

    index = len(arr)
    for x in range(3, len(arr)):
        set = {arr[x-3], arr[x-2], arr[x-1], arr[x]}
        if(len(set) == 4):
            print("4th: " + str(x))
            print(set)
            index = x
            break
        del(set)

    print(index)


mc()