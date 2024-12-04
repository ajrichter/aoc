def runOne(file_path):
    data = open(file_path).read().strip()
    # convert all lines to a [][] array
    array_2d = [list(line.strip()) for line in data]
    # do graph search for XMAS
    # add visited to check nearby?

    
    

if __name__ == "__main__":
    file_path = "day4.in"
    runOne(file_path)
