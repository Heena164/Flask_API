from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'
db = SQLAlchemy(app)
app = Flask(__name__)


employees = [
    { 'id':1, 'name': 'Salman', 'phone_no': 9967882181, 'com_name': 'TCL', 'job_role': 'Developer', 'location':'Andheri'},
    { 'id':2, 'name': 'Shahrukh', 'phone_no': 9967882121, 'com_name': 'Wipro', 'job_role': 'Developer', 'location':'Powai'},
    { 'id':3, 'name': 'Aamir', 'phone_no': 9967882233, 'com_name': 'Infosys', 'job_role': 'Full_Stack Developer', 'location':'Bandra'}

]
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify({"employees":employees})


@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    for employee in employees:
        if employee['id'] == employee_id:
            return jsonify(employee)
    return jsonify({'message': 'Employee not found'})

    
@app.route('/employees', methods=['POST'])
def add_employee():
    new_employee = {
        'id': request.json['id'],
        'name': request.json['name'],
        'phone_no': request.json['phone_no'],
        'comp_name': request.json['comp_name'],
        'job_role': request.json['job_role'],
        'location': request.json['location'] 
    }
    employees.append(new_employee)
    return jsonify(new_employee)

@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    for employee in employees:
        if employee['id'] == employee_id:
            employee['name'] = request.json['name']
            employee['phone_no'] = request.json['phone_no']
            employee['comp_name'] = request.json['comp_name']
            employee['job_role'] = request.json['job_role']
            employee['location'] = request.json['location']
            return jsonify(employee)
    return jsonify({'message': 'Employee not found'})


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)