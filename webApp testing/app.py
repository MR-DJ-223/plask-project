from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Define a list of services
services = ["Lambda", "RDS", "EC2", "Load Balancers"]

# Route to fetch the list of services
@app.route('/services')
def get_services():
    return render_template('services.html')

# Route to render the index.html template
@app.route('/')
def index():
    return render_template('temp.html')

@app.route('/services/lambda')
def lambda_reports():

    return render_template('lambda_reports.html')

if __name__ == '__main__':
    app.run(debug=True)
