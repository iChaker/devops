import flask
import psutil
from hurry.filesize import size
from math import factorial
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/fact<n>')
def fact(n):
	try:
		return str(factorial(int(n)))
	except:
		return "error, please provide an int"


@app.route('/ramusage', methods=['GET'])
def home():
    values = psutil.virtual_memory()
    return size(values.available )



app.run(host="0.0.0.0",port=5000)
