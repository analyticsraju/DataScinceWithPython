from flask import Flask, jsonify
from flask import abort
from flask import request
from werkzeug.utils import secure_filename
import os

os.getcwd()
os.chdir("D:/")

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


@app.route('/', methods=['GET'])
def get_tasks():
    return 'Welcome'

@app.route('/tasks', methods=['GET'])
def get_tasks2():
    return jsonify({'tasks': tasks})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

#@app.route('/createTasks', methods=['POST'])
#def create_task():
#    print("request gor here...",request.json)
#    if not request.json or not 'title' in request.json:
#        print("inside abort")
#        abort(400)
#        
#    #request.__getitem__()
#    print("request gor here...",request.json)
#    task = {
#        'id': tasks[-1]['id'] + 1,
#        'title': request.json['title'],
#        'description': request.json.get('description', ""),
#        'done': False
#    }
#    tasks.append(task)
#    print("inside response", tasks)
#    return jsonify({'task': task}), 201
#
#@app.route('/upload/', methods=['GET', 'POST'])
#def upload():
#   if request.method == 'POST':
#      file = request.files['file']
#      if file:
#        filename = secure_filename(file.filename)
#        file.save(os.path.join("/", filename))
#        a = 'file uploaded'
#        print(a)



if __name__ == '__main__':
    app.run()
