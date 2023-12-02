cal_vals = []
num_digits = '0123456789'
num_words = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

def get_digits(line):
    found = {}
    for char in line:
        if char in num_digits:
            loc = line.index(char)
            found[loc] = char
            if line.count(char) > 1:
                loc = line.rindex(char)
                found[loc] = char
    for num in num_words:
        if num in line:
            loc = line.index(num)
            found[loc] = num
            if line.count(num) > 1:
                loc = line.rindex(num)
                found[loc] = num
    return found

def get_first_last_numbers(d):
    digits = []
    low = min(d.keys())
    high = max(d.keys())
    if d[low] in num_words:
        digits.append(num_words.index(d[low]))
    else:
        digits.append(num_digits.index(d[low]))
    
    if d[high] in num_words:
        digits.append(num_words.index(d[high]))
    else:
        digits.append(num_digits.index(d[high]))

    return digits
    

with open('input') as file:
    list_of_lines = file.readlines()
    for line in list_of_lines:
        data = get_digits(line)
        digits = get_first_last_numbers(data)
        digits = int(str(digits[0]) + str(digits[-1]))

        cal_vals.append(digits)

    print(sum(cal_vals)) 
