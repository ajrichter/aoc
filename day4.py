def runOne(file_path):
    data = open(file_path).read().strip()
    lines = [x.strip() for x in data.split('\n')]
    # convert all lines to a [][] array
    # do graph search for XMAS
    # add visited to check nearby?
    xArray = [][]
    for line in lines:
        
        for x in line:




if __name__ == "__main__":
    file_path = "day4.in"
    runOne(file_path)
