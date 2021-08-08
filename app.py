from flask import Flask,redirect,render_template,jsonify
from flask.helpers import url_for
import bio

app=Flask(__name__)

#profile of straw hats
@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html',name=bio.straw_hat)

#generates API for Straw Hat Pirates
@app.route('/api')
def generate():
    return jsonify(bio.straw_hat)

if __name__ == '__main__':
    app.run(debug=False)