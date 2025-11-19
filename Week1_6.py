def max_product(lst):
    if len(lst) < 2:
        return "Invalid"
    elif lst[1] == 0:
        return "Invalid"
    lst.sort()
    return max(lst[-1] * lst[-2], lst[0] * lst[1])

value = input().strip()
try:
    value = value.strip("[]")  
    value = value.replace(",", " ") 
    value = value.split() 
    value = [int(x) for x in value]  
    output = max_product(value)
except ValueError:
    output = "Invalid" 

print(output)