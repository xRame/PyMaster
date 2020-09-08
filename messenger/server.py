from flask import Flask, request
import time

app = Flask(__name__)
db = []

@app.route("/")
def hello():
	return "Hello"

@app.route("/status")
def status():
	return{'status':'OK'}	

@app.route("/send", methods = ['POST'])
def send():
	data = request.json
	
	db.append({
		'id':len(db),
		'name': data['name'],
		'text': data['text'],
		'timestamp': time.time()

		})
	return{'ok':True}	

@app.route("/messages")
def messages():
	if 'after_id' in request.args:
		after_id = int(request.args['after_id'])
	else:
		after_id = 0	
	return{'messages':db[after_id:]}	


app.run()	