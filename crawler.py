from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

u=urlopen('http://www.mtcbus.org/Places.asp')
data=str(u.read())
soup = BeautifulSoup(data)
soup=soup.prettify()

f=open('data/list.html','w')
f.write(soup)
f.close()