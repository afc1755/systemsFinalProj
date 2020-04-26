import string

txtList = open('caa-rechecking-incident-affected-serials.txt', 'r')
outFile = open('urls.txt', 'w')

names = False
currTxt = txtList.readline()
nameList = []
currName = ""
i = 0
while(currTxt):
    i += 1
    for charNum in range(0, len(currTxt)):
        if currTxt[charNum] == '[':
            names = True
        elif currTxt[charNum] == ']':
            names = False
        elif names:
            if not currTxt[charNum] in string.whitespace:
                currName += currTxt[charNum]
            else:
                nameList.append(currName)
                currName = ""
    if i % 10000 == 0:
        print(i)
    currTxt = txtList.readline()

for name in nameList:
    outFile.write(name + '\n')


txtList.close()