def is_palidrome(item) -> bool:
    return str(item)[::-1] == str(item)
#print(is_palidrome('itemeti'))

def recursive_palindrome(array,i = 0) -> bool:
    if not array or i == len(array):
        return ""
    else:
        return f"{array[i]}:{is_palidrome(array[i])}\n{recursive_palindrome(array,i+1)}"
ar=[132,5000,0000,1111,'madam','not madam']
print(recursive_palindrome(ar))