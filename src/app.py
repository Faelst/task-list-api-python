from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1


@app.route("/task", methods=["POST"])
def createTask():
    global task_id_control
    data = request.get_json()
    new_task = Task(
        title=data["title"], description=data["description"], id=task_id_control
    )
    task_id_control += 1
    tasks.append(new_task)
    return jsonify({"message": "Nova tarefa foi criada com sucesso.", "task": new_task.toDict()})


@app.route("/task")
def getTask():
    task_list = [task.toDict() for task in tasks]
    output = {"tasks": task_list, "task_length": len(task_list)}
    return jsonify(output)


@app.route("/task/<int:id>")
def getTaskById(id):
    task = findTask(id)

    if task == None:
        return jsonify({"message": "Nao possível localizar a atividade"}), 404
    else:
        return jsonify({"task": task.toDict()})


@app.route("/task/<int:id>", methods=["PUT"])
def updateTask(id):
    task = findTask(id)
    
    if task == None:
        return jsonify({"message": "Nao possível localizar a atividade"}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    
    return jsonify({"message": "Task atualizada"})

@app.route("/task/<int:id>", methods=["DELETE"])
def deleteTask(id):
    task = findTask(id)
    
    if task == None:
        return jsonify({"message": "Nao possível localizar a atividade"}), 404
    
    tasks.remove(task)
    
    return jsonify({"message": "Tarefa Removida"})


def findTask(id):
    for t in tasks:
        if t.id == id:
            return t
        
    return None


if __name__ == "__main__":
    app.run(debug=True)
