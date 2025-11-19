def largest_palindrome_product(num_digits):
    if num_digits <= 1:
        return "Invalid"
    
    max_num = 10**num_digits - 1
    min_num = 10**(num_digits - 1)
    max_palindrome = 0

    for i in range(max_num, min_num - 1, -1):
        for j in range(i, min_num - 1, -1):
            product = i * j
            if product <= max_palindrome:
                break  
            if str(product) == str(product)[::-1]:  
                max_palindrome = product
    
    return max_palindrome if max_palindrome > 0 else 0

value = input()

try:
    value = int(value)
    if value <= 0:
        print("Invalid")
    else:
        output = largest_palindrome_product(value)
        print(output)
except ValueError:
    print("Invalid")
