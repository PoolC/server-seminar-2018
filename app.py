from flask import Flask, request, redirect, render_template, session

app = Flask(__name__)
app.secret_key = 'TOPSECRET'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        session['server'] = request.form['server']
        session['nickname'] = request.form['nickname']
        return redirect('/chat')


@app.route('/chat')
def chat():
    context = {
        'server': session['server'],
        'nickname': session['nickname'],
    }
    return render_template('chat.html', **context)
