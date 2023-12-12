
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str :rtype: bool
        """
        # alle buchstaben in set schreiben

        lettersInS = []
        for a in s:
            lettersInS.append(a)

        lettersInT = []
        for b in t:
            lettersInT.append(b)

        lettersInS.sort()
        lettersInT.sort()

        if(lettersInT != lettersInS): return False

        return True
    


sol = Solution()

print(sol.isAnagram("aa", "a"))
    

     
