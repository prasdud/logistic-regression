#!/usr/bin/env python3

import joblib
import lyricsgenius
import csv
from pycontractions import Contractions


# Load models
model = joblib.load('model.pkl')
vectorizer = joblib.load('count_vectorizer.pkl')
genius= lyricsgenius.Genius("MpY2-SgiN1WZygcE3lXZiRZFnyTcWG8zQBVSyLZGVYnX9Hc607mreDQlvYXoQfDt")
cont = Contractions('../GoogleNews-vectors-negative300.bin')
lyricsFile = 'lyrics.csv'
profanityFile = 'predictedProfanityFile.csv'

#lyrics = "im a boss you know"
print("enter the name of the artist")
artistName = input()
print("enter the name of the song")
songName = input()
song = genius.search_song(songName ,artistName)

songExpanded = list(cont.expand_texts([song.lyrics]))
Song = []

for lyrics in songExpanded:
    lines = lyrics.split('\n')
    for line in lines:
        Song.append([line])

with open(lyricsFile, mode = 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(Song)




with open(lyricsFile, mode = 'r', newline='') as infile, open(profanityFile, mode = 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    writer.writerow(['Lyrics', 'Profanity Label'])
    for row in reader:
        lyric = row[0]
        lyric_vec = vectorizer.transform([lyric])
        prediction = model.predict(lyric_vec)
        writer.writerow([lyric, prediction])


lyricCount = 0
labelOne = 0
labelZero = 0
profanityPercent = 0

with open(profanityFile, mode='r', newline='') as infile:
    reader = csv.reader(infile)
    for row in reader:
        label = row[1]
        lyricCount += 1
        if label == '[0]':
            labelZero += 1
        elif label == '[1]':
            labelOne += 1
        else:
            continue

profanityPercent = round((labelOne/lyricCount) * 100, 2)

print(f'The total no. of bars in the song are {lyricCount}')
print(f'The no. of bad lyrics in this song are {labelOne}')
print(f'The given song has a profanity rating of {profanityPercent}%')


