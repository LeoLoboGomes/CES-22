from flask import *
app = Flask(__name__)
app.secret_key = 'you can never'

@app.route('/')
def index():
   if 'username' in session:
      username = session['username']
      return render_template('logged.html', value = username)
   return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        html_text = '<p><h3>Selected objects:</h3></p>'
        try:
            session['object1'] = request.form['object1']
        except:
            session['object1'] = None
        try:
            session['object2'] = request.form['object2']
        except:
            session['object2'] = None
        try:
            session['object3'] = request.form['object3']
        except:
            session['object3'] = None
        if session['object1'] != None:
            html_text = html_text + '<h3>' + session['object1'] + '</h3><br>'
        if session['object2'] != None:
            html_text = html_text + '<h3>' + session['object2'] + '</h3><br>'
        if session['object3'] != None:
            html_text = html_text + '<h3>' + session['object3'] + '</h3><br>'
        html_text = html_text + '<a href="/logout">Logout</a>'
        return html_text



@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   session.pop('object1', None)
   session.pop('object2', None)
   session.pop('object3', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)