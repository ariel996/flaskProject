import json
import os
from json import JSONDecodeError
import requests
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/"

@app.route('/')
def login():  # put application's code here
    return render_template('index.html')


@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['instance_name_file']
        filename = secure_filename(f.filename)
        f.save(app.config['UPLOAD_FOLDER'] + filename)
        file = open(app.config['UPLOAD_FOLDER'] + filename, "r")
        content = file.read()
        result = content.split('\n')
    return render_template('instance_name.html', result=result)



@app.route('/get_instance_node/<string:instance_name>')
def get_instance_node(instance_name: str):
    payload = {}
    headers = {
        'Authorization': 'Basic c3ZjLWJsc20taG9zdGxlYXNlOjgjOUpmUyEyWVNqJnNxIVI='
    }
    url = "https://blossom.nvidia.com/" + instance_name + "/computer/api/json"
    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.json()
    key = 'Swarm agent'
    systL = "Linux"
    key_system = "hudson.node_monitors.ArchitectureMonitor"
    return render_template('instance_node.html', response=response, result=result, instance_name=instance_name, key=key, systL=systL, key_system=key_system)


@app.route('/homepage')
def homepage():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
