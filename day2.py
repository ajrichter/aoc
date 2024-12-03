def checkEquals(lines):
    for x in range(len(lines)-1):
        if(lines[x] == lines[x+1]):
            return False
        
    return True

def checkIncrease(lines):
    for x in range(len(lines)-1):
        if(lines[x] < lines[x]):
            return False
    return True
    
def read_file(file_path):
    data = open(file_path).read().strip()
    lines = [x.strip() for x in data.split('\n')]
    sum = 0

    for line in lines:
        levels = line.split()
        if (checkEquals(levels) and checkIncrease(levels) and checkDecrease(levels)):
            sum+=1             

    print(sum)


# Main program
if __name__ == "__main__":
    file_path = "day2.in"
    # file_path = "easy1.txt"
    read_file(file_path)
