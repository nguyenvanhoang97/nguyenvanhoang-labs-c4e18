from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2018/1/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)

data = conn.read()

html_content = data.decode("utf-8")

soup = BeautifulSoup(html_content , "html.parser")

tabl = soup.find("table" , id = "tblGridData")

td_ls = tabl.find_all("td" , "h_t")

table = soup.find("table", id = "tableContent")

td_list = table.find_all("td","b_r_c")

#mới xđ đk vùng chưa add đk vào