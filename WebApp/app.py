from flask import Flask, render_template, request, redirect, url_for, session
from Ai import 

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = "your_secret_key" 

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':  
            session['user'] = username  
            return redirect(url_for('home'))
        else:
            return "Error in username or password"
    return render_template('login.html')

@app.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/chatbot')
def chatbot():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('chatbot.html')

if __name__ == '__main__':
    app.run(debug=True)
