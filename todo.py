import argparse
import json
import os

TODO_FILE = "todos.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f)

def add_task(task):
    todos = load_todos()
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print(f"Tarefa adicionada: '{task}'")

def list_tasks():
    todos = load_todos()
    if not todos:
        print("Nenhuma tarefa encontrada.")
        return
    for i, todo in enumerate(todos, 1):
        status = "✓" if todo["done"] else " "
        print(f"{i}. [{status}] {todo['task']}")

def complete_task(index):
    todos = load_todos()
    if 1 <= index <= len(todos):
        todos[index-1]["done"] = True
        save_todos(todos)
        print(f"Tarefa {index} marcada como concluída!")
    else:
        print("Índice inválido.")

def main():
    parser = argparse.ArgumentParser(description="CLI Todo List")
    subparsers = parser.add_subparsers(dest="command")

    parser_add = subparsers.add_parser("add", help="Adicionar tarefa")
    parser_add.add_argument("task", type=str, help="Descrição da tarefa")

    subparsers.add_parser("list", help="Listar tarefas")

    parser_complete = subparsers.add_parser("complete", help="Marcar tarefa como concluída")
    parser_complete.add_argument("index", type=int, help="Número da tarefa")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.task)
    elif args.command == "list":
        list_tasks()
    elif args.command == "complete":
        complete_task(args.index)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
