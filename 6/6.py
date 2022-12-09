def mc():   
    infile = "6.in"
    # f = open(file, "r")
    data = open(infile).read()
    # str.split(sep=None, maxsplit=-1)
    # print(data)
    print(len(data))
    arr = list(data)

    index = len(arr)
    for x in range(13, len(arr)):
        set = {arr[x-13]}
        for y in range(x-12, x+1):
            add = arr[y]
            if(add in set):
                break
            set.add(add)
        
        if(len(set) == 14):
            print("found index: " + str(x+1))
            break

        del(set)

# part 1
        # set = {arr[x-3], arr[x-2], arr[x-1], arr[x]}
        # if(len(set) == 4):
        #     print("4th: " + str(x))
        #     print(set)
        #     index = x+1
        #     break

    print(index)


mc()