from os import write


todoFile = open("todoList.txt","w",encoding="utf-8")
todoFile.write("to do list \n" + "1- todo 1 \n"+"2- todo 2 \n"+"3- todo 3 \n")
todoFile.close

#Read from file
todoFile = open("todoList.txt","r",encoding="utf-8")
todo_content = todoFile.read()
todoFile.close

print(todo_content)