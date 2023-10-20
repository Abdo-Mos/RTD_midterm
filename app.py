# user_service.py

from flask import Flask, jsonify, request
# import requests

app = Flask(__name__)


students = [ 
    {'id': 1, 'name': 'Muna', 'grade': 'A+'},
    {'id': 2, 'name': 'Ghosh', 'grade': 'B+'},
    {'id': 3, 'name': 'Cam', 'grade': 'C+'},
    {'id': 4, 'name': 'Abdo', 'grade': 'D+'}
]


@app.route('/')
def home():
    return jsonify(students)

# -R- read 
@app.route('/student/<id>')
def student(id):
    student = None
    for stu in students:
        if int(stu['id']) == int(id):
            student = stu
            break

    if student == None:
        return jsonify({'error:': 'stu not found'})
    
    return jsonify({'found': student})

# -C- create  
@app.route('/student', methods=['POST'])
def create_stu():
    new_stu = {
        'id': request.json['id'],
        'name': request.json['name'],
        'grade': request.json['grade']
    }
    students.append(new_stu)
    return jsonify({'user': new_stu})

# -U- update 
@app.route('/student/<int:id>', methods=['PUT'])
def update_stu(id):
    print("hello from update")
    student = None
    for stu in students:
        if int(stu['id']) == int(id):
            student = stu
            break

    if student == None:
        return jsonify({'error:': 'stu not found'})
    
    student['name'] = request.json['name']
    student['grade'] = request.json['grade']

    return jsonify({'updated': student})

# -D- delete 
@app.route('/student/<id>', methods=['DELETE'])
def delete_stu(id):
    stu = None
    for usr in students:
        if int(usr['id']) == int(id):
            stu = usr
            break

    if stu == None:
        return jsonify({'error:': 'stu not found'})
    
    students.remove(stu)
    return jsonify("Deleted successfully")


if __name__ == '__main__':
    app.run(port=5000)