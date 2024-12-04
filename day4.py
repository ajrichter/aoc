def findM(array_2d, row, col, letters):
    letter = letters.get(0)


def runOne(file_path):
    data = open(file_path).read().strip()
    # convert all lines to a [][] array
    array_2d = [list(line.strip()) for line in data]
    # do graph search for XMAS
    # add visited to check nearby?
    for row in array_2d:
        for col in row:
            if array_2d[row][col] == 'X':
                # check the rest
                findLetter(array_2d, row, col, 'MAS')


if __name__ == "__main__":
    file_path = "day4.in"
    runOne(file_path)
