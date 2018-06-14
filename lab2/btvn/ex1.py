from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL
import pyexcel
# 1
url = "https://www.apple.com/itunes/charts/songs"
#
conn = urlopen(url)
# 
data = conn.read()
# 
html_content = data.decode("utf-8")
# 2
soup = BeautifulSoup(html_content , "html.parser")
sec = soup.find("section" , "section chart-grid")
div = sec.find("div")
ul = div.find("ul")
li_list = ul.find_all("li")
# 3
list_song = []
count = 0

for li in li_list:
    # print(li.prettify())
    na = li.h3.a
    ar = li.h4.a
    # print(na.string)
    # print("* " * 20)
    # print(ar.string)
    new = {
    "name" : na.string,
    "artists" : ar.string
    }

    list_song.append(new)

    options = {
    'default_search': 'ytsearch',
    'max_downloads': 1
    }
    dl = YoutubeDL(options)
    downl = na.string + " " + ar.string
    dl.download([downl])

    count += 1
    if count == 5:
        break

pyexcel.save_as(records=list_song, dest_file_name="itunes.xlsx")