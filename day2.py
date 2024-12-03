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
    a = int(levels.pop(0))
    b = int(levels.peek(0))
    if ((a < b) and (a >= b-3)):
        return checkIncrease(levels)
    else:
        return False

def checkDecrease(levels):
    if(len(levels) == 1):
        return True
    a = int(levels.pop(0))
    b = int(levels.peek(0))
    if ((a > b) and (a-3 <= b)):
        return checkDecrease(levels)
    else:
        return False

def run_code(file_path):
    data = open(file_path).read().strip()
    lines = [x.strip() for x in data.split('\n')]
    sum = 0

    for line in lines:
        levels = line.split()
        if not checkEquals(levels):
            break
        if(checkIncrease(levels) or checkDecrease(levels)):
            sum+=1

    print(sum)

# Main program
if __name__ == "__main__":
    file_path = "day2.in"
    run_code(file_path)
