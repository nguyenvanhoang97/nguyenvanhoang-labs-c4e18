from pymongo import MongoClient

mongo_uri = "mongodb://admin:Hn18071997@ds151840.mlab.com:51840/c4e18-lab"

#1. Content to database
client = MongoClient(mongo_uri)

#2. Get database
db = client.get_default_database()

#3. Create collection
games = db["games"]

#4. Create document
# new_game = {
#     "titel" : "FAF",
#     "description" : "Fast"
# }

#5. Insert document intro collection
# film.insert_one(new_game)

all_game = games.find()

for game in all_game:
    print(game)