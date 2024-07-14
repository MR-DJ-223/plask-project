from flask import Flask, render_template, request, redirect, url_for, jsonify
import datetime
import json
import os

app = Flask(__name__)

DATA_FILE = 'data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {'notes': [], 'activities': [], 'passwords': {}, 'accounts': []}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

data = load_data()

@app.route('/')
def index():
    return render_template('index.html', notes=data['notes'], activities=data['activities'])

@app.route('/update_note', methods=['POST'])
def update_note():
    note = request.form.get('note')
    if note:
        data['notes'].append(note)
        save_data(data)
    return redirect(url_for('index'))

@app.route('/update_activity', methods=['POST'])
def update_activity():
    activity = request.form.get('activity')
    time = request.form.get('time')
    if activity and time:
        data['activities'].append({'activity': activity, 'time': time})
        save_data(data)
    return redirect(url_for('index'))

@app.route('/cyberark')
def cyberark():
    return render_template('cyberark.html')

@app.route('/lz_prod')
def lz_prod():
    return render_template('lz_prod.html', accounts=data['accounts'])

@app.route('/update_password', methods=['POST'])
def update_password():
    service = request.form.get('service')
    password = request.form.get('password')
    if service and password:
        data['passwords'][service] = password
        save_data(data)
    return redirect(url_for('cyberark'))

@app.route('/get_password', methods=['GET'])
def get_password():
    service = request.args.get('service')
    if service:
        password = data['passwords'].get(service, '')
        return jsonify(password=password)
    return jsonify(password='')

@app.route('/add_account', methods=['POST'])
def add_account():
    account = request.form.get('account')
    if account:
        data['accounts'].append(account)
        save_data(data)
    return redirect(url_for('lz_prod'))

@app.route('/search_account', methods=['GET'])
def search_account():
    query = request.args.get('query')
    results = [account for account in data['accounts'] if query.lower() in account.lower()]
    return jsonify(results=results)

if __name__ == '__main__':
    app.run(debug=True)
