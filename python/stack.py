class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to stack.")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop from empty stack.")
            return None
        item = self.stack.pop()
        print(f"Popped {item} from stack.")
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        print(f"Top element is {self.stack[-1]}")
        return self.stack[-1]

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack contents (top to bottom):")
            for item in reversed(self.stack):
                print(item)


# Menu-driven interface
def menu():
    stack = Stack()

    while True:
        print("\n--- Stack Menu ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            item = input("Enter item to push: ")
            stack.push(item)

        elif choice == '2':
            stack.pop()

        elif choice == '3':
            stack.peek()

        elif choice == '4':
            stack.display()

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    menu()
