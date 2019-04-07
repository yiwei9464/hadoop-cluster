#!/usr/bin/python
import sys
import re

wordList = ["environment", "future", "green", "health", "innovation", "recycle", "safety", "scholarship", "sports", "technology"]

for line in sys.stdin:
    if line.strip() != '':
        data = line.strip().split()
        for d in data:
            word = re.sub(r"[^a-zA-Z-]", "", d)
            for w in wordList:
                if (word != "" and word == w):
                    word = word.lower()
                    sys.stdout.write("{0}\t{1}\n".format(word, 1))
