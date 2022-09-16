import requests
from flask import Flask, render_template, redirect, url_for, request
from requests import get

app = Flask(__name__)


@app.route('/')
def login():  # put application's code here
    payload = {}
    headers = {
        'Authorization': 'Basic c3ZjLWJsc20taG9zdGxlYXNlOjgjOUpmUyEyWVNqJnNxIVI='
    }
    url = 'https://blossom.nvidia.com/jenkins/api/v1/projects/instances/list/'
    response = requests.request("GET", url, headers=headers, data=payload)
    output_json = response.iter_content(chunk_size=128)
    if response.status_code == 200:
        return render_template('index.html', output_json=output_json)
    else:
        return 'unable to continue'

@app.route('/login', methods=['POST'])
def login_post():
    payload = {}
    headers = {
        'Authorization': 'Basic c3ZjLWJsc20taG9zdGxlYXNlOjgjOUpmUyEyWVNqJnNxIVI='
    }
    url = 'https://blossom.nvidia.com/jenkins/api/v1/projects/instances/list/'
    response = requests.request("GET", url, headers=headers, data=payload)
    output_json = response.iter_content(chunk_size=128)
    if response.status_code == 200:
        return redirect(url_for('homepage', response=output_json))
    else:
        return redirect(url_for('login'))

@app.route('/get-instance_node/{instance_name}')
def get_instance_node(instance_name: str):
    payload = {}
    headers = {
        'Authorization': 'Basic c3ZjLWJsc20taG9zdGxlYXNlOjgjOUpmUyEyWVNqJnNxIVI='
    }
    url = "https://blossom.nvidia.com/" + instance_name + "/computer/api/json"
    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.json()
    context = {
        'result': result,
        'instance_name': instance_name,
    }
    return render_template('instance_node.html', context=context)

@app.route('/homepage')
def homepage():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'about us'

if __name__ == '__main__':
    app.run()
