from flask import Flask, redirect, url_for


app = Flask(__name__)


@app.route("/")
def index():
    return "Index sample at lesson2"


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_world2(name=''):
    return 'Hi {}!'.format(name)


@app.route("/info")
def get_info():
    return "Info"


@app.route('/blog/<int:post_id>')
def show_blog(post_id):
    return 'Blog Number %d' % post_id


@app.route('/revision/<float:revision_number>')
def revision(revision_number):
    return 'Revision Number %f' % revision_number


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name =='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


with app.test_request_context():
    print (url_for('get_info'))
    print (url_for('hello_world2'))
    print (url_for('hello_world2', name='juan'))
    print (url_for('show_blog', post_id=1))
    print (url_for('revision', revision_number=1.5))


if __name__ == '__main__':
    app.run(debug=True)
