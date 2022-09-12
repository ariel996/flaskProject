from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def login():  # put application's code here
    return render_template('index.html')

@app.route('/homepage')
def homepage():
    return 'homepage'

@app.route('/about')
def about():
    return 'about us'

if __name__ == '__main__':
    app.run()
