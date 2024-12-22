# logistic-regression
uses logistic regression algorithms to check whether a song contains profanity

requires bin file for contractions, file too big to put on github, 
https://drive.google.com/file/d/1NSPClpuNIZQegvp1M5EEUUUzvAKNMBVp/view?usp=sharing
<h1>USAGE</h1> <br>
<ul>
<li>You need to source the activation file found in code/genius/bin/activate</li>
`source code/genius/bin/activate`
<li>The script to run is profanity-checker/mark1.py</li>
`python3 mark1.py`
<li>You also need a contractions bin file to run this. Can be found in the google drive link provided. Place the file in the root folder</li>
</ul>

<h1>TODO</h1> <br>
<ul>
  <li>i count about 245 lyrics or "bars" for 2 songs so about 122.5 bars per song. Assuming a robust model, i would need 50000 per class. so i have 2 classes, 1 = profane, 0 = not profane. so all in all 100,000 bars. if my math is right need about 816 songs. i will train it on 1000 songs just to be safe</li>
    <li> set up a script that automates the labelling process for 1000 songs.</li>
      <li>1000 songs seems too much to handle but eminem himself has about 11 albumns in his discography. assuming an average of 15 songs per album, 1 artist gives me upwards of 150 songs. so i just need 10 artists, maybe</li>
      <h3>august 19</h3>
      <li>now i have the final data to be trained, approximately 230000 song lyrics to be trained</li>
      <li>will manuallly clean the data again</li>
      <li>next thing to do is retrofit my labeller software to utilize workers and read from my final.csv</li>
      <li>will also work on a main software where user enters name of artist and song</li>
      <li>also need to come up with some sort of ranking system or formula to put the profanity of a song into a numeric value or a letter grade. have not decided yet</li>

  <h3>august 21</h3>
  <li>turns out i did not need to utilize workers, the training itself was pretty quick, used scikit-learn</li> 
  <li>obtained the final model. 99 percent accuracy throughout, for both 0 and 1</li>
  <li>need to create main software</li>
  <li>need to come up with a formula to rank, will think it over</li>
  <li>more importantly need to name it. will probably be the hardest thing about this project</li>

  <h3>august 24</h3>
  <li>I ended up just calling it mark1</li>
  <li>It "works". At the end of the day it is just a basic implementation of logistic regression to classify lyrics based on a 2000 row profanity file</li>
  <li>It does not properly detect the sentiment behind the lyrics, for example during testing the song 'im back' by eminem, the software gave me a profanity percentage of 15 percent. That song deserves way more, but since it follows a bag of words approach as opposed to sentimental analysis, this is the best i can do right now</li>
  <li>need to clean the lyrics before i pass it to the model, for ex. need to remove duplicate lyrics</li>
  <li>This project is far from over. Will definitely work on it in the future, will add sentimental analysis</li>
  <li>This was supposed to be a 2 hour project for my AI class. LOL</li>
</ul>

