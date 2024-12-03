def checkEquals(lines):
    for x in range(len(lines)-1):
        if(lines[x] == lines[x+1]):
            return False
    return True

def checkIncrease(lines):
    for x in range(len(lines)-1):
        if(lines[x] < lines[x]) and lines[x]+3 <= lines[x]:
            return True
    return False

def checkDecrease(lines):
    for x in range(len(lines)-1):
        if(lines[x] > lines[x]) and lines[x] >= lines[x]+3:
            return True            
    return False

def read_file(file_path):
    data = open(file_path).read().strip()
    lines = [x.strip() for x in data.split('\n')]
    sum = 0

    for line in lines:
        levels = line.split()
        if (checkEquals(levels) and (checkIncrease(levels) or checkDecrease(levels))):
            sum+=1

    print(sum)
    print(2)

# Main program
if __name__ == "__main__":
    file_path = "day2.in"
    read_file(file_path)
