#!/usr/bin/env python3

import csv
import re

def loadProfanityCsv(profCsv):
    with open(profCsv, mode='r') as file:
        reader = csv.reader(file)
        profaneWords = {row[0].strip().lower() for row in reader}
    return profaneWords


profanityCsv = '../data/profanity-unique-main.csv'
profaneWords = loadProfanityCsv(profanityCsv)


def labelProfanity(lyric, profaneWords):
    lyricLower = lyric.lower()
    #return 1 if any(word in lyricLower for word in profaneWords) else 0
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in profaneWords) + r')\b'
    return 1 if re.search(pattern, lyricLower) else 0

inputCsv = '../data/final-data-unlabelled.csv'
labelledData = '../data/final-data-labelled.csv'

with open(inputCsv, mode='r') as infile, open(labelledData, mode='a', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    writer.writerow(['lyrics', 'label'])
    for row in reader:
        lyric = row[0]
        label = labelProfanity(lyric, profaneWords)
        writer.writerow([lyric, label])
