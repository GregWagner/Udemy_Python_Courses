''' First App '''
todos = []

while True:
    user_action = input('Type add, edit, show, or exit: ').strip().lower()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item.title())
        case 'edit':
            number = int(input('Number of the todo to edit: ')) - 1
            todos[number] = input('Enter new todo: ')
        case 'exit':
            break
print('bye')