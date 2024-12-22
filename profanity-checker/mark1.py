#!/usr/bin/env python3

import joblib
import lyricsgenius
import csv
from pycontractions import Contractions
import time
import os.path

# Load models
print("Loading model", end="", flush=True)
try:
    model = joblib.load('model.pkl')
    print(f"\rModel ", model, " loaded succesfully")
except Exception as e:
    print(f"\rError loading model")
    print(f"{e}")
    exit()

print("\rLoading vectorizer", end="", flush=True)
try:
    vectorizer = joblib.load('count_vectorizer.pkl')
    print(f"\rVectorizer ", vectorizer, " loaded succesfully")
except Exception as e:
    print(f"\rError loading vectorizer")
    print(f"{e}")
    exit()

genius= lyricsgenius.Genius("MpY2-SgiN1WZygcE3lXZiRZFnyTcWG8zQBVSyLZGVYnX9Hc607mreDQlvYXoQfDt")
#genius= lyricsgenius.Genius("Fx-gUjjxNsRvjfOIGBpeVhrBsKjNG5LQmWiEXYNyAo3od7HrSUZM8DM_68u0KPA3IwdtMO6HGOHmzpR6vQzkaw")
print("\rLoading contractions.bin", end="", flush=True)
#cont = Contractions('../GoogleNews-vectors-negative300.bin')
if(os.path.exists("../GoogleNews-vectors-negative300.bin")):
    cont = Contractions('../GoogleNews-vectors-negative300.bin')
    print(f"\rContractions file loaded succesfully")
else:
    print(f"\rContractions file does not exist")
    exit()

lyricsFile = 'lyrics.csv'
profanityFile = 'predictedProfanityFile.csv'

                                                                                                                                  
#lyrics = "im a boss you know"
print("\rEnter the name of the artist")
artistName = input()
print("Enter the name of the song")
songName = input()
song = genius.search_song(songName ,artistName)
#print(song)
if(song == None):
    print(f"The song could not be found, try again with the correct song name")
    exit()
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

print(f'\nThe number of bars in the song are {lyricCount}')
print(f'The number of profane lyrics in this song are {labelOne}')
print(f'The given song has a profanity rating of {profanityPercent}%')


