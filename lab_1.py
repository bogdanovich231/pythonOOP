import pytest

def reverseWords(string):
    words = string.split()
    reversed_words = [word[::-1] for word in words]
    palindrome = " ".join(reversed_words)
    return palindrome

def isPalindrome(string):
    return string == string[::-1]

input_string = input("Enter the line: ")

palindrome_string = reverseWords(input_string)

if isPalindrome(input_string):
    print("The entered string is a palindrome")
else:
    print("The entered string is not a palindrome")

print("Palindrome:", palindrome_string)

def testReversePalindrome():
    assert reverseWords("hello world") == "olleh dlrow"
    assert reverseWords("python is awesome") == "nohtyp si emosewa"
    assert reverseWords("") == ""

def testIsPalindrome():
    assert isPalindrome("madam") == True
    assert isPalindrome("hello") == False
    assert isPalindrome("") == True

pytest.main()