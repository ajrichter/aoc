import re

def multiply(file_path):
    pattern = r"mul\(\d+,\d+\)"
    sum = 0
    data = open(file_path).read().strip()    
    matches = re.findall(pattern, data)
    for m in matches:
        result = m[4:-1].split(',')
        print(result)
        sum = sum + (int(result[0])*int(result[1]))
    print(sum)

def mulTwo(file_path):
    pattern = r"mul\(\d+,\d+\)"
    off_patterm = r"don't\(\)"
    on =  r"do\(\)"

    sum = 0
    data = open(file_path).read().strip()    
    matches = re.findall(pattern, data)
    for m in matches:
        result = m[4:-1].split(',')
        print(result)
        sum = sum + (int(result[0])*int(result[1]))



if __name__ == "__main__":
    file_path = "day3.in"
    multiply(file_path)
    mulTwo(file_path)
