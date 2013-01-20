from bs4 import BeautifulSoup

f=open('data/stopList.html','r')
soup = BeautifulSoup(f.read())
f.close()
myRouteList=[]
temp=soup.find('select').find_all('option')
for op in temp:
	myRouteList.append(str(BeautifulSoup(str(op)).string))
myRouteList.sort()
f=open('data/routeList','w')
for name in myRouteList:
	f.write(name+'\n')
f.close()


f=open('data/busList.html','r')
soup = BeautifulSoup(f.read())
f.close()
myBusList=[]
temp=soup.find('select').find_all('option')
for op in temp:
	loc=str(BeautifulSoup(str(op)).string)
	if loc!="" and loc!="None":
		myBusList.append(loc)
myBusList.sort()
f=open('data/busList','w')
for name in myBusList:
	f.write(name+'\n')
f.close()
