def total_sum(myster_int):
    count = 0
    absolute_num = abs(myster_int)
    for num in range(absolute_num + 1):
        count += num
    if myster_int < 0:
        count = count * -1
    return count

mystery_int = 4
print(total_sum(mystery_int))


