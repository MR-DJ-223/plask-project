from flask import Flask, render_template, request, redirect, url_for, jsonify
import datetime

app = Flask(__name__)

# Dummy data for demonstration
notes = []
activities = []
passwords = {
    'cyberark': '',
    'prod_account': '',
    'ss_dev': ''
}

@app.route('/')
def index():
    return render_template('index.html', notes=notes, activities=activities)

@app.route('/update_note', methods=['POST'])
def update_note():
    note = request.form.get('note')
    if note:
        notes.append(note)
    return redirect(url_for('index'))

@app.route('/update_activity', methods=['POST'])
def update_activity():
    activity = request.form.get('activity')
    if activity:
        activities.append(activity)
    return redirect(url_for('index'))

@app.route('/update_password', methods=['POST'])
def update_password():
    service = request.form.get('service')
    password = request.form.get('password')
    if service and password:
        passwords[service] = password
    return redirect(url_for('index'))

@app.route('/get_password', methods=['GET'])
def get_password():
    service = request.args.get('service')
    if service:
        password = passwords.get(service, '')
        return jsonify(password=password)
    return jsonify(password='')

if __name__ == '__main__':
    app.run(debug=True)
