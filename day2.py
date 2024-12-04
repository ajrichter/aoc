def checkEquals(levels):
    for x in range(len(levels)-1):
        a = int(levels[x])
        b = int(levels[x+1])
        if(a == b):
            return False
    return True

def checkIncrease(levels):
    if(len(levels) == 1):
        return True
    a = int(levels[0])
    b = int(levels[1])
    if ((a < b) and (a >= b-3)):
        return checkIncrease(levels[1:])
    else:
        return False

def checkDecrease(levels):
    if(len(levels) == 1):
        return True
    a = int(levels[0])
    b = int(levels[1])
    if ((a > b) and (a-3 <= b)):
        return checkDecrease(levels[1:])
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
                current = checkLevel(nums.remove(x))
                if current == 1:
                    sum += 1
                    break

    print(sum)

# Main program
if __name__ == "__main__":
    # file_path = "day2.in"
    file_path = "easy2.in"
    # run_code(file_path)
    runPtTwo(file_path)
