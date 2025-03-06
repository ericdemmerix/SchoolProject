
import random
def generate_random_string(length):
    letters = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(length):
        result += random.choice(letters)
    return result

print(generate_random_string(10))