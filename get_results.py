
from flask import Flask, render_template, request, redirect, url_for
from joblib import load


pipeline = load("fake_news_classification.joblib")

# Function to get the result for a particular text query
def requestResults(name):
    check = pipeline.predict(name)
    out = "Possible Fake News" if check==1 else "Possible Real News"
    return str(out)


# Start flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST','GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', name=user))

@app.route('/success/<name>')
def success(name):
    return str(requestResults([name]))