#-------------------------------------------------------------------------------
# Purpose:  Exemplify Stack Data Structure
#-------------------------------------------------------------------------------


class Stack():
    def __init__(self,data=None):
        if data is None:
            print("Cannot add null value")
            return

        self.data = data
        self.next = None


    def pop(self): #remove top item from stack
        if not self.isEmpty():
            popped_item = self.data
            self.data = self.next
            return popped_item

    def push(self,data=None): #add item to the top of stack
        temp_node = Stack(data)
        temp_node.next = self
        self = temp_node

    def peek(self): #Return the top of the stack
        return self.data

    def isEmpty(self): #Return true if and only if stack is empty
        return self.data == None


if __name__ == '__main__':
    sample_stack = Stack(4)
    print(sample_stack.peek())
    sample_stack.push()
    print(sample_stack.peek())

