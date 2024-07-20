

def isPalindrome(s):
    # Base Case
    # Smallest subset problem

    if (len(s) == 0 or len(s) == 1): return True
    if(s[0] == s[-1]):
        return isPalindrome(s[1:-1])
    return False


if __name__ == "__main__":
    word = "racecar"
    if(isPalindrome(word)):
        print("is Palindrome")
    else:
        print("NOT a Palindrome")
