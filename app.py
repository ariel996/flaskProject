from flask import Flask, render_template, redirect, url_for, request
from requests import get

app = Flask(__name__)


@app.route('/')
def login():  # put application's code here
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    url = 'https://blossom.nvidia.com/jenkins/api/v1/projects/instances/list/'
    headers = {
        'Content-type': 'application/json'
    }
    response = get(url, auth=(username, password), headers=headers)
    output_json = response.iter_content(chunk_size=128)
    if response.status_code == 200:
        return redirect(url_for('homepage', response=output_json))
    else:
        return redirect(url_for('login'))

@app.route('/get-instance_node/{instance_name}')
def get_instance_node(instance_name: str):
    return 'ok';

@app.route('/homepage')
def homepage():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'about us'

if __name__ == '__main__':
    app.run()
