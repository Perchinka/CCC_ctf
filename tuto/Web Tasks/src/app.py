from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'CCC{I_l0v3_s1mpl3_w3b}'

if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')