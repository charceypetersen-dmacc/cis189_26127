def print_hi():
    """prints the string hi"""
    print("hi")

print_hi()

def calculate_square(number):
    """squares the provided number"""
    print(number)
    number = number**2
    print(number)


calculate_square(5)
calculate_square(4)
calculate_square(2)
calculate_square(3854903)
calculate_square(6859)

def multiply_str(message, number):
    """multiply the provided message by the provided number"""
    output_str = message * number
    print(output_str)

multiply_str("hi", 8)

def calculate_square(number):
    """squares the provided number"""
    print(number)
    number = number**2
    print(number)


# calculate_square(5)
# calculate_square(4)
# calculate_square(2)
# calculate_square(3854903)
# calculate_square(6859)

# TODO: Add try except
def print_user_info(name, job, age):
    """finds user age age genre and prints info"""
    age_genre = None
    if age < 2:
        age_genre = "baby"
    elif age < 4:
        age_genre = "toddler"
    elif age < 13:
        age_genre = "kid"
    elif age < 20:
        # TODO come back!
        age = "teenager"
    else:
        age_genre = "old"

    output_str = f"{name} is a(n) {job} and is in the age genre {age_genre} with an age of {age}."
    print(output_str)

print_user_info("charcey", "instructor", "15")


