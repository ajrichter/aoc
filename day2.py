def run_code(file_path):
    data = open(file_path).read().strip()
    lines = [x.strip() for x in data.split('\n')]
    sum = 0

    for line in lines:
        levels = line.split()
        isEqual = True
        isUp = True
        isDown = False

        for x in range(len(levels)-1):
            a = int(levels[x])
            b = int(levels[x+1])
            if(a == b):
                isEqual = False
                break
            if((b-a) > 3):
                isUp = False
                break
            if(a-b) > 3:
                isDown = False
                break

        if(isEqual and (isUp or isDown)):
            sum+=1

    print(sum)

# Main program
if __name__ == "__main__":
    file_path = "day2.in"
    run_code(file_path)
