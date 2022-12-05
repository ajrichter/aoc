# notes on Python

`int(var)` turns a string to number

`str(v)` turns an int to a string

# Read in lines, stripped

```
data = open(infile).read().strip()
lines = [x.strip() for x in data.split('\n')]
```

