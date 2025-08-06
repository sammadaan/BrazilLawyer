import json
import os
from typing import List, Dict, Optional

DATA_FILE = "data/todos.json"
os.makedirs("data", exist_ok=True)  # Ensure the directory exists

def _load_todos() -> List[Dict]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def _save_todos(todos: List[Dict]):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=2, ensure_ascii=False)

def get_todos() -> List[Dict]:
    return _load_todos()

def add_todo(title: str) -> Dict:
    todos = _load_todos()
    new_todo = {"id": len(todos) + 1, "title": title, "done": False}
    todos.append(new_todo)
    _save_todos(todos)
    return new_todo

def update_todo(todo_id: int, done: Optional[bool]=None, title: Optional[str]=None) -> Optional[Dict]:
    todos = _load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            if done is not None:
                todo["done"] = done
            if title is not None:
                todo["title"] = title
            _save_todos(todos)
            return todo
    return None

def delete_todo(todo_id: int) -> bool:
    todos = _load_todos()
    new_todos = [todo for todo in todos if todo["id"] != todo_id]
    if len(new_todos) == len(todos):
        return False
    _save_todos(new_todos)
    return True