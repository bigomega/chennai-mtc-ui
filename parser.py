from bs4 import BeautifulSoup

f=open('data/stopList.html','r')
soup = BeautifulSoup(f.read())
f.close()
open('data/stopList.html','w').close()
f=open('data/stopList.html','w')
f.write(str(soup))
f.close()

myList=[]
temp=soup.find('select').find_all('option')
for op in temp:
	myList.append(str(BeautifulSoup(str(op)).string))
myList.sort()

f=open('data/list','w')
for name in myList:
	f.write(name+'\n')
f.close()