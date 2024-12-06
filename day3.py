def multiply(file_path):
    data = open(file_path).read().strip()
    lines = [line.strip() for line in data]


if __name__ == "__main__":
    file_path = "day3.in"
    multiply(file_path)
