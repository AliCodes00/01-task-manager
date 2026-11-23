def show_menu():
    print("~~~~task manager~~~~")
    print("1.add task")  
    print("2.view task") 
    print("3.complete task") 
    print("4.delete task") 
    print("5.exit") 
    print("6. edit task")   
    print("7.search task")   
       
def get_choice():
    choice=input("choice an option:") 
    return choice 
tasks=[]
def save_task():
    file=open("task.txt","w")
    for task in tasks:
        file.write(task["title"] + "," + task["status"] + "\n")
    file.close        
def add_task():
    task_name=input("enter task name:")
    if task_name.strip()=="":
        print("task cannot be empty") 
    new_task={"title":task_name,"status":"pending"}
    tasks.append(new_task)
    print("successfuly")
    save_task()
def view_tasks():
    if len(tasks)==0:
        print("no task found")
    else:
        for index, task in enumerate(tasks,start=1):
            print (index,"-",task["title"],"-",task["status"])  
def complete_task():
    try:
        task_num=int(input("enter task number:"))
    except ValueError:
        print("please enter a valid number")
        return
    if 1<=task_num<=len(tasks):
        tasks[task_num - 1]["status"]="completed"
        print("task completed successfully")
    else:
         print("invalid task number")  
def delete_task():
    view_tasks()
    try:
        task_num=int(input("enter task number delete:"))
    except ValueError:
        print("please enter a valid number")
        return
    if 1<=task_num<=len(tasks):
        deleted_task=tasks.pop(task_num - 1)
        save_task()
        print("task deleted")
        print(deleted_task["title"],"deleted successfuly")
        
    else:
        print("invalid task number")
def edit_task():
    view_tasks()
    try:
        task_num=int(input("enter task number :"))
        if 1<=task_num<=len(tasks):
            new_task=input("enter new task name:")
            if new_task:
                tasks[task_num - 1]["title"] = new_task
                save_task()
                print("task updated !")
            else:
                    print("task name cannot be empty !")
        else:
            print("invalid task number !")
    except ValueError:
        print("please enter a valid number")
def search_task():
    search_name=input("enter task name:").strip()
    found =False
    for task in tasks:
        if search_name.lower() in task["title"].lower():
            print(f'task:{task["title"]}|status:{task["status"]}')
            found=True 
    if not found:
         print("no task found !")    

def load_tasks():
    try:
        file=open("task.txt","r")
        for line in file:
            title, status = line.strip().split(",")
            tasks.append({"title":title,"status":status})
        file.close()
    except FileNotFoundError:
        print("file not found")
load_tasks()                                       

while True:
    show_menu()
    user_choice=get_choice()

    if user_choice=="1":
        add_task()
    elif user_choice=="2":
        view_tasks()
    elif user_choice=="3":
        complete_task()
    elif user_choice=="4":
        delete_task()    
    elif user_choice=="5":
        print("goodbye?")
    elif user_choice =="6":
        edit_task()
    elif user_choice =="7":
        search_task()
        break
    else:
        print("invalid choice")   