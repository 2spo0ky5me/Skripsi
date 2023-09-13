from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/training')
def trainingPage():
    return render_template('trainingPage.html')

@app.route('/prediction')
def predictionPage():
    return render_template('predictionPage.html')

if __name__ == "__main__":
    app.run(debug=True)