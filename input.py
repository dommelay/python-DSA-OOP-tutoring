
def search_in_files(filename, search_string):
    
    line_numbers = []
    
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if search_string in line:
                line_numbers.append(line_number)
    
    return line_numbers

filename = 'example.txt'
search_string = 'Python'
result = search_in_files(filename, search_string)

print(result)