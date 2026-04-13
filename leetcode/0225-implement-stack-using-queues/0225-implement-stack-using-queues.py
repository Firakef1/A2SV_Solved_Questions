class MyStack:

    def __init__(self):
        self.pop_first = deque()
        self.push_first = deque()
        

    def push(self, x: int) -> None:
        self.push_first.append(x)
        self.pop_first = self.push_first.copy()
        self.pop_first.reverse()

        

    def pop(self) -> int:
        element = self.pop_first.popleft()
        self.push_first = self.pop_first.copy()
        self.push_first.reverse()

        return element
        

    def top(self) -> int:

        return self.pop_first[0]

        

    def empty(self) -> bool:

        return False if len(self.pop_first) else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()