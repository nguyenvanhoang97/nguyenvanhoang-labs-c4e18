from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://dantri.com.vn"
#1. download web page
#1.1 
conn = urlopen(url)

#1.2 read
data = conn.read()
# print(data)

#1.3 decode
html_content = data.decode("utf-8")
# print(html_content)

#1.4 save html_content to file
# import urllib.request
# urllib.request.urlretrieve(url, "dantri.html")
# f = open("dantri.html" , "wb")
# f.write(html_content)
# f.close()

#2. extract ROI
soup = BeautifulSoup(html_content , "html.parser")
# print(soup.prettify())
ul = soup.find("ul" , "ul1 ulnew")
# print(ul.prettify())
a_list_of_dictionaries = []


li_list = ul.find_all("li")
for li in li_list:
    # print(li.prettify())
    # print("* " * 20)
    # h4 = li.find("h4")
    # a = h4.find("a")
    #a = li.h4.a
    h4 = li.h4
    a = h4.a

 #3. extract info
 
    new = {
        "title" : a.string,
        "link" : url + a["href"]
    }
    a_list_of_dictionaries.append(new)
    # print(a.string)
    # print(url + a["href"])

pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="text.xlsx")