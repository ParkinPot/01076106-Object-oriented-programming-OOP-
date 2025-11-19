def sort(value):
    numbers = list(map(int, value.split()))

    length_numbers = len(numbers)

    if length_numbers > 10 or length_numbers < 2:
        return "Invalid"
    else:
        numbers.sort()
        if numbers[0] == 0:
            for i in range(1, len(numbers)):
                if numbers[i] != 0:
                    numbers[0], numbers[i] = numbers[i], numbers[0]
                    break
            return ''.join(map(str, numbers))
        elif numbers[0] < 0:
            return "Invalid"
        
        return ''.join(map(str, numbers))

value = input()
try:
    output = sort(value)
    print(output)
except:
    print("Invalid")
