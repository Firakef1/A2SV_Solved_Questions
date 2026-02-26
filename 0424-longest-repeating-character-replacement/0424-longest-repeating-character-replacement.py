class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        in_s = set(s)
        lis = list(in_s)
        _max = 0
        for i in lis:
            one = 0
            two = one
            counter = 0

            while two < len(s):
                if s[two] != i:
                    counter += 1
                
                if counter > k:
                    _max = max(_max, two - one)
                    while counter > k and one <= two:
                        if s[one] != i:
                            counter -= 1
                        one += 1
                
                two += 1
            _max = max(_max, two-one)
        return _max