f = open('ReadInputFile.txt.txt', 'r')
#print(f.read())
#f.close()
count=0
for line in f:
    line_split=line.split()
    if line_split[2] == 'P':
        print(line)
    #print(str(count)+ line)
    #count=count+1
f.close()

