from flask import Flask, jsonify, render_template, request, Response
from jinja2 import Environment, PackageLoader
from urllib import urlopen
from bs4 import BeautifulSoup
import json, socket

app = Flask(__name__)
env = Environment(loader=PackageLoader('server', 'templates'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/busList')
def busList():
	f=open('data/busList','r')
	list=f.read().split('|')
	template = env.get_template('busSearch.html')
	return template.render(localStopList=[],busList=list)

@app.route('/getBus')
def getBus():
	f=open('data/routeList','r')
	list=f.read().split('|')
	template = env.get_template('placeSearch.html')
	return template.render(placeList=list)

@app.route('/getBusRoute')
def getBusRoute():
	bus=request.args.get('bus','',type=str)
	u=urlopen('http://www.mtcbus.org/Routes.asp?cboRouteCode='+bus)
	soup = BeautifulSoup(str(u.read()))
	# a=[v for v in[w for w in[z for z in[y for y in[x for x in soup.table.tr][3].table][1].table][1].table][1].children]
	# a=a[3:-2]
	# a.pop(1)
	# a.pop(1)
	b=soup.find_all('table')[4].find_all('table')[1].find_all('tr')
	resJS={
		'busType':b[2].find_all('td')[1].string,
		'busFrom':b[2].find_all('td')[2].string,
		'busTo':b[2].find_all('td')[3].string,
		'busTime':b[2].find_all('td')[4].string,
		'placeData':0
	}
	resJS['placeData']=[str(x.find_all('td')[-1].string) for x in b[5:-2]]
	return Response(json.dumps(resJS), mimetype='application/json')

@app.route('/getPlaceBuses')
def getPlaceBuses():
	p1=request.args.get('p1','',type=str)
	p2=request.args.get('p2','',type=str)
	u1=urlopen('http://www.mtcbus.org/Places.asp?cboSourceStageName='+p1+'&submit=Search.&cboDestStageName='+p2)
	u2=urlopen('http://www.mtcbus.org/Places.asp?cboSourceStageName='+p2+'&submit=Search.&cboDestStageName='+p1)
	soup1 = BeautifulSoup(str(u1.read()))
	soup2 = BeautifulSoup(str(u2.read()))
	a=soup1.find_all('td')[7].find_all('table')[1].find_all('tr')[1:-1]
	b=soup1.find_all('td')[7].find_all('table')[1].find_all('tr')[1:-1]
	resJS={
		'fromPlace':p1,
		'toPlace':p2,
		'busData':0
	}
	resJS['busData']=[{
		'busNo':str(x.find_all('td')[1].string),
		'busType':str(x.find_all('td')[2].string),
		'busTime':str(x.find_all('td')[3].string),
		'busFrom':str(x.find_all('td')[4].string),
		'busTo':str(x.find_all('td')[5].string),
		'noBus':str(x.find_all('td')[6].string)		
	} for x in b]
	if(len(a)!=len(b)):
		for x in a:
			for y in resJS['busData']:
				if(str(x.find_all('td')[1].string)!=y['busNo']):
					resJS['busData'].append({
						'busNo':str(x.find_all('td')[1].string),
						'busType':str(x.find_all('td')[2].string),
						'busTime':str(x.find_all('td')[3].string),
						'busFrom':str(x.find_all('td')[4].string),
						'busTo':str(x.find_all('td')[5].string),
						'noBus':str(x.find_all('td')[6].string)
					});
	return Response(json.dumps(resJS), mimetype='application/json')

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    port = sock.getsockname()[1]
    sock.close()
    app.run(port=port)
