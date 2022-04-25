my_file = open("todoList.txt","w")
my_file.write(" study\n go for a walk\n working out on the gym \n buy groceries \n doctor appoinment ")
my_file.close

my_file = open("todoList.txt", "r+")
content = my_file.read()
print(content)