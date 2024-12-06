import re

def multiply(file_path):
    pattern = r"mul\(\d,\d\)"
    sum = 0

    data = open(file_path).read().strip()    
    print(data)

    matches = re.findall(pattern, data)
    for m in matches:
        result = m[4:-1].split(',')
        sum = sum + (result[0]*result[1])

    print(sum)

if __name__ == "__main__":
    file_path = "day3.in"
    multiply(file_path)
