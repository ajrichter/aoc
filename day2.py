def checkEquals(equalList):
    for x in range(len(equalList)-1):
        a = int(equalList[x])
        b = int(equalList[x+1])
        if(a == b):
            return False
    return True

def checkIncrease(upList):
    if(len(upList) == 1):
        return True
    a = int(upList[0])
    b = int(upList[1])
    if ((a < b) and (a >= b-3)):
        return checkIncrease(upList[1:])
    else:
        return False

def checkDecrease(downList):
    if(len(downList) == 1):
        return True
    a = int(downList[0])
    b = int(downList[1])
    if ((a > b) and (a-3 <= b)):
        return checkDecrease(downList[1:])
    else:
        return False

# def run_code(file_path):
#     data = open(file_path).read().strip()
#     lines = [x.strip() for x in data.split('\n')]
#     sum = 0

#     for line in lines:
#         levels = line.split()
#         if checkEquals(levels):
#             increase = checkIncrease(levels)
#             decrease = checkDecrease(levels)
#             if increase:
#                 sum+=1
#             elif decrease:
#                 sum+=1
#     print(sum)

def checkLevel(path_one):
    sum = 0
    if checkEquals(path_one):
        increase = checkIncrease(path_one)
        decrease = checkDecrease(path_one)
        if increase:
            sum+=1
        elif decrease:
            sum+=1
    return sum

def runPtTwo(file_path):
    data = open(file_path).read().strip()
    lines = [x.strip() for x in data.split('\n')]
    sum = 0

    for line in lines:
        nums = line.split()
        current = checkLevel(nums)
        if current == 0:
            for x in nums:
                newList = nums
                newList.remove(x)
                current = checkLevel(newList)
                if current == 1:
                    sum += 1
                    break
        else:
            sum+=1

    print(sum)

if __name__ == "__main__":
    file_path = "day2.in"
    # file_path = "easy2.in"
    # run_code(file_path)
    runPtTwo(file_path)
