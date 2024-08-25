from itertools import zip_longest
class Solution(object):
    def mergeAlternately(self, word1, word2):
        str=""
        for w1,w2 in zip_longest(word1,word2,fillvalue=""):
            str+=w1+w2            
        print(str)
Solution().mergeAlternately("Aravind","Jinnu")