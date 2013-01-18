from flask import Flask
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('yourapplication', 'templates'))

@app.route("/")
def hello():
	template = env.get_template('busSearch.html')
	print template.render(localStopList=[])
    return template.render(localStopList=[])

if __name__ == "__main__":
    app.run()