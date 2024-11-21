from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/deals')
def deals():
    return render_template('deals.html')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
