
#Create and add to file
todoFile = open("todoList.txt","w",encoding="utf-8")
todoFile.write("solve labs\n")
todoFile.write("reading \n")
todoFile.write("watch tv \n")
todoFile.write("go to sopermarket \n")
todoFile.close


#Read from file
todoFile = open("todoList.txt","r",encoding="utf-8")
content = todoFile.read()
todoFile.close

print(content)
