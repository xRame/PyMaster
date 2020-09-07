from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello"

@app.route("/status")
def status():
	return{'status':'OK'}	

app.run()	