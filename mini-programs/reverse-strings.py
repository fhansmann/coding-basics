# 1 Slicing

original_string = "ABCDE"
reversed_string = original_string[::-1]print("Original String : ", original_string)
print("Reversed String : ", reversed_string)# Output
# Original String :  ABCDE
# Reversed String :  EDCBA


# 2 Appending characters in reverse order using a loop

def reverse_string_loop(original_string):
    reversed_string = ""
    for a in original_string:
        # appending characters in reverse
        reversed_string = a + reversed_string
    return reversed_string

original_string = "ABCDE"
print("Original String : ", original_string)
print("Reversed String : ", reverse_string_loop(original_string))


# 3 Using reversed() iterator


ef reverse_string_iterator(original_string):

    reversed_iterator = reversed(original_string)
    reversed_string = "".join(reversed_iterator)

    return reversed_string

original_string = "ABCDE"

print("Original String1 : ", original_string)
print("Reversed String : ", reverse_string_iterator(original_string))


# 4 Using the built-in reverse() function

def reverse_string(original_string):

    temp_list = list(original_string)
    temp_list.reverse()
    reversed_string = "".join(temp_list)

    return reversed_string

original_string = "ABCDE"
print("Original String : ", original_string)
print("Reversed String : ", reverse_string(original_string))

# 5 Recursion

def recursion_reverse(s):
    # Base Case
    if(len(s)==1):
        return s
    else:
        return recursion_reverse(s[1:]) + s[0]

original_string = "ABCDE"
print("Original String : ", original_string)
print("Reversed String : ", recursion_reverse(original_string))
