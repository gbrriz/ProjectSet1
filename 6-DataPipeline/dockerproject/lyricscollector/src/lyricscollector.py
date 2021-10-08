import requests
import pymongo

url_list = ["https://www.lyrics.com/lyric/19058154/D.O.A.+%28Death+of+Auto-Tune%29"]

song = """La da da da da da
Hey hey hey goodbye (good riddens)
Hold up
Only rappers to re-write history without a pen
No I-D on the track let the story begin, begin, begin
This is anti auto-tune, death of the ring-tone,
This ain't for iTunes, this ain't for sing alongs
This is Sinatra at the opera, bring a blonde
Preferably with a fat ass who can sing a song
Wrong, this ain't politically correct (arh!)
This might offend my political connects (arh!)
My raps don't have melodies
This shit make niggas wan' go and commit felonies
Get your chain tooken
I may do it myself, I'm so Brooklyn
I know we facing a recession
But the music y'all making going make it the great depression (arh!)
Or your lack aggression
Put your skirt back down, grow a set man
Nigga this shit violent
This is death of auto-tune, moment of silence
La da da da da da
Hey hey goodbye
Hold up
Only rappers to re-write history without a pen
No I-D on the track let the story begin, begin, begin
Hold up,
This ain't a number one record (arh!)
This is practically assault with a deadly weapon (arh!)
I made it just for Flex and
Mister Cee, I want niggas to feel threatened (arh!)
Stop your bloodclot crying
The kid, the dog, everybody dying, no lying
You niggas jeans too tight
You colors too bright, your voice too light (arh!) (arh!)
(It's too far nigga)
I might wear black for a year straight
I might bring back Versace shades
This ain't for z100
Ye told me to kill y'all to keep it one hundred
This is for Hot 9-7
This shit's for Clue, for Khaled, for we the best in
Nigga this shit violent
This is death of auto-tune, moment of silence
La da da da da da
Hey hey hey goodbye
Hold up
Only rappers to re-write history without a pen
No I-D on the track let the story begin, begin, begin
Hold up,
This shit need a verse from Jeezy
I might send this to the mix-tape Weezy
Get somebody from B-M-F to talk on this
Get this to a blood, let a crip walk on it (arh!)
Fifty thou' to style on this
I just don't need nobody to smile on this (arh!)
Y'all niggas singing too much
Get back to rap you t-paining too much (arh!) (arh!)
I'm a multi-millionaire
So how is it I'm still the hardest here (arh!)
I don't be in the project hallway
Talking about how I be in the project all day (arh!)
That sound stupid to me
If you a gangsta this is how you prove it to me (arh!) (arh!)
Nigga just get violent
This is death of auto-tune moment of silence
La da da da da da
Hey hey hey goodbye
Hold up"""

# for i in url_list:

#     song_url_current=i
#     song = requests.get(song_url_current)
#     song_soup = BeautifulSoup(song.text)
#     text = song_soup.find_all('pre',id='lyric-body-text')[0].text
#     text_clean = re.sub("\n"," ",text)
#     text_clean = re.sub("  "," ",text_clean)

CLIENT = pymongo.MongoClient(mongodb, serverselectiontimeoutms=5000)
song_db = CLIENT.song_db
song_collection = song_db.song_collection
print(song_collection)

song1 = {"songs":song}
song_collection.insert_one(song1)

for i in song_db.song_collection.find({}):
    print('we wrote new songs to db')
