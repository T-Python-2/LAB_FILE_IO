
# write to the file
file = open("todoList.txt" ,"w",encoding="utf-8")
file.writelines (["\nSolve labs","\nLearn more about Today Pyhon's concepts","\nRead Quran"])
file.close()

# read the file and print the contetn
file = open("todoList.txt","r",encoding="utf-8")
content = file.read()
file.close()
print(content)