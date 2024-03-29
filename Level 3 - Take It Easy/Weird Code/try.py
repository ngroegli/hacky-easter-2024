# This function expects user input for the flag
def get_flag_input():
    return input('enter the flag: ')

# This function checks if the inputted flag matches a specific format
def check_flag(flag):
    if flag == ('he2024{%s%s%s%s%s}' % (flag, '_', flag, '_', flag)):
        print('Flag is correct!')
    else:
        print('Flag is incorrect!')

# Decoded punycode string
flag = get_flag_input()

# Check the flag format
check_flag(flag)
