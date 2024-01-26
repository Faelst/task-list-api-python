import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"
task = []


def testCreateTask():
    new_task_data = {"title": "Nova tarefa", "description": "Descricao da nova tarefa"}

    response = requests.post(f"{BASE_URL}/task", json=new_task_data)
    response_json = response.json()

    assert response.status_code == 200
    assert "message" in response_json
    assert "id" in response_json["task"]


def testGetTasks():
    response = requests.get(f"{BASE_URL}/task")
    response_json = response.json()

    assert response.status_code == 200
    assert "tasks" in response_json
    assert "task_length" in response_json

def testGetTaskById():
    id = 1
    response = requests.get(f"{BASE_URL}/task/{id}")
    response_json = response.json()

    assert response.status_code == 200
    assert "task" in response_json
    assert response_json['task']['id'] == id


def testUpdateTask():
    updatePayload = {
        "id": 1,
        "title": "Outro description",
        "description": "Outro description",
        "completed": True,
    }
    
    response = requests.put(f"{BASE_URL}/task/1", json=updatePayload)
    response_json = response.json()
    
    responseGet = requests.get(f"{BASE_URL}/task/1")
    responseGetJson = responseGet.json()

    assert response.status_code == 200
    assert response_json['message'] == 'Task atualizada'
    assert responseGetJson['task'] == updatePayload
    
def testRemoveTask():
    if task:
        response = requests.delete(f"{BASE_URL}/task/1")
        response_json = response.json()
    
        assert response.status_code == 200
        assert response_json['message'] == 'Tarefa Removida'
