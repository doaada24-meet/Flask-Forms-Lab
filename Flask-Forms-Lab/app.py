from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "aesthetic_photos"
password = "778654"
facebook_friends=["Taleen","Mjd","Waseem", "Maria", "Zena", "Katia"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method=='POST':
		 u=request.form['username'] 
		 p = request.form['password']
		 if p==password and u==username:
		 	   return redirect(url_for('home'))
	return render_template('login.html')


@app.route('/home',methods=['GET','POST'])
def home():
	return render_template('home.html', friends=facebook_friends)


@app.route('/friend_exists/<string:name>',methods=['GET','POST'])
def name_3(name):
	  return render_template('friend_exists.html',facebook_friends=facebook_friends,name=name)




	   # return 'You just made a POST request!'
   #_template('login.html',un='username',p='password)
  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)