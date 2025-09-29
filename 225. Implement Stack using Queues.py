----------------------------------------------------------------- Implement Stack using Queues---------------------------------------------------------------------------------------------
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.

################################################################################### Solution (First approch) ##################################################################################
class MyStack:

    def __init__(self):
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> int:
        if not self.empty():
            return self.items.pop()
        else:
            return "Stack is empty"
    def top(self) -> int:
        if not self.empty():
            return self.items[-1]
        else:
            return "Stack is empty"
    def empty(self) -> bool:
        return len(self.items)== 0

######################################################################## Optimal Solution #################################################################################        
from queue import Queue
class MyStack:

    def __init__(self):
        self.q=Queue()

    def push(self, x: int) -> None:
        s=self.q.qsize()
        self.q.put(x)
        for _ in range(s):
            self.q.put(self.q.get())

    def pop(self) -> int:
        if not self.empty():
            return self.q.get()
        else:
            return "Stack is empty"
    def top(self) -> int:
        if not self.empty():
            return self.q.queue[0]
        else:
            return "Stack is empty"
    def empty(self) -> bool:
        return self.q.qsize()== 0
