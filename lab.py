
#1 Create a new file "todoList.txt"
file = open("todoList.txt" ,"w",encoding="utf-8")
file.writelines(["\nFinish my HW" , "\nDo some Python exercises" , "\nGo shopping "])
file.close()


#2 Read & print the file
file = open("todoList.txt" , "r",encoding="utf-8")
print(file.read())