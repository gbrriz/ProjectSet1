import requests
import pymongo

url_list = ["https://www.lyrics.com/lyric/19058154/D.O.A.+%28Death+of+Auto-Tune%29"]

# for i in url_list:

#     song_url_current=i
#     song = requests.get(song_url_current)
#     song_soup = BeautifulSoup(song.text)
#     text = song_soup.find_all('pre',id='lyric-body-text')[0].text
#     text_clean = re.sub("\n"," ",text)
#     text_clean = re.sub("  "," ",text_clean)

client = pymongo.MongoClient("mongodb://mongodb:27017/")
db = client.songs
song1 = {'song': 'song'}
db.collections.song_coll.insert_one(song1)

#CLIENT = pymongo.MongoClient(mongodb, serverselectiontimeoutms=5000)
#song_db = CLIENT.song_db
#song_collection = song_db.song_collection
#print(song_collection)

#song1 = {"songs":song}
#song_collection.insert_one(song1)

#for i in song_db.song_collection.find({}):
#    print('we wrote new songs to db')
