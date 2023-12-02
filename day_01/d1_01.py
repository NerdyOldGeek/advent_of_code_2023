cal_vals = []
num_digits = '123456789'

def get_digits(line):
    digits = []
    for char in line:
        if char in num_digits:
            digits.append(char)
    return digits

with open('./day_01/input') as file:
    file.seek(0)
    list_of_lines = file.readlines()
    for line in list_of_lines:
        data = get_digits(line)
        digits = int(data[0] + data[-1])
        cal_vals.append(digits)

    print(sum(cal_vals)) 
