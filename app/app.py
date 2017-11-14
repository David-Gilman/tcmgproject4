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


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

#Factorial
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
	print("Error: Factorial does not exist for negative numbers")
elif num == 0:
	print("The factorial of 0 is 1")
else:
	for i in range(1, num + 1):
		factorial *= i
	print("The factorial of", num, "is", factorial)
