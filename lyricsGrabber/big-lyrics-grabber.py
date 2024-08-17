import re
import string
import lyricsgenius
from pycontractions import Contractions
from gensim import models
import csv

#w=models.KeyedVectors.load_word2vec_format('archive.npy', binary=True)

genius=lyricsgenius.Genius("MpY2-SgiN1WZygcE3lXZiRZFnyTcWG8zQBVSyLZGVYnX9Hc607mreDQlvYXoQfDt")
input_filename = 'temp.csv'
output_filename = 'output.csv'


#genius=Genius()

#artist=genius.search_artist("Eminem", max_songs=1, sort="title", include_features=True)

cont = Contractions('GoogleNews-vectors-negative300.bin')


def getLyrics(artistName, songName):
    song = genius.search_song(songName,artistName)
    output1=list(cont.expand_texts([song.lyrics]))
    outputTemp=[]
    for lyrics in output1:
        lines = lyrics.split('\n')
        for line in lines:
            #line.translate(None, string.punctuation)
            cleanedLine = line.translate(str.maketrans('','',string.punctuation))
            outputTemp.append([cleanedLine])

    return outputTemp






#artistName="eminem"
#song=genius.search_song("lucifer",artistName)

#print(song.lyrics)
#cont = Contractions('GoogleNews-vectors-negative300.bin')
#cont = Contractions(api_key="glove-twitter-100")
#cont = Contractions(w)
#print("working")

#print(song.lyrics)
#output1=list(cont.expand_texts([song.lyrics]))
#outputTemp=[]
#for i in output1:
#    outputTemp.append([i])
#cleanOut=re.sub('\W+',' ',outputTemp) #removes whitespaces

#for lyrics in output1:
#    lines = lyrics.split('\n')
#    for line in lines:
#        outputTemp.append([line])


#print(outputTemp) #printing this gets pretty verse output

with open(input_filename, mode='r') as infile, open(output_filename, mode='a', newline='') as outfile:
    writer = csv.writer(outfile)
    reader = csv.reader(infile)
    for songs in reader:
        songName = songs[0]
        artistName = songs[1]
        writer.writerows(getLyrics(artistName, songName))
        #writer.writerows(outputTemp)



print("done")
