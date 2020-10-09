#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dct = dict()

for line in handle:
    if not line.startswith('From ') :
        continue
    else : 
        line = line.split()
        dct[line[1]] = dct.get(line[1], 0) + 1
        
max_value = None
key_of_max = None

for key in dct.keys():
    if max_value is None :
        max_value = dct[key]
        key_of_max = key
    elif dct[key] > max_value :
         max_value = dct[key]
         key_of_max = key   
        
print(key_of_max, dct[key_of_max]) 
