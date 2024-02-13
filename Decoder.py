# you can give a number to this function and it will give you <a,<b,c>> of that number
# so you can decode each line's code with the help of this function

def decode_line_number(line_number):
    a = 0
    while (line_number + 1) % (2**(a+1)) == 0:
        a += 1

    d = ((line_number + 1) // (2**a) - 1) // 2
    b, c = 0, d

    while (c + 1) % (2**(b+1)) == 0:
        b += 1

    c = ((d + 1) // (2**b) - 1) // 2
    return a, b, c

# this function has c of <a,<b,c>> function which represents variable of that line
# and will return correct symbol + 0:y 1:xi 2:zj + i or j because I need them to
# initial snapshot in the universal program question
 
def variable_mapping(c):
    if c == 0:
        return 'y', 0 , 0
    elif c % 2 == 1:
        return f'x{(c + 1) // 2}', 1 , (c + 1) // 2
    else:
        return f'z{c // 2}', 2 , c // 2

# this function is the base function of our program it gets line numbers and will lead
# them to get each line's correct syntax
# it also returns maximum number of variables this program need and <a,<b,c>> for each line
# because we need them for universal program question
# I will describe it more in the function.
def line_numbers_to_davis_language(line_numbers):
    label_order = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lines = []
    max_z= 0
    max_x= 0
    program_codes= []

    for line_number in line_numbers:
        # calculate <a,<b,c>> and it will add it to program_codes
        # because I need it in universal program
        a, b, c = decode_line_number(line_number)
        program_codes.append({'a': a, 'b': b, 'c': c})

        variable, check, new_max = variable_mapping(c)
        if(check == 1):
            if(new_max>max_x):
                max_x= new_max
        elif(check==2):
            if(new_max>max_z):
                max_z= new_max
        # save label of this line!
        label = ""
        if a != 0:
            label_index = a - 1
            label_cycle = label_index // 26
            label_char = label_order[label_index % 26]
            label = f"[{label_char}{label_cycle + 1}]"
        operation = ""
        # check what kind of operation we have based on number of b
        if b == 0:
            operation = f"{variable} <- {variable}"
        elif b == 1:
            operation = f"{variable} <- {variable} + 1"
        elif b == 2:
            operation = f"{variable} <-{variable} - 1"
        else:
            jump_label_index = b - 3
            jump_label_cycle = jump_label_index // 26
            jump_label_char = label_order[jump_label_index % 26]
            jump_label = f"[{jump_label_char}{jump_label_cycle + 1}]"
            operation = f"IF {variable} != 0 GOTO {jump_label[1:-1]}"
        
        # saving correct syntax of each line
        line = f"{label} {operation}".strip()
        lines.append(line)
    
    return lines, max(2*max_z, 2*max_x-1), program_codes

def main():
    # input_str = input("Please give me line numbers separated by space: ")
    input_str = input()
    line_numbers = [int(num) for num in input_str.split()]
    lines, max, codes = line_numbers_to_davis_language(line_numbers)
    
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
