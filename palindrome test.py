def isPalindrome(x):
    x = str(x)
    original_list = list(x)
    reverse_list = original_list[::-1]

    # zip compares each character from start to end and from end to start simultaneously
    for i, j in zip(original_list, reverse_list):
        if i != j:
            return False
    
    return True

print(isPalindrome(202))
