from os import write


#Create and add to file
todoFile = open("todoList.txt","w",encoding="utf-8")
todoFile.write("Learn More about I/O Files \n")
todoFile.write("Solve I/O Lab \n")
todoFile.close

#Read from file
todoFile = open("todoList.txt","r",encoding="utf-8")
content = todoFile.read()
todoFile.close

print(content)
