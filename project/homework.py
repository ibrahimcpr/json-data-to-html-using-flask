import json
from flask import Flask, render_template




with open('us.json', 'r') as f:
    json_verisi = json.load(f)
    veri_dict = dict(json_verisi)


app = Flask(__name__)

@app.route('/')
def index3():
    return render_template('index.html',veri_dict=veri_dict)
if __name__ == "__main__":
    app.run(debug=True)