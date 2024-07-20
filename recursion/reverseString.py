# given a sorted array A[0 ... n]
# insert number x such that the result is also sorted

def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]


if __name__ == "__main__":
    word = "hello"
    print(reverse(word))