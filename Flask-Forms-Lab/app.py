from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/')  # '/' for the default page
def login():
  return render_template('login.html')

@app.route('/test', methods=['GET', 'POST'])
def method():
    if request.method == 'POST':
    	if username==username and password==password:
    		return render_template('home.html')
    
    else:
        
        return render_template('login.html')


@app.route('/home')  # '/' for the default page
def home():
  return redirect(url_for('home' , facebook_friends=facebook_friends))

@app.route('/friend_exists/<string:name>', methods=['GET', 'POST'])  # '/' for the default page
def login1(name):
	if name in facebook_friends:
		return ('true' )
	else:
		return ("false")







if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)