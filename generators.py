def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements

    yield n

    n += 1
    print('This is printed second')
    yield n


    n += 1
    print('This is printed at last')
    yield n


# a = my_gen()
# next(a)
# next(a)
# next(a)

for item in my_gen():
    print(item)


my_list = [1, 3, 6, 10]
print([x**2 for x in my_list])
print((x**2 for x in my_list))