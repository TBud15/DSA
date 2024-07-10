def countdown(i):
    print(i)
    if i <= 0:  #Base case (if this correct recursive function won't run)
        return
    else:   #Recursive case
        countdown(i-1)


countdown(10)