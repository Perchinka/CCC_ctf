from flask import Flask, send_from_directory, request, render_template
app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/definitely_not_the_flag')
def falg():
    return 'CCC{d0_u_sp3ak_roBot1sh}'

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__=='__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')