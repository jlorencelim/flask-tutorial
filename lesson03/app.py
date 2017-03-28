from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('name')
        return redirect(url_for('success', name=user))


@app.route('/')
def index():
    return '<html><body><h1>Hello World</h1></body></html>'


@app.route('/hello/')
def hello():
    return render_template('hello.html')


@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello_name.html', name=user)


@app.route('/score/<int:score>')
def hello_score(score):
    return render_template('hello_score.html', marks=score)


@app.route('/result')
def result():
    dict = {
        'physics': 50,
        'chemistry': 60,
        'math': 70
    }
    return render_template('result.html', result=dict)


@app.route("/hello-static")
def hello_static():
    return render_template("hello_static.html")


if __name__ == '__main__':
    app.run(debug = True)
