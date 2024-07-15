def countdown(num):
    print(num)

    if num <= 0: #base case
        return
    else:
        countdown(num - 1)


countdown(10)