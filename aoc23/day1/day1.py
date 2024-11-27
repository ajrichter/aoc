def solve_one():
	f = open("a.in", "r")
	Lines = f.readlines()
	sum = 0
	# f = open("demofile.txt", "r")
	# for x in f:
  	# print(x)

	for line in Lines:
		# find forward number
		line = strip(line)
		print(line)
		print("before " + str(sum))
		for c in line:
			if(c.isdigit()):
				sum += int(c)
				break

		# last num
		for c in reversed(line):
			if(c.isdigit()):
				sum += int(c)
				break

		print("after " + str(sum))
	

	return sum


print(solve_one())