
from flask import Flask,request, render_template, redirect, url_for

import login

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method=="POST":
        link= request.form.get('link')
        sel()
    return render_template('index.html')

def sel():
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8888', debug=True)