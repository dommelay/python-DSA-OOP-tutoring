# Write a function called average_word_length that takes as input a string called my_string, and returns as output the average length of the words in the string.

# You should account for consecutive spaces. A string like "Hi   Lucy" is two words with an average length of 3.0 characters.
# - You should not assume the string starts with a letter. A string like "  David" has one word with an average length of 5.0 characters.
# - You should not count punctuation marks toward the length of a word. A string like "Hi, Lucy" has two words with an average length of 3.0 characters: the , after "Hi" does not count as a character in the word. The only punctuation marks you need to handle are these: . , ! ?
# - You may assume the only characters in the string are
#   letters, the punctuation marks listed above, and spaces.
# - If my_string is not a string, you should instead return the string, "Not a string".
# - If there are no words in my_string, you should instead return the string, "No words". This could happen for strings like "" (an empty string) and ".,!?" (a string of only punctuation marks). You may assume that any of these punctuation marks will always be followed by at least one space.

def average_word_length(my_string):

    if not isinstance(my_string, str):
        print('Not a String')
        return 
    
    excluded_chars = [' ', '.', '?', '!', ',']
    words = my_string.split()

    # accepted_words = [''.join(c for c in word if c not in excluded_chars) for word in words if any(c not in excluded_chars for c in word)]

    accepted_words = []
    for word in words:
        if any(c not in excluded_chars for c in word):
            cleaned_word = ''.join(c for c in word if c not in excluded_chars)
            accepted_words.append(cleaned_word)

    if accepted_words:
        total_length = sum(len(word) for word in accepted_words)
        average_length = total_length / len(accepted_words)
        print(average_length)
    else:
        print('No words')

my_string = True   
# my_string = 'Hi, Lucy' 
# my_string = '?!?!?! ... !'
# average_word_length(my_string)

#Write a function called product_code_check. product_code_check. Should take as input a single string. It should return a boolean: True if the product code is a valid code according to the rules below, False if it is not.
# A string is a valid product code if it meets ALL the following conditions:
# - It must be at least 8 characters long.
# - It must contain at least one character from each of the following categories: capital letters, lower-case letters, and numbers.
# - It may not contain any punctuation marks, spaces, or other characters.

def product_code_check(single_string):
    valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    filtered_string = ''.join(c for c in single_string if c in valid_chars)

    has_lowercase = any(c.islower() for c in single_string)
    has_uppercase = any(c.isupper() for c in single_string)
    has_integer = any(c.isdigit() for c in single_string)

    if has_lowercase and has_uppercase and has_integer and filtered_string == single_string and len(single_string) >= 8:
        print(True)
    else: 
        print(False)

# single_string = 'g00dlONGproductCODE'
# single_string = 'fRV53FwSXX663cCd'
# single_string = '2shOrt'
# single_string = 'alll0wercase'
single_string = 'inv4l1d CH4R4CTERS~'
# product_code_check(single_string)

#The Collatz Conjecture is a famous sequence in mathematics proposed by Lothar Collatz. It proceeds as follows: Start with any number. If the number is even, divide it by 2. If the number is odd, triple it and add one. Repeat. Eventually, no matter what number you begin with, this sequence will converge on 1 (and if you continue repeating it, you'll repeat 1-4-2 infinitely).

def collatz(integer):
    total_turns = 0

    while integer != 1:
        if integer % 2 == 0:
            integer = integer // 2
            total_turns += 1
        else:
            integer = integer * 3 + 1
            total_turns += 1
    
    print(total_turns)

# collatz(25)

#Write a function called check_date. check_date should require two positional parameters: a string representing the name of a month, and an integer representing a date. check_date should also have a keyword parameter called is_leap_year, assumed to be False, representing whether or not it's a leap year.
#Return True if the date is a valid calendar date. Return False if it is not. A date may not be a valid calendar date if the month isn't a real month, or if that date does not exist for that month. You can see some examples at the end of this file.
#Remember: 30 days has September, April, June, and November. All the rest have 31, except February, which has 28, until Leap Year gives it 29. You may assume that day will be greater than 0 (you don't need to check negative or zero values for day).

def check_date(month, day, is_leap_year=False):
    month_days = {
        'January': 31,
        'February': 29 if is_leap_year else 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31
    }

    if month not in month_days:
        print('False')
        return False
    if day < 1 or day > month_days[month]:
        print('False')
        return False
    print('True')
    return True

# check_date("January", 31)
# check_date("February", 29, is_leap_year = True)
# check_date("Techtember", 15, is_leap_year = True)

#Write a function called get_numerals. get_numerals should accept one parameter, a string. It should return a string containing only the numerals from the original string: no letters, punctuation marks, or spaces. Remember, numerals have ordinal numbers between 48 ("0") and 57 ("9"). You may use the ord() function to get a letter's ordinal number.
#Your function should be able to handle strings with no numerals (return an empty string) and strings with all numerals (return the original string). You may assume we'll only use regular characters (no emojis, formatting characters, etc.).

def get_numerals(s):
    numerals = ''
    for char in s:
        if '0' <= char <= '9':
            numerals += char
    print(numerals)

def get_numerals_ord(s):
    numerals = ''
    for char in s:
        if 48 <= ord(char) <= 57:
            numerals += char
    print(numerals)

s = 'CS1301'
# s = 'Georgia Institute of Technology'
# s = '8675309'

# get_numerals(s)
# get_numerals_ord(s)

# print(ord('A'))