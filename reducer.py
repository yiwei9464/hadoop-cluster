#!/usr/bin/python
import sys

totalCount = 0
oldWord = None

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue
    newWord, newCount = data

    if oldWord and oldWord != newWord:
        sys.stdout.write("{0}\t{1}\n".format(oldWord, totalCount))

        totalCount = 0

    oldWord = newWord
    totalCount += int(newCount)

if oldWord != None:
    sys.stdout.write("{0}\t{1}\n".format(oldWord, totalCount))