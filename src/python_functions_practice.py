def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name(month_num):
    month_lookup = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return month_lookup[month_num]

def number_to_short_month_name(month_num):
    month_lookup = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    return month_lookup[month_num]

def volume_of_cube(edge_length):
    return edge_length * edge_length * edge_length

def reverse_string(string):
    return string[::-1]

def fahrenheit_to_celcius(temp_f):
    return (temp_f - 32) * 5/9

def palindrome_check(string):
    string_reversed = reverse_string(string)
    if string_reversed == string:
        print("That's a Palindrome")
    else:
        print("No Palindromes here")

palindrome_check("racecar")

one_to_onehundred = list(range(3, 101))


def prime_nums(range):
    prime_num_list = []
    for num in range:
        if num % 2 == 0:
            pass
        elif num % 3 == 0 and num > 3:
            pass
        elif num % 5 == 0 and num > 5:
            pass
        elif num % 7 == 0 and num > 7:
            pass
        elif num % 11 == 0 and num > 11:
            pass
        else:
            prime_num_list.append(num)
    print(prime_num_list)

prime_nums(one_to_onehundred)
