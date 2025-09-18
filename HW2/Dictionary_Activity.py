mydict = {}

matrix = int(input("enter matrix size: "))

for i in range(matrix):
    item = input(f"Shopping item{i+1}: ")
    mydict[i] = item

print(f"\nYou have {len(mydict)} items in the cart\n")

while True:
    choice = input("What would you like to do [C]hange items [R]emove [D]isplay  S[earch] ? ").lower()

    if choice == "*":
        print("Bye")
        break

    # display
    elif choice == "d":
        print("Displaying Values")
        print("Key      Value")
        for k, v in mydict.items():
            print(f"{k:<8} {v}")

    # search
    elif choice == "s":
        search_val = input("Enter item to search: ")
        found = False
        for k, v in mydict.items():
            if v == search_val:
                print(f"Found {v} item")
                found = True
                break
        if not found:
           print("Im sorry, not in the cart")
    
                     

    # remove
    elif choice == "r":
        key = input("Enter key to search: ")
        key = int(key)
        if key in mydict:
            removed = mydict.pop(key)
            print(f"The key {key} with value {removed} has been deleted")
        else:
            print("Im sorry, not in the cart")
            
    # change
    elif choice == "c":
        key = int(input("Enter key to search: "))
        
        if key in mydict:
            print(f"Found {mydict[key]} item")
            new_value = input("Enter value: ")
            mydict[key] = new_value
        else:
            print("Im sorry, not in the cart")
    
    else:
        print("Invalid choice")
