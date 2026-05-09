def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """

        current = ""
        lst_palindrome = []
        index = 0
        length = len(s)

        while length :
            for i in (s):
                current+=i
                if current == current[::-1]:

                    lst_palindrome.append(current)
            current = ""
            
            s = s[1:]
            length-=1
        if not lst_palindrome :
            return ""
        else:
            return max(lst_palindrome , key = len)
    
    
a = "abbcccba"

print(longestPalindrome(a))