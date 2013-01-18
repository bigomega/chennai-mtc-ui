from flask import Flask, jsonify, render_template, request
from jinja2 import Environment, PackageLoader
from urllib import urlopen
from bs4 import BeautifulSoup

app = Flask(__name__)
env = Environment(loader=PackageLoader('server', 'templates'))

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/busList')
def hello():
	f=open('data/busList','r')
	list=f.read().split('|')
	template = env.get_template('busSearch.html')
	return template.render(localStopList=[],busList=list)

@app.route('/getBusRoute')
def getBusRoute():
	bus=request.args.post('bus','',type=str)
	u=urlopen('http://www.mtcbus.org/Routes.asp?cboRouteCode='+bus)
	soup = BeautifulSoup(str(u.read()))
	# a=[v for v in[w for w in[z for z in[y for y in[x for x in soup.table.tr][3].table][1].table][1].table][1].children]
	# a=a[3:-2]
	# a.pop(1)
	# a.pop(1)
	b=soup.find_all('table')[4].find_all('table')[1].find_all('tr')
	busType=b[2].find_all('td')[1].string
	busFrom=b[2].find_all('td')[2].string
	busTo=b[2].find_all('td')[3].string
	busTime=b[2].find_all('td')[4].string
	return jsonify(type=busType,from=busFrom,to=busTo,time=busTime,data=[str(x.find_all('td')[-1].string) for x in b[5:-2]])

if __name__ == "__main__":
    app.run(debug=True)