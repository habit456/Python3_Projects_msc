from time import sleep

# functions - start
def number_adder():
    user_input = input('Give me a whole number. When you are done, write "done".')
    if user_input.isdigit():
        return {"value": int(user_input), "done": False}
    elif user_input.lower() == "done":
        return {"done": True}
    else:
        print("I don't understand")
        return number_adder()


def map_exponent(arr):
    ui = input("\nWhat should the exponent be for each number? Please choose between 0 and 10")
    if ui.isdigit():
        if 0 <= int(ui) <= 10:
            return list(map(lambda a: a ** int(ui), arr))
        else:
            print("\nThat is not a valid input")
            return map_exponent(arr)
    else:
        print("\nI don't understand")
        return map_exponent(arr)


def map_multiply(arr):
    ui = input("\nWhat should each number be multiplied by?")
    if ui.isdigit():
        return list(map(lambda a: a * int(ui), arr))
    else:
        print("\nI don't understand")
        return map_multiply(arr)


def each_num(arr):
    user_input = input("\nChoose: "
                       "\n1: Multiply each number in your array exponentially "
                       "\n2: Multiply each number in your array by a number "
                       "\n3: Do nothing")
    if user_input.isdigit():
        if int(user_input) == 1:
            return map_exponent(arr)
        elif int(user_input) == 2:
            return map_multiply(arr)
        elif int(user_input) == 3:
            return arr
        else:
            print("That isn't a choice.")
            return each_num(arr)
    else:
        print("I don't understand")
        return each_num(arr)


def yes_or_no():
    ui = input("\nWould you like to make another choice? y/n?")
    if ui.lower() == "yes" or ui.lower() == "y":
        return True
    elif ui.lower() == "no" or ui.lower() == "n":
        return False
    else:
        print("I don't understand")
        return yes_or_no()


def user_interface(section = 0, array = []):
    # add a number, when you are done, write done
    user_array = array.copy()
    if section == 0:
        na_input = number_adder()
        if na_input["done"]:
            return user_interface(1, user_array)
        else:
            user_array.append(na_input["value"])
            print("Your array: ", user_array, "\n")
            return user_interface(0, user_array)
    elif section == 1:
        user_array = each_num(user_array)
        print(user_array)
        choice = yes_or_no()
        if choice:
            user_interface(1, user_array)
            return user_array
        else:
            return user_array


# functions - end

print("Hello, welcome to array maker 1.0 \n")
sleep(1)
print("Let's start making our array! \n")
user_array_final = user_interface()
print("\nYour array is: ", user_array_final)
print("\nThank you for using array maker 1.0!")
