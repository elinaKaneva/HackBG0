def isPalindrome(string):
    return string == string[::-1]


def findPalindromes(text):
    flag = 0

    for x in range(len(text)):
        rotatedText = text[x:] + text[:x]
        if isPalindrome(rotatedText):
            print(rotatedText)
            flag = 1

    if flag == 0:
        print("NONE")
print("Input: labalaa")
findPalindromes("labalaa")
print("Input: akawwaka")
findPalindromes("akawwaka")
print("Input: shakira")
findPalindromes("shakira")
print("Input: azobi4amma4iboza")
findPalindromes("azobi4amma4iboza")
