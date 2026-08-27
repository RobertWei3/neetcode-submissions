# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

class MinStack:

    def __init__(self):
        self.stack  = []
        self.MinStack = []

        # new_node = Node(val)
        # self.top = None
        # self.height = 1

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.MinStack[-1] if self.MinStack else val)
        self.MinStack.append(val)


        # push_node = Node(val)

        # if self.height == 0:
        #     self.top = push_node
            
        # else:
        #     push_node.next = self.top
        #     self.top = push_node

        # self.height += 1

    def pop(self) -> None:
        self.stack.pop()
        self.MinStack.pop()

        # if self.height == 0:
        #     return "null"
        # temp = self.head
        # self.top = self.top.next
        # temp.next = None
        
        # self.height -= 1

        # return temp

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.MinStack[-1]
        
