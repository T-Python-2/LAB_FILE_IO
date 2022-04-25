
todo = open("ToDoList.txt","w",encoding="utf-8")
todo.write("Playing volleyball \n")
todo.write("Go for shopping \n")
todo.write("watch tv \n")
todo.write("Translate some articles \n")
todo.close

todoFile = open("ToDoList.txt","r",encoding="utf-8")
content = todoFile.read()
todoFile.close

print(content)