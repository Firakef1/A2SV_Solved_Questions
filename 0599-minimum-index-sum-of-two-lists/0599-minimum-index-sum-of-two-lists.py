class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        least = float("inf")
        arr = []
        set_list2 = set(list2)

        for i in range(len(list1)):
            string = list1[i]
            if string not in set_list2:
                continue
            
            for j in range(len(list2)):
                if string == list2[j]:
                    if i+j > least:
                        break
                    if i+j < least:
                        least = i+j
                        arr.clear()
                        arr.append(string)

                    elif i+j == least:
                        arr.append(string)

        return arr
        