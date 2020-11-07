import sys

file = open(sys.argv[1], 'r')
Lines = file.readlines()

for i in range(0,len(Lines)):
    Lines[i] = Lines[i].replace("\n","")

print(Lines)