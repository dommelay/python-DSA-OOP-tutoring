#Write a function called average_word_length that takes as input a string called my_string, and returns as output the average length of the words in the string.
# The only punctuation marks you need to handle are these: . , ! ?
my_string = 4

def average_word_length(my_string):

    if not isinstance(my_string, str):
        print('Not a String')
        return 
    
    excluded_chars = [' ', '.', '?', '!', ',']
    words = my_string.split()
    accepted_words = [''.join(c for c in word if c not in excluded_chars) for word in words if any(c not in excluded_chars for c in word)]

    if accepted_words:
        total_length = sum(len(word) for word in accepted_words)
        average_length = total_length / len(accepted_words)
        print(average_length)
    else:
        print('No words')
    
# average_word_length(my_string)

#Write a function called product_code_check. product_code_check. Should take as input a single string. It should return a boolean:
#True if the product code is a valid code according to the rules below, False if it is not.
#A string is a valid product code if it meets ALL the following conditions:
# - It must be at least 8 characters long.
# - It must contain at least one character from each of the following categories: capital letters, lower-case letters, and numbers.
# - It may not contain any punctuation marks, spaces, or other characters.
single_string = 'g00dlONGproductCODE'

def product_code_check(single_string):
    has_lowercase = any(c.islower() for c in single_string)
    has_uppercase = any(c.isupper() for c in single_string)
    has_integer = any(c.isdigit() for c in single_string)

    if has_lowercase and has_uppercase and has_integer and len(single_string) >= 8:
        print(True)
    else: 
        print(False)

product_code_check(single_string)

