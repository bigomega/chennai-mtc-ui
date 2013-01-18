from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

u=urlopen('http://www.mtcbus.org/Places.asp')
data=str(u.read())
#print(data[0:30].replace('\\n','\n'))
data=replace_all(data,{'\\\'':'\'','\\\"':'\"','\\n':'\n','\\r':'','\\t':'	'});

print (str(soup.title))

f=open('data/list.html','w')
f.write(soup)
f.close()

f=open('data/list.html','r')
soup = BeautifulSoup(f.read())
soup=soup.prettify()
f.close()