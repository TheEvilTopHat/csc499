import fileinput
names = {}
sorted = []
#sort by length
for line in fileinput.input():
    line = line.replace(' ','')
    if str(len(line)) not in names.keys():
        names[str(len(line))] = []
    names[str(len(line))].append(line) 
#max name size 100
#sort by alph
for i in range(100):
    i = str(i)
    if i in names.keys():
        arr = names[i]
        arr.sort()
        for j in arr:
            sorted.append(j)
#store in file called sorted
with open("sorted.txt",'w') as file: # Use file to refer to the file object
   file.writelines(sorted)
