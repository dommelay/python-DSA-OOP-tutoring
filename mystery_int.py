# FIND SUM OF ALL NUMBERS BETWEEN 0 AND MYSTERY_INT
def total_sum(myster_int):
    count = 0
    absolute_num = abs(myster_int)
    for num in range(absolute_num + 1):
        count += num
    if myster_int < 0:
        count = count * -1
    return count

mystery_int = 3
# print(total_sum(mystery_int))





# BEATS PER MEASURE
def total_beats(beats, measure):
    for num in range(1, measure + 1):
        print(num)
        for num in range(2, beats + 1):
            print(num)

beats = 4
measure = 5
print(total_beats(beats, measure))

def total_beats(beats, measure):
    last_beats = []
    # print 1 2 3 4, add 2, 3, 4 to a list
    for num in range(1, beats + 1):
        if num > 1:
            last_beats.append(num)
        print(num)

    # print all numbers in range measure, starting at 2. Print each item in the beats list [2, 3, 4]
    for num in range(2, measure + 1):
        print(num)
        for beat in range(len(last_beats)):
            print(last_beats[beat])

beats = 4
measure = 5
# print(total_beats(beats, measure))






