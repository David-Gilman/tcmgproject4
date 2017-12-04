from flask import Flask, request, json
import json, requests, config, math, redis


app = Flask(__name__)
db = redis.Redis('localhost')


@app.route('/')
def hello_world():
    return "Hello, welcome to my API application"


@app.route('/md5/<path:inp>')
def hash(inp):
	import md5
	m = md5.new()
	m.update(inp.encode('utf-8'))
	out =  m.hexdigest()
	return json.dumps({"input":inp, "output":out})


@app.route('/factorial/<int:inp>')
def fact(inp):
	try:
		if inp < 0:
			raise ValueError()
	except ValueError:
		return json.dumps({"input":inp, "output":"Value must be a non-negative integer"}) 
	else:
		out = math.factorial(inp);
		return json.dumps({"input":inp, "output":out})


@app.route('/fibonacci/<int:inp>')
def fibonacci(inp):
	try:
		if inp <= 0:
			raise ValueError()
	except ValueError:
		return json.dumps({"input":inp, "output":"Value must be a non-negative integer"}) 
	else:
		final = inp
		out = [0, 1, 1]
		i = 0
		while (out[-1]+out[-2]) <= final:
			i = out[-1] + out[-2] 
			out.append(i)
		return json.dumps({"input":inp, "output":out})


@app.route('/is-prime/<int:inp>')
def isPrime(inp):
        try:
                if inp <= 0:
                        raise ValueError()
        except ValueError:
                return json.dumps({"input":inp, "output":"Value must be an integer, greater than 0"}) 
        else:
		num = inp
		check = 1
		for i in range(2, num-1):
			if num % i == 0:
            			check = 0
		if inp == 1:
			check = 0
		if check:
			return json.dumps({"input":inp, "output":True})
		else:
			return json.dumps({"input":inp, "output":False})


@app.route('/slack-alert/<string:inp>')
def slackAlert(inp):
	try:
		url = config.HOOK
		r = requests.post(url, data=json.dumps({'text':inp}),headers={'Content-Type': 'application/json'})
		return json.dumps({"input":inp, "output":True})
	except Exception as err:
		print(err)
		return json.dumps({"input":inp, "output":False})


@app.route('/kv-record/', methods = ["POST", "PUT"])
def record():
	try:
		if request.method == "POST":
			data = request.json
			key, value = data.items()[0]
			db.set(key, value)
			return "0\n"

		elif request.method == "PUT":
			pass
	except:
		return "1"
		

@app.route('/kv-retrieve/')
def retrieve():
	pass


if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
