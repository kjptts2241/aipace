from flask import Flask, request, render_template, url_for, redirect
import face
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/naver')
def naver():
    return 'naver'


@app.route('/img')
def myimage():
    return render_template("myimage.html")


@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        imglink = request.form['imglink']
        face.url_image(imglink)
        return redirect(url_for('myimage'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)