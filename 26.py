def format_number(num):
    return "{:,}".format(num)


print(format_number(1000000))
print(format_number(10000))
print(format_number(999999999999))
print(format_number(0))