
def add_item(todo_list, item):
    print("Add item")
    todo_list.append(item)


def list_items(todo_list):
    print("List of items:")
    for item in todo_list:
        print(item)

def mark_completed(todo_list, item):
    todo_list.remove(item)
    

def clear_list(todo_list):
    todo_list.clear()

def send_email(todo_list):
    print("Send email")
    for item in todo_list:
        print("Sending email to", item)

todo_list = []

while True:
    #Create the main program
    print("1. Add item")
    print("2. List items")
    print("3. Mark item as completed")
    print("4. Clear list")
    print("5. Send email")
    print("0. Exit program")
    choice = input("Enter your choice: ")
    if choice == "1":
        item = input("Enter item to add: ")
        add_item(todo_list, item)
    elif choice == "2":
        list_items(todo_list)
    elif choice == "3":
        item = input("Enter item to mark as completed: ")
        mark_completed(todo_list, item)
    elif choice == "4":
        clear_list(todo_list)
    elif choice == "5":
        send_email(todo_list)
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")
    print()
print("Exiting program. Have a nice day!")
