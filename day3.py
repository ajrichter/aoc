import re

def multiply(file_path):
    pattern = r"mul\(\d,\d\)"
    sum = 0

    data = open(file_path).read().strip()
    lines = [line.strip() for line in data]    
    for line in lines:
        matches = re.findall(pattern, line)
        for m in matches:
            print(m)
            temp = m[4:-1]
            result = temp.split(',')
            sum = sum + (result[0]*result[1])

    print(sum)

if __name__ == "__main__":
    file_path = "day3.in"
    multiply(file_path)
