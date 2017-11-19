from flask import Flask
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Flask Dockerized'


@app.route('/md5/<path:inp>')
def hash(inp):
	import md5
	m = md5.new()
	m.update(inp.encode('utf-8'))
	out =  m.hexdigest()
	return json.dumps({"input":inp, "output":out})


@app.route('/factorial/<string:inp>/')
def factorial(inp):
	try:
		out = int(inp)
		if inp < 0:
			raise ValueError()
	except ValueError:
		return json.dumps({"input":inp, "output":"Value must be an integer, greater than 1"}) 
	else:
		for i in range(2,out):
			out *= i
		return json.dumps({"input":inp, "output":out})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
