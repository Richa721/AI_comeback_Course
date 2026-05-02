

grocery_list=[]

while True:
    choice=int(input("Enter your choice"))
    if choice==1:
        item=input("Enter the item to add: ")
        grocery_list.append(item)
        print("Item added successfully")
    elif choice==2:
        item=input("Enter item to remove: ")
        if item in grocery_list:
            grocery_list.remove(item)
            print("Successfully removed")
        else:
            print("Item not found")
    elif choice==3:
        print("Your Grocery List:", grocery_list)
    elif choice==4:
        print("Final Grocery List:", grocery_list)
        break
    else:
        print("Invalid choice")


