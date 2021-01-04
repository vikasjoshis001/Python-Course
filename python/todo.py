import time
import datetime

try:
    while True:
        str1 = input()
        task = input().split(' ')
        cmd = task[0]
        if cmd == "add":
            tsk = task[1]
            file1 = open("todo.txt","w") 
            # L = []
            # L.append(tsk)
            file1.write(tsk)
            file1.close()

        elif cmd == "ls":
            file1 = open("todo.txt","r") 
            print(file1.readline())

        elif cmd == "del":
            tsk = task[1]
            file2 = open("todo.txt", "r")
            lines = file2.readlines()
            print(lines)
            file2.close()
            del lines[int(tsk)-1]
            new_file = open("todo.txt", "w+")
            for line in lines:
                new_file.write(line)
            new_file.close()

        elif cmd == "done":
            tsk = task[1]
            file2 = open("todo.txt", "r")
            file3 = open("done.txt","w")
            lines = file2.readlines()
            file2.close()
            dte = datetime.today().strftime('%Y-%m-%d')
            file3.write("x"+dte+lines[int(tsk)])
            del lines[int(tsk)]
            new_file = open("sample.txt", "w+")
            for line in lines:
                new_file.write(line)
            new_file.close()

        elif cmd == "help":
            print("./todo add 'todo item'  # Add a new todo")
            print("./todo ls               # Show remaining todos")
            print("./todo del NUMBER       # Delete a todo")
            print("./todo done NUMBER      # Complete a todo")
            print("./todo help             # Show usage")
            print("./todo report           # Statistics")
except:
    print("Exception Raised")
    pass