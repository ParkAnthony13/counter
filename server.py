from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'speak friend and enter'


@app.route('/')
def home():
    if 'views' in session:
        session['views'] += 1
    else:
        session['views'] = 0
    return render_template('index.html')

@app.route('/drinks')
def add():
    session['views'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('views')		# clears a specific key
    session.clear()		# clears all keys
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
