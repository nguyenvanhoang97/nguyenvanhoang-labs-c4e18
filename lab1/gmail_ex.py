from gmail import*
from random import choice
import datetime
now = datetime.datetime.now()
# print (now.year, now.month, now.day, now.hour, now.minute, now.second)


html_content = """
<p style="text-align: center;">Cộng h&ograve;a x&atilde; h&ocirc;i chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Độc lập - Tự do - Hạnh ph&uacute;c</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">ĐƠN XIN NGHỈ HỌC</p>
<p style="text-align: left;">K&iacute;nh gửi: Gi&aacute;o vi&ecirc;n chủ nhiệm</p>
<p style="text-align: left;">Em t&ecirc;n l&agrave;: Nguyễn Văn Ho&agrave;ng</p>
<p style="text-align: left;">L&yacute; do em viết đơn n&agrave;y l&agrave; để xin buổi học h&ocirc;m nay \
    {{sickness}}</p>
<p style="text-align: left;">&nbsp;</p>
"""

#placeholder
sickness = ["đau tay" , "đau chân" , "sốt"]
reson = choice(sickness)
news = html_content.replace("{{sickness}}" , reson)

while True:
    if now.hour == 7:
        gmail = GMail('nvhoang00010@gmail.com','hn18071997')
        msg = Message('Hello',
                        to='dongkooi01@gmail.com',
                        html = news)
        gmail.send(msg)
        break