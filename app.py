from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

todos = []

@app.route('/todos', methods=['GET', 'POST'])
def updateTodos():
  if request.method == 'GET':
    return jsonify(todos)
  elif request.method == 'POST':
    label = request.json.get('label')
    done = request.json.get('done')
    todos.append({"done": done, "label": label})
    return jsonify('Se agrego la tarea correctamente')

@app.route('/todos/<int:position>', methods=['DELETE'])
def deleteTodo(position):
  todos.pop(position)
  return jsonify('Se elimino la tarea correctamente')

if __name__ == "__main__": 
  app.run(host='localhost')