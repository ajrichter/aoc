# notes on Python

`int(var)` turns a string to number

`str(v)` turns an int to a string

# Read in lines, stripped

```
data = open(infile).read().strip()
lines = [x.strip() for x in data.split('\n')]
```

# Day 7
- brute force doesn't seem like a good idea but can code a naive solution to start
- since the total input is small 

# regex
re.findalll(pattern, data)
