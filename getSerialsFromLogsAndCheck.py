import csv
import os

serials = []
vulnerableSerials = {}

serF = open('serials.txt', 'r')
currNext = serF.readline()
serials = currNext.split()

i = 0
for file in os.listdir('argon'):
    data = csv.reader(open('argon/' + file, 'r'), delimiter=",")
    for row in data:
        currS = row[2]
        if row[2] in serials:
            i += 1
            vulnerableSerials[row[2]] = row[4]
    if i % 10000 == 0:
        print(i)

vulnerableFile = open('vulnerableSerials.txt', 'w')
for key in vulnerableSerials:
    vulnerableFile.write(key)
    vulnerableFile.write(',')
    vulnerableFile.write(vulnerableSerials[key])

vulnerableFile.close()
serF.close()