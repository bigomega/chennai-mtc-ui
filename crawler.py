from urllib import urlopen

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

u=urlopen('http://www.mtcbus.org/Places.asp')
data=str(u.read())
#print(data[0:30].replace('\\n','\n'))
data=replace_all(data,{'\\\"':'\"','\\n':'\n','\\r':'','\\t':'	'});

f=open('data/stopList.html','w')
f.write(data)
f.close()
