import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot
from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

customers = db["customers"]

count_event = customers.find({"ref" : "events"}).count()
count_wow = customers.find({"ref" : "wom"}).count()
count_ads = customers.find({"ref" : "ads"}).count()

labels = ["events" , "wow" , "ads"]
values = [count_event , count_wow , count_ads]
explode = [0 , 0 , 0]

pyplot.pie(values , labels = labels , explode = explode , shadow = True)
pyplot.axis("equal")

pyplot.show()