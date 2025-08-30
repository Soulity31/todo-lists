todo =[]

isRunning= True
while isRunning:
    user2=input("What do you want to do in todo list today?\n(add(a), delete(d), view(v), use q to quit ) \n").lower()
    if user2 =="add" or user2=="a":
        print(f"This is your list {todo}")
        user1i=input("What you want to add?\n")
        todo.append(user1i)
        last_index=len(todo) - 1
        print(f"You have sucessfully added the todo '{todo[last_index]}'")
    elif user2 =="view" or user2=="v":
        for i in range(1,len(todo)):
            print(f"{i}:{todo[i]}")
                 
    elif user2=="delete"or user2=="d":
        print("Here is your todo list")
        print(todo)
        user2i=(input("\nWhat do you want to delete?\n").lower())
        if user2i not in todo:
            print("Not found in your todo list")
            continue
        else:  
            todo.remove(user2i)
            print(f"You have successfully removed {user2i}")
    elif user2=="nothing" or user2=="none" or user2=="no" or user2=="n" or user2=="quit" or user2=="q":
        print("Here is a quote for you\nWork hard today, conquer tomorrow!")
        isRunning=False
                
                 



