from flask import Flask, request, render_template
from flask.scaffold import F

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])

def cal():
    bmi = ''
    w = ''
    h = ''
    if request.method == 'POST' and 'weight' in request.form and 'height' in request.form :
        w1 = float(request.form.get('weight'))
        h1 = float(request.form.get('height'))
        bmi = round(w1/((h1/100)**2), 2)
        w = round(w1)
        h = round(h1)
    return render_template('index.html', bmi=bmi, weight=w, height=h )

if __name__ == '__main__':
   app.run(debug=True)