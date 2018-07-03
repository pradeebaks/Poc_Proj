import urllib.request as rs
from re import findall as f


url = "https://www.britishairways.com/en-gb/information/help-and-contacts/contact-us"
# 0344 493 0787
con = rs.urlopen(url)
rd = con.read()
strval = rd.decode()
pdata = f("\d{4} \d{3} \d{4}",strval)
for d in pdata:
    print (d)

