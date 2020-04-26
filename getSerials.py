import string

txtList = open('caa-rechecking-incident-affected-serials.txt', 'r')
outFile = open('serials.txt', 'w')

serial = False
currTxt = txtList.readline()
nameList = []
currName = ""
i = 0
while(currTxt):
    i += 1
    outFile.write(currTxt[48:112])
    if i % 100000 == 0:
        print(i)
    currTxt = txtList.readline()


txtList.close()
outFile.close()