class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        newx=''
        for i in str(x):
            newx = i+newx
        if newx == str(x):
            return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()

    # Test cases
    print(sol.isPalindrome(121))   # Expected Output: True
    print(sol.isPalindrome(-121))  # Expected Output: False
    print(sol.isPalindrome(10))