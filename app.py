
from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf.csrf import CSRFProtect
import secrets

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config["SECRET_KEY"] = secrets.token_urlsafe(16)

@app.route('/', methods=['GET', 'POST'])
def index():
	
	if request.method == "POST":
		session['search'] = request.form['search']
		## return search
		return redirect(url_for('mainpage'))
	
	return render_template('index.html')

@app.route('/mainpage', methods=['GET', 'POST'])
def mainpage():
	
	return render_template('mainpage.html', search=session['search'])

if __name__ == '__main__':
    app.run("0.0.0.0", "80")
