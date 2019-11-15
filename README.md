# Data Structures

Part of being a great problem-solver is knowing what data structure to use when handling data. This repository will contain commonly used data structures and sample problems that illustrate use-cases.

# Files
```dataStructures
├── README
├── stack
│   ├── stack.py
```
## Stack

Stacks use last-in first-out (LIFO) ordering. 
To access data in a stack, we use the following operations:
+ pop() : remove top item from stack
+ push(*x*): add item *x* to the top of the stack
+ peek(): return the top of the stack
+ isEmpty(): return True if and only if the stack is empty

Adding or removing an item from a stack takes constant time. However, stacks do not offer constant time access to the *n-th* element.
A sample implementation of a stack can be found in [*stack.py*](https://github.com/Mokeira/dataStructures/blob/master/stack/stack.py)

### Next Steps
+ Add test file for stack.py
+ Add sample Stack problems 
+ implement queues and related sample problems
+ implement linked list and related sample problems
+ implement hash table and related sample problems
+ implement graph and related sample problems
+ implement trees  and related sample problems
