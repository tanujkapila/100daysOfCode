#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letters_string=""
numbers_string=""
symbols_string=""
for letter in range(1,nr_letters+1):
  #letter_pos=random.randint(0,len(letters)-1)
  #letters_string+=letters[letter_pos]
  letters_string += random.choice(letters)

for number in range(1,nr_numbers+1):
  # number_pos=random.randint(0,len(numbers)-1)
  # numbers_string+=str(numbers[number_pos])
  numbers_string+= random.choice(numbers)

for symbol in range(1,nr_symbols+1):
  # symbol_pos=random.randint(0,len(symbols)-1)
  # symbols_string+=symbols[symbol_pos]
  symbols_string+=random.choice(symbols)

easy_password = letters_string+symbols_string+numbers_string
print(easy_password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password=""
password_string = easy_password
#converting string to list
password_list=list(password_string)
#use shuffle function from random
random.shuffle(password_list)

#concatenating all the character of the shuffled list
for pass_char in password_list:
  password+=pass_char 
print(password)




##Below this is second solution

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
randalphabets=[]
randsymbols=[]
randnumbers=[]
while len(randalphabets)<nr_letters:
  randalphabets+= letters[random.randint(0,len(letters)-1)]

while len(randsymbols)<nr_symbols:
  randsymbols+= symbols[random.randint(0,len(symbols)-1)]

while len(randnumbers)<nr_numbers:
  randnumbers+= numbers[random.randint(0,len(numbers)-1)]

easyPasswordList=randalphabets+randsymbols+randnumbers
print(easyPasswordList)

easyPassword=""
for char in easyPasswordList:
  8easyPassword+=char

print("This is easy password : "+easyPassword)
  


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(easyPasswordList)
hardPassword=""
for char in easyPasswordList:
  hardPassword+=char

print("This is hard password : "+hardPassword)
  
  
