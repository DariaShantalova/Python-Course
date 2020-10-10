#In this assignment you will read through and parse a file with text and numbers. 
#You will extract all the numbers in the file and compute the sum of the numbers.

import re
sum = 0
fh = open("regex_sum_942426.txt")
for line in fh:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) != 0 :
        for number in x :
            sum = sum + int(number)


print(sum)
