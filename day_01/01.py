

cal_vals = []
num_digits = '123456789'

def get_digits(line):
    digits = []
    for char in line:
        if char in num_digits:
            digits.append(char)
    return digits

with open('input') as file:
    file.seek(0)
    list_of_lines = file.readlines()
    print(len(list_of_lines))
    input()
    for line in list_of_lines:
        print(line.strip())
        data = get_digits(line)
        print(data)
        digits = int(data[0] + data[-1])
        print(digits)
        cal_vals.append(digits)

    print(sum(cal_vals)) 
