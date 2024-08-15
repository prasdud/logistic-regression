#!/usr/bin/env python3

import csv


def loadProfanityCsv(profCsv):
    with open(profCsv, mode='r') as file:
        reader = csv.reader(file)
        profaneWords = {row[0].strip().lower() for row in reader}
    return profaneWords


profanityCsv = 'profanity.csv'
profaneWords = loadProfanityCsv(profanityCsv)


def labelProfanity(lyric, profaneWords):
    lyricLower = lyric.lower()
    return 1 if any(word in lyricLower for word in profaneWords) else 0


inputCsv = 'input.csv'
labelledData = 'final_data.csv'

with open(inputCsv, mode='r') as infile, open(labelledData, mode='a', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    writer.writerow(['lyrics', 'label'])
    for row in reader:
        lyric = row[0]
        label = labelProfanity(lyric, profaneWords)
        writer.writerow([lyric, label])
