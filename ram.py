import flask
import psutil
from hurry.filesize import size
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/ramusage', methods=['GET'])
def home():
    values = psutil.virtual_memory()
    return size(values.available )



app.run(host="0.0.0.0",port=5000)