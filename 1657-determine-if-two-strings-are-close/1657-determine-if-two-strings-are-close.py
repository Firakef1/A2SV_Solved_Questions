class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if set(word1) != set(word2):
            return False
        
        count_one = Counter(word1)
        count_two = Counter(word2)

        freq_one = sorted(list(count_one.values()))
        freq_two = sorted(list(count_two.values()))
        if freq_one != freq_two:
            return False

        return True