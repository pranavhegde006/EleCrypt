from flask import Flask,render_template,request,redirect,url_for,jsonify
from firebaseapp import firebaseapp
from functions import machagiveno, decrypt
from time import ctime
app = Flask(__name__)

firebaseapp=firebaseapp

@app.route('/',methods = ['GET','POST'])
def one():
	if request.method == 'GET':
		return render_template('index.html',title='one',time=ctime())
	else:
		time = request.form['time']
		sensornum = request.form['sensornum']
		print(f'looking for sensor data from {time} from {sensornum} ... ')
		data = machagiveno(sensornum,firebaseapp,time=time)
		if data:
			print(f'data found: {data}')
			return render_template('two.html',title='two',time=time,data=decrypt(data))
		else:
			print(f'data not found for {time}')
			return render_template('two.html',title='two',time=time)

@app.route('/api/v1/data')
def api():
	data = firebaseapp.get('/sensor3',None)
	return jsonify(decrypt(data))



if __name__ == '__main__':
	app.run()


