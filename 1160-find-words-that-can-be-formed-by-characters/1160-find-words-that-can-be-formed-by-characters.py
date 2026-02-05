class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
    
        total = 0

        for word in words:
            counter = Counter(chars)
            letters = set(chars)

            for letter in word:
                
                if letter not in letters or word.count(letter) > counter[letter]:
                    break
            else:
                total += len(word)

        return total

                








        # for word in words:
        #     for i in word:
        #         if i not in letters:
        #             break

        #     else:
                

        #         for i in word:
        #             if not counter[i]:
        #                 break
        #             counter[i] -= 1
        #             if counter[i] == 0:
        #                 del counter[i]
        #                 letters.discard(i)

        #         else:
        #             total += len(word)

        # return total

        