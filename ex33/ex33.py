numbers = []

def count_and_fill(start, limit):
  while start < limit:
    print "At the top start is %d" % start
    numbers.append(start)

    start = start + 3
    print "Numbers now: ", numbers
    print "At the bottom start is %d" % start

count_and_fill(0, 6)

print "The numbers: "

for num in numbers:
  print num