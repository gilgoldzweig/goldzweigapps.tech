from flask import Flask, jsonify, request, session, make_response
import mail
from pymongo import MongoClient as client
from flask_session import Session

clientLink = 'mongodb://gilgoldzweig:0508392942g@ds049486.mlab.com:49486/users'
mongo = client(clientLink)
db = mongo.get_default_database()
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


def getByName(name):
	return request.form[name]

#Handle signup post request
@app.route('/api/signup', methods = ['POST'])
def signup():
	users = db['users']
	email_exist = users.find_one({'email' : getByName('email')}) is not None
	username_exist = users.find_one({'username' : getByName('username')}) is not None

	password_ok = not(email_exist or username_exist)

	if password_ok:
		try:
			users.insert({
				'name' : getByName('name'),
				'email' : getByName('email'),
				'username' : getByName('username').lower(),
				'password' : getByName('password')
				})
			return make_response('User created seccessfully.')
		except Exception as e:
			app.logger.debug(e)
			return make_response('Server error please try again later')
	elif email_exist:
		return make_response("Email address already exist please try something else.")
	elif username_exist:
		return make_response('Username already taken please try something else.')
	else:
		return make_response('Server error try again later.')
				

#Handle login post request
@app.route('/api/login', methods = ['POST'])
def login():
	users = db['users']
	user = users.find_one({'username': getByName('username').lower(), 'password' : getByName('password')})
	if user != None:
		session['username'] = user['username']
		return make_response('Login seccessfully,')
	else:
		return make_response('Username or password is incorrect')	

@app.route('/api/logout', methods = ['POST'])
def logout():
	if 'username' in session:
		session.pop('username', None)
		return make_response('Bye bye.')

@app.route('/api/session', methods = ['GET'])
def getSession():
	if 'username' in session:
		return make_response('Session is alive.')
	else:
		return make_response('Session is dead.')
			

#Handle mail sending post request
@app.route('/api/mail', methods = ['POST'])	
def sendMail():
	return make_response(mail.send('name', 'from', 'subject', 'message'))

#Handle custom object saving post request
@app.route('/api/save', methods = ['POST'])
def save():
	pass


#Handle values get request
@app.route('/api/values', methods = ['GET'])
def getValues():
	pass

#Handle DataBase save
def saveToDB():
	pass

#Handle DataBase get functions
def getFromDB():
	pass


if __name__ == '__main__':
    
    app.run(debug = True)