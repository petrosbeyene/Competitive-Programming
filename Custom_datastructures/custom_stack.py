class Node:
    """
    A node in a linked list structure.
    
    Each node contains a value and a reference to the next node.
    Used as the building block for our stack implementation.
    """
    def __init__(self, value):
        """
        Initialize a new node with the given value.
        
        Args:
            value: The data to be stored in this node
        """
        self.value = value  # The data stored in this node
        self.next = None    # Reference to the next node (initially None)


class Stack:
    """
    A custom implementation of a stack data structure from scratch without using built-in lists.
    
    This implementation uses a singly linked list structure where:
    - The 'head' points to the top of the stack
    - New elements are added to the top (head) of the stack
    - Elements are removed from the top (head) of the stack
    
    This follows the Last-In-First-Out (LIFO) principle.
    """
    
    def __init__(self):
        """
        Initialize an empty stack.
        
        Sets up the head pointer to None and a counter for tracking the size.
        """
        self.head = None  # Points to the top of the stack (initially empty)
        self._size = 0    # Counter to track the number of elements
    
    def push(self, value):
        """
        Add an element to the top of the stack.
        
        Implementation:
        1. Create a new node with the given value
        2. Set the new node's next pointer to the current head
        3. Update the head to point to the new node
        4. Increment the size counter
        
        Args:
            value: The element to be added to the stack
            
        Time Complexity: O(1) - Constant time
        """
        new_node = Node(value)  # Create a new node with the given value
        new_node.next = self.head  # New node points to current top
        self.head = new_node  # Update head to point to the new node
        self._size += 1  # Increment size counter
    
    def pop(self):
        """
        Remove and return the top element from the stack.
        
        Implementation:
        1. Check if the stack is empty
        2. Save the value of the head node
        3. Update the head to point to the next node
        4. Decrement the size counter
        5. Return the saved value
        
        Returns:
            The value at the top of the stack
            
        Raises:
            IndexError: If attempting to pop from an empty stack
            
        Time Complexity: O(1) - Constant time
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        
        value = self.head.value  # Save the value to return
        self.head = self.head.next  # Move head to the next node
        self._size -= 1  # Decrement size counter
        return value
    
    def peek(self):
        """
        Return the top element from the stack without removing it.
        
        Implementation:
        1. Check if the stack is empty
        2. Return the value of the head node
        
        Returns:
            The value at the top of the stack
            
        Raises:
            IndexError: If the stack is empty
            
        Time Complexity: O(1) - Constant time
        """
        if self.is_empty():
            raise IndexError("Cannot peek an empty stack")
        return self.head.value
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Implementation:
        Check if the head pointer is None or use the size counter
        
        Returns:
            True if the stack is empty, False otherwise
            
        Time Complexity: O(1) - Constant time
        """
        return self.head is None  # Or could use: return self._size == 0
    
    def size(self):
        """
        Return the number of elements in the stack.
        
        Implementation:
        Return the value of the size counter
        
        Returns:
            The number of elements in the stack
            
        Time Complexity: O(1) - Constant time
        """
        return self._size
    
    def clear(self):
        """
        Remove all elements from the stack.
        
        Implementation:
        Reset the head pointer to None and the size counter to 0
        
        Time Complexity: O(1) - Constant time
        (The garbage collector will handle freeing the memory of unreferenced nodes)
        """
        self.head = None
        self._size = 0
    
    def __str__(self):
        """
        Return a string representation of the stack.
        
        Implementation:
        1. Start at the head
        2. Traverse the linked list, collecting all values
        3. Format and return the values as a string
        
        Returns:
            A string showing stack elements from top to bottom
            
        Time Complexity: O(n) - Linear in the size of the stack
        """
        if self.is_empty():
            return "Stack: []"
            
        current = self.head
        elements = []
        
        # Traverse the linked list to collect values
        while current is not None:
            elements.append(str(current.value))
            current = current.next
            
        # Format as a string with top of stack first
        return "Stack: [" + " (top) -> ".join(elements) + "]"
    
    def __repr__(self):
        """
        Return a technical representation of the stack.
        
        Returns:
            A string with information about the stack state
            
        Time Complexity: O(1) - Constant time
        """
        return f"Stack(size={self._size})"


# Example usage
if __name__ == "__main__":
    stack = Stack()
    
    # Push elements onto the stack
    stack.push("apple")
    stack.push("banana")
    stack.push("cherry")
    
    print(stack)  # Stack: [cherry (top) -> banana (top) -> apple]
    
    # Peek at the top element
    top_element = stack.peek()
    print(f"Top element: {top_element}")  # Top element: cherry
    
    # Pop elements from the stack
    popped = stack.pop()
    print(f"Popped: {popped}")  # Popped: cherry
    print(stack)  # Stack: [banana (top) -> apple]
    
    # Check size and emptiness
    print(f"Size: {stack.size()}")  # Size: 2
    print(f"Is empty? {stack.is_empty()}")  # Is empty? False
    
    # Clear the stack
    stack.clear()
    print(f"After clearing - Is empty? {stack.is_empty()}")  # After clearing - Is empty? True
    
    # Test error handling
    try:
        stack.pop()
    except IndexError as e:
        print(f"Error: {e}")  # Error: Cannot pop from an empty stack