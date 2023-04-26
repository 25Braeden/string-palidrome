string = input("Enter a string: ")

# reverse the input string
rev_string = string[::-1]

# check if the string is equal to its reverse
if string == rev_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
