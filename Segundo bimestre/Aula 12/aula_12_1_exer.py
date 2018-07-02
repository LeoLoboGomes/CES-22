from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        try:
            user = request.form['nm']
        except:
            user = None
        try:
            user_bd = request.form['bday']
        except:
            user_bd = None
        try:
            checkbox1 = request.form['vehicle1']
        except:
            checkbox1 = None
        try:
            checkbox2 = request.form['vehicle2']
        except:
            checkbox2 = None
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', '', expires=0)
        resp.set_cookie('birthday', '', expires=0)
        resp.set_cookie('checkbox1', '', expires=0)
        resp.set_cookie('checkbox2', '', expires=0)
        try:
            resp.set_cookie('userID', user)
        except:
            pass
        try:
            resp.set_cookie('birthday', user_bd)
        except:
            pass
        try:
            resp.set_cookie('checkbox1', checkbox1)
        except:
            pass
        try:
            resp.set_cookie('checkbox2', checkbox2)
        except:
            pass
        return resp

@app.route('/getcookie')
def getcookie():
    try:
        name = request.cookies.get('userID')
    except:
        name = None
    try:
        birthday = request.cookies.get('birthday')
    except:
        birthday = None
    try:
        checkbox1 = request.cookies.get('checkbox1')
    except:
        checkbox1 = None
    try:
        checkbox2 = request.cookies.get('checkbox2')
    except:
        checkbox2 = None
    html_text = ''
    if (name != None):
        html_text = html_text + '<h1>welcome '+name+'</h1>'
    if (birthday != None):
        html_text = html_text + '<h1>Data Aniversario ' + birthday + '</h1>'
    if (checkbox1 != None):
        html_text = html_text + '<h1>' + checkbox1 + '</h1>'
    if (checkbox2 != None):
        html_text = html_text + '<h1>' + checkbox2 + '</h1>'
    return html_text

if __name__ == '__main__':
    app.run(debug = True)