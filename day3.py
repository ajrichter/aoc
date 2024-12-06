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

def mul(str):
    sum1 = 0


    return sum1

def mulTwo(file_path):
    sum = 0
    pattern = r"mul\(\d+,\d+\)"
    off = r"don't\(\)"
    on =  r"do\(\)"

    data = open(file_path).read().strip()
    # split into off patterns
    off_match = re.findall(off, data)
    # add the sum of index 0 
    matches = re.findall(pattern, off_match[0])
    for m in matches:
        result = m[4:-1].split(',')
        sum = sum + (int(result[0])*int(result[1]))

    for offs in off_match[1:]:
        # find the first on
 
    # then split each off pattern 
    # then split after pull the first 

    matches = re.findall(pattern, data)
    for m in matches:
        result = m[4:-1].split(',')
        print(result)
        sum = sum + (int(result[0])*int(result[1]))

    print(sum)


if __name__ == "__main__":
    file_path = "day3.in"
    multiply(file_path)
    mulTwo(file_path)
