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
    sum = 0
    pattern = r"mul\(\d+,\d+\)"
    off = r"don\'t\(\)"
    on =  r"do\(\)"
    
    data = open(file_path).read().strip()
    # split into off patterns
    off_match = re.findall(off, data)
    print(off_match)
    # add the sum of index 0 
    matches = re.findall(pattern, off_match[0])
    print(matches)
    for m in matches:
        result = m[4:-1].split(',')
        sum = sum + (int(result[0])*int(result[1]))

    for disabled in off_match[1:]:
        # find the first on
        on_match = re.findall(on, disabled)
        for enabled in on_match[1:]:
            matches = re.findall(pattern, enabled)
            for m in matches:
                result = m[4:-1].split(',')
                sum = sum + (int(result[0])*int(result[1]))

    # then split each off pattern 
    # then split after pull the first 
    print(sum)

if __name__ == "__main__":
    file_path = "day3.in"
    mulTwo(file_path)
