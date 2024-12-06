def runOne(file_path):
    data = open(file_path).read().strip()
    array_2d = [list(line.strip()) for line in data]


if __name__ == "__main__":
    file_path = "day4.in"
    runOne(file_path)
