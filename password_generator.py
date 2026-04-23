import random
print("Welcome to the password generator!")
alphabet_pairs = [
    'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 
    'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 
    'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 
    'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z'
]
symbols_list= ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
numbers_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
password =" "
user_choice_of_letters=int(input("How many letters would you like in your password?"))
user_choice_of_symbols=int(input("How many symbols would you like?"))
user_choice_of_numbers=int(input("How many numbers would you like?"))
for letter in range(user_choice_of_letters):
    password+=random.choice(alphabet_pairs)
for symbol in range(user_choice_of_symbols):
    password+=random.choice(symbols_list)
for number in range(user_choice_of_numbers):
    password+=random.choice(numbers_list)
list_of_password=list(password.strip())
random.shuffle(list_of_password)
final_password="".join(list_of_password)
print("Your passsword is :",final_password)
