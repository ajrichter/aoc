def run(file_path):
    data = open(file_path).read().strip()
    lines = [x.strip() for x in data.split('\n')]
    # read all rules into a dictionary
    rules = {}

    for line in lines:
        if line == '':
            break
        rule = line.split("|")
        if rule[0] in rules:
            rules.get(rule[0]).add(rule[1])
        else:
            rules[rule[0]] = set([rule[1]])
        
    # if line is in o
    # if line is correct, add middle page
    # 143 - middle pages of 3
        
if __name__ == "__main__":
    file_path = "day5.in"
    run(file_path)
