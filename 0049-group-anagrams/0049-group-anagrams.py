class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        new_dict = {}

        for i in range(len(strs)):
            word = tuple(sorted(strs[i]))

            if not word in new_dict:
                new_dict[word] = [i]
            else:
                new_dict[word].append(i)

        return_arr =[]

        for key in new_dict:
            arr = new_dict[key]
            anagram = []

            for i in arr:
                anagram.append(strs[i])

            return_arr.append(anagram)

        return return_arr