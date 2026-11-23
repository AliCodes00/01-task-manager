tasks=[]
file=open("task.txt","w")
for task in tasks:
    file.write(task + "\n")
file.close
print("tasks saved successfuly")