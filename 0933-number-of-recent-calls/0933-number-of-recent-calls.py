class RecentCounter:
    
    def __init__(self):
        self.last_in = deque()
        

    def ping(self, t: int) -> int:
        last_in = self.last_in

        while last_in and t - last_in[0] > 3000:
            last_in.popleft()
        last_in.append(t)

        return len(last_in)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)