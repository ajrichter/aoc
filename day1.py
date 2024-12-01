def read_file(file_path):
    try:
        with open(file_path, 'r') as file:  # Open the file in read mode
            for line in file:  # Read each line in the file
                line = line.strip()  # Remove leading/trailing whitespace
                print(f"Line: {line}")  # Process or print the line
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")

# Main program
if __name__ == "__main__":
    file_path = "day1.in"  # Replace with your file path
    read_file(file_path)
