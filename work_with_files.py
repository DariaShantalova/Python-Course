count = 0
average = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else : 
      dot = line.find('.')
      average = average + float(line[dot:]) 
      count = count + 1
print("Average spam confidence:", average / count)
