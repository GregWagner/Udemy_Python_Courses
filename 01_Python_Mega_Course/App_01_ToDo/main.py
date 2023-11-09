''' toDo list console applicaation '''

user_prompt: str = "Enter a todo: "
todos: list[str] = []

while True:
    todo: str = input(user_prompt)
    todos.append(todo)
    print(todos)
