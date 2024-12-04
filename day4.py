def runPtTwo(file_path):
    data = open(file_path).read().strip()
    lines = [x.strip() for x in data.split('\n')]
    sum = 0

    for line in lines:
        nums = line.split()
        current = checkLevel(nums)
        if current == 0:
            for x in range(len(nums)):
                new_list = list(nums[:x] + nums[x+1:])
                current = checkLevel(new_list)
                if current == 1:
                    print(new_list)
                    sum += 1
                    break
        else:
            sum+=1

    print(sum)

if __name__ == "__main__":
    file_path = "day2.in"
    # file_path = "easy2.in"
    # run_code(file_path)
    runPtTwo(file_path)
