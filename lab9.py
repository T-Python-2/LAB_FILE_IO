from fileinput import close


file = open("todoList.txt", "w", encoding="utf-8")
content = file.write("my to-do list for today: \n")

#first way
'''file.writelines(["\n 1- solve my homework \n"," 2- cook \n"," 3- go shopping \n"," 4- do exercises "])'''
file.close()

#second way
file = open("todoList.txt", "a+", encoding="utf-8")
content = file.write(" 1- solve my homework \n")
content = file.write(" 2- cook \n")
content = file.write(" 3- go shopping \n")
content = file.write(" 4- do exercises \n")
file.close()



file = open("todoList.txt", "r", encoding="utf-8")
content = file.readlines()
print(content)
file.close
