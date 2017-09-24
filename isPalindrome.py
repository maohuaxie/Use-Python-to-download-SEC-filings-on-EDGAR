# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 17:17:39 2017

@author: maohuaxie
"""
def isPalindrome(s):
    return isPalindromeHelper(s, 0, len(s) - 1)

def isPalindromeHelper(s, low, high):
    if high <= low: # Base case
      return True
    elif s[low] != s[high]: # Base case
      return False
    else:
      return isPalindromeHelper(s, low + 1, high - 1)

def main():
    print("Is moon a palindrome?", isPalindrome("moon"))
    print("Is noon a palindrome?", isPalindrome("noon"))
    print("Is a a palindrome?", isPalindrome("a"))
    print("Is aba a palindrome?", isPalindrome("aba"))
    print("Is ab a palindrome?", isPalindrome("ab"))

main() # Call the main function


# Time:  O(n)
# Space: O(1)
#
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# 
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
# 
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
# 
# For the purpose of this problem, we define empty string as valid palindrome.
#

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1
        return True

if __name__ == "__main__":
    print Solution().isPalindrome("A man, a plan, a canal: Panama")

