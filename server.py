from flask import Flask
from jinja2 import Environment, PackageLoader

app = Flask(__name__)
env = Environment(loader=PackageLoader('server', 'templates'))

@app.route("/")
def hello():
	f=open('data/busList','r')
	list=f.read().split('\n')
	template = env.get_template('busSearch.html')
	return template.render(localStopList=[],busList=list)

if __name__ == "__main__":
    app.run(debug=True)