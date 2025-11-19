## ------------------------------------------------------------------
## START: Week1_1.py - The Pattern Sum Problem
## ------------------------------------------------------------------

def sum(a):
    """
    Calculates the sum: a + aa + aaa + aaaa, where aa, aaa, and aaaa 
    are concatenations of the string representation of a.
    Example: if a = 5, returns 5 + 55 + 555 + 5555 = 6170.
    """
    a = int(a)
    return a + int(str(a) * 2) + int(str(a) * 3) + int(str(a) * 4)

a = input()
try:
    output = sum(a)
    print(output)
except ValueError:
    # Handle cases where input 'a' is not an integer
    # The original file does not explicitly handle this, 
    # but a 'try-except' block is good practice.
    print("Invalid input for sum calculation.")

## ------------------------------------------------------------------
## END: Week1_1.py
## ------------------------------------------------------------------


## ------------------------------------------------------------------
## START: Week1_2.py - Largest Palindrome Product
## ------------------------------------------------------------------

def largest_palindrome_product(num_digits):
    """
    Finds the largest palindrome made from the product of two n-digit numbers.
    """
    if num_digits <= 1:
        return "Invalid"
    
    # Largest n-digit number (e.g., 99 for num_digits=2)
    max_num = 10**num_digits - 1
    # Smallest n-digit number (e.g., 10 for num_digits=2)
    min_num = 10**(num_digits - 1)
    max_palindrome = 0

    # Iterate downwards from the largest n-digit number
    for i in range(max_num, min_num - 1, -1):
        for j in range(i, min_num - 1, -1):
            product = i * j
            
            # Optimization: If the current product is already smaller 
            # than the largest found palindrome, stop checking smaller j values
            if product <= max_palindrome:
                break  
            
            # Check if the product is a palindrome
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

## ------------------------------------------------------------------
## END: Week1_2.py
## ------------------------------------------------------------------


## ------------------------------------------------------------------
## START: Week1_3.py - Parking Time and Fee Calculation
## ------------------------------------------------------------------

def check_time(Inmin, Outmin, Inhr, Outhr):
    """
    Calculates the parking fee based on entry and exit times.
    Inputs are assumed to be strings of hours and minutes (In/Out).
    """
    Inhr = int(Inhr)
    Inmin = int(Inmin)
    Outhr = int(Outhr)
    Outmin = int(Outmin)

    # Handle 24:xx time by converting it to 00:xx for continuous time calculation
    if Outhr == 24:
        Outhr = 0

    # Convert times to total minutes from the start of the day
    a = Inhr * 60 + Inmin  # Entry time in minutes
    b = Outhr * 60 + Outmin # Exit time in minutes

    time_diff = b - a

    # The logic below implements the tiered fee structure
    if 0 < time_diff <= 15:
        return("0")
    elif a < 0 or Inmin < 0 or Outmin < 0 or Inhr < 0 or Outhr < 0:
        # Added check for negative time components
        return("Invalid")
    elif 15 < time_diff <= 180:
        # Up to 3 hours (180 min)
        if 0 < Outmin - Inmin <= 60:
            Hr = (Outhr - Inhr) + 1 # Bill for an extra hour if minute difference is positive
            return(Hr * 10)
        else:
            Hr = Outhr - Inhr
            return(Hr * 10)
    elif 180 < time_diff < 360:
        # 3 to 6 hours (360 min)
        Hr = (Outhr - Inhr - 3)
        if 0 < Outmin - Inmin <= 60:
            Hr = Hr + 1
            return((Hr * 20) + 30) # Base fee of 30 plus 20 per hour after the first 3
        else:
            return((Hr * 20) + 30)
    elif time_diff >= 360:
        return("200") # Capped fee
    else:
        # Handles time_diff <= 0 or other invalid scenarios
        return("Invalid")

try:
    # Expects four space-separated inputs: Inhr Inmin Outhr Outmin
    Inhr, Inmin, Outhr, Outmin = input("").split()
    output = check_time(Inmin, Outmin, Inhr, Outhr)
    print(output)
except ValueError:
    # Handles incorrect number of inputs or non-integer inputs
    print("Invalid")

## ------------------------------------------------------------------
## END: Week1_3.py
## ------------------------------------------------------------------


## ------------------------------------------------------------------
## START: Week1_5.py - Custom Integer Array Sorting and Concatenation
## ------------------------------------------------------------------

def sort(value):
    """
    Sorts a list of space-separated integers, applying a custom swap 
    rule if the smallest number is zero, and returns the result as a 
    concatenated string.
    """
    numbers = list(map(int, value.split()))

    length_numbers = len(numbers)

    # Validation: Length must be between 2 and 10
    if length_numbers > 10 or length_numbers < 2:
        return "Invalid"
    else:
        numbers.sort()
        
        # Validation: Check for negative numbers after sorting
        if numbers[0] < 0:
            return "Invalid"
            
        # Custom Rule: If the smallest number is 0
        if numbers[0] == 0:
            # Find the first non-zero number and swap it with the leading 0
            for i in range(1, len(numbers)):
                if numbers[i] != 0:
                    numbers[0], numbers[i] = numbers[i], numbers[0]
                    break
            # Return the concatenated string
            return ''.join(map(str, numbers))
        
        # If no leading zero, return the concatenated sorted string
        return ''.join(map(str, numbers))

value = input()
try:
    output = sort(value)
    print(output)
except:
    print("Invalid")

## ------------------------------------------------------------------
## END: Week1_5.py
## ------------------------------------------------------------------


## ------------------------------------------------------------------
## START: Week1_6.py - Max Product of Two Numbers
## ------------------------------------------------------------------

def max_product(lst):
    """
    Finds the maximum product of any two numbers in the list.
    """
    if len(lst) < 2:
        return "Invalid"
    
    # Check for the second smallest element being zero (potential specific constraint)
    # The list is sorted immediately below, so lst[1] will be the second smallest number.
    lst.sort()
    
    if lst[1] == 0:
        return "Invalid"
    
    # The max product is either the product of the two largest numbers (lst[-1] * lst[-2]) 
    # or the product of the two smallest numbers (lst[0] * lst[1], used for two large negatives).
    return max(lst[-1] * lst[-2], lst[0] * lst[1])

value = input().strip()
try:
    # Input processing to handle list-like string input (e.g., "[1, 2, 3]")
    value = value.strip("[]")  
    value = value.replace(",", " ") 
    value = value.split() 
    value = [int(x) for x in value]  
    output = max_product(value)
except ValueError:
    output = "Invalid" 

print(output)

## ------------------------------------------------------------------
## END: Week1_6.py
## ------------------------------------------------------------------
