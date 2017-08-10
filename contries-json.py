#!/usr/bin/python
import json

print "Start convert name2.txt to json"
fo = open("names2.txt", "r+")
fw = open("names.json", "w+")

boys = []
girls = []

for line in fo:
    n1 = line.find("	")
    line2 = line[n1 + 1:]
    n2 = line2.find("	")
    name1 = line2[0: n2]
    name2 = line2[n2 + 1: len(line2) - 1]
    girls.append(name1)
    boys.append(name2)

data = {}
data["boys"] = boys
data["girls"] = girls
fw.write(json.dumps(data))

fo.close()
fw.close()
print "Finish convert name2.txt to json"
print "Check file names.json"
