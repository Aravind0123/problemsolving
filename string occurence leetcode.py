class Solution(object):
    def strStr(self, haystack, needle):
        if(needle in haystack):
            return 0
        else:
            return -1
haystack="sadbutsad"
needle='sad'
value=Solution().strStr(haystack,needle)
        