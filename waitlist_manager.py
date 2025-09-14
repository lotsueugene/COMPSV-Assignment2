# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self,name):
        self.name=name
        self.next=None




# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head=None 

    # add_front(name): Adds a customer to the front of the waitlist.
    def add_front(self,name):
        new_node=Node(name)
        new_node.next=self.head
        self.head=new_node
    
    # add_end(name): Adds a customer to the end of the waitlist.
    def add_end(self,name):
        new_node=Node(name)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node

     # remove(name): Removes a customer from the waitlist by name.
    def remove(self,name):
       
        current=self.head
        previous=None

        while  current is not None:
            if current.name==name:
                if previous is  None:
                    self.head=current.next
                else:
                    previous.next=current.next
                return  f"Removed {name} from the waitlist"
            previous=current
            current=current.next
        return f"{name} not found."

    # print_list(): Prints the current waitlist.
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.name,end='->')
            temp=temp.next
        print()


waitlist=LinkedList()
def waitlist_generator():
    # Create a new linked list instance
    
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)
            waitlist.print_list()
            

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            waitlist.add_end(name)
            waitlist.print_list()
            
            
            

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            result=waitlist.remove(name)
            print(result)
            waitlist.print_list()
            
            
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            
            waitlist.print_list()
            
            
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?
'''


# My list works by first asking the user to interact with a specific command such as add name to the front, add name to the end, or remove name from the list.
# For example, if a user enters a name and selects “add_front,” the name is stored at the front of the list if there are other names already waiting.
# If this user happens to be the first input, the name is stored in the first node.
# The head in the code keeps track of the very first node in the linked list.

# Real engineers might use lists like this when handling data that changes often and when quick insertions or deletions are needed, for example in waitlists or real-time scheduling systems.
# It is useful because it does not require shifting data the way a standard Python list does.