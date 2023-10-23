from flask import Flask, render_template
from data import retrieval
import pandas as pd 

app = Flask(__name__)

@app.route('/')
def mainpage():
    df = retrieval()
    return render_template('index.html', rivers=df.values.tolist())

if __name__ == "__main__":
    app.run(debug=True)