class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = {}
        for i, n in enumerate(order):
            order_dict[n] = i

        def order(x):
            if x in order_dict:
                return order_dict[x]
            
            return -1
        
        s = sorted(s, key = lambda x: order(x))

        s = "".join(s)
        return s

        