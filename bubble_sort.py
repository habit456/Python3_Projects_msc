# Imported libraries
import random as r
import time as t
import colorama as col


# Functions


# little helper function that converts an array of numbers into a string
def arr_to_string(arr_nums):
    arr_str = ""
    for n in arr_nums:
        arr_str += str(n) + " "
    return arr_str


# color(number, number, array, boolean)
# slices array from index1(inclusive) - index2(inclusive) from whole_arr.
# If switch = 1, pair is red. If switch = 0, pair is blue
def color(index1, index2, whole_arr, switch):
    num1 = str(whole_arr[index1])
    num2 = str(whole_arr[index2])

    if switch:
        pair = col.Fore.LIGHTRED_EX + num1 + " " + num2
    else:
        pair = col.Fore.LIGHTBLUE_EX + num1 + " " + num2

    if index1 == 0:
        rest_of_arr = whole_arr[2:]
        str_rest = ""
        for n in rest_of_arr:
            str_rest += str(n) + " "
        print(pair + " " + col.Fore.RESET + str_rest)
    else:
        arr_slice_1 = whole_arr[0:index1]
        arr_slice_2 = whole_arr[index2+1:]
        str_slice_1 = ""
        str_slice_2 = ""
        for n in arr_slice_1:
            str_slice_1 += str(n) + " "
        for n in arr_slice_2:
            str_slice_2 += str(n) + " "
        print(str_slice_1 + pair + " " + col.Fore.RESET + str_slice_2)


def bubble_sort(arr_sort, speed):
    input("\nI will now attempt to sort your array. Press \"Enter\" when ready...")
    print()
    arr0 = arr_sort.copy()
    i = 0
    print(arr_to_string(arr0))
    t.sleep(speed)

    # i = how many swaps there aren't. So if i < len(arr0) - 1, it hasn't been fully sorted
    while i < len(arr0) - 1:
        i = 0

        # loops through array in pairs, which is why condition is (n < arr0.length - 1)
        for n in range(0, len(arr0) - 1):
            num1 = arr0[n]
            num2 = arr0[n + 1]

            # if 1st value in the pair is greater than 2nd value, swap
            if num1 - num2 > 0:
                color(n, n + 1, arr0, 1)
                t.sleep(speed)
                arr0[n] = num2
                arr0[n + 1] = num1
                color(n, n+1, arr0, 1)
                t.sleep(speed)
            # if 1st value in pair is not greater than 2nd value, add 1 to i
            else:
                i += 1
                color(n, n+1, arr0, 0)
                t.sleep(speed)

    print('\nFinished! Your newly sorted array is: \n%s' % col.Fore.MAGENTA + str(arr0))
    return arr0


# user generates a random array
# for arr_sort argument in bubble_sort function
def user_interface():
    input('\nWelcome to Array Sort 1.0! Press "Enter" to continue...')
    count = input('\nWe\'re going to generate a random array of numbers.'
                  '\nHow many numbers should be in the array? Please choose between 5 and 25: ')
    num_max = input('\nWhat is the maximum number each number in the array should be? '
                    '\nIn other words, no number will be greater than this number: ')
    num_min = input('\nWhat is the minimum number each number in the array should be?'
                    '\nIn other words, no number will be less than this number: ')
    random_array = [r.randint(int(num_min), int(num_max)) for a in range(0, int(count))]
    print('\nYour array is: \n%s' % col.Fore.MAGENTA + str(random_array) + col.Fore.RESET)
    return random_array


# for speed argument in bubble_sort function
def sorting_speed():
    user_speed = input("\nPlease choose the speed at which you would like to see your array sorted: "
                       "\n1. Slow"
                       "\n2. Normal"
                       "\n3. Instant")
    if user_speed == "1" or user_speed.lower() == "slow":
        return .5
    elif user_speed == "2" or user_speed.lower() == "normal":
        return .3
    elif user_speed == "3" or user_speed.lower() == "instant":
        return 0
    else:
        print("\nI don't understand")
        return sorting_speed()


# Function calls
user_array = user_interface()
speed_choice = sorting_speed()
bubble_sort(user_array, speed_choice)


# End
print(col.Fore.RESET + "\nThank you for using Array Sort 1.0!")
