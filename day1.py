def read_file(file_path):
    list1 = []
    list2 = []

    try:
        with open(file_path, 'r') as file:  # Open the file in read mode
            for line in file:  # Read each line in the file
                line = line.strip()  # Remove leading/trailing whitespace
                words = line.split()
                if words[0].isdigit():
                    list1.append(int(words[0]))
                if words[1].isdigit():
                    list2.append(int(words[1]))
                else:
                    print(f"Skipping non-numeric line: {line}")
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")

    sum = 0
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        sum = sum + abs(list1[i] - list2[i])

    print(sum)

    # Part two
    similar = 0
    for i in range(len(list1)):
        count = 0
        for j in range(len(list2)):
            if list1[i] == 

# Main program
if __name__ == "__main__":
    file_path = "day1.in"
    # file_path = "easy1.txt"
    read_file(file_path)
