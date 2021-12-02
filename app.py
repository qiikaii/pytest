
from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	
	if request.method == "POST":
		search = request.form['search']
		## return search
		return redirect(url_for('mainpage', search=search))
	
	return render_template('index.html')

@app.route('/mainpage', methods=['GET', 'POST'])
def mainpage():
	search = request.args['search']
	return render_template('mainpage.html', search=search)

if __name__ == '__main__':
    app.run("0.0.0.0", "5000")
