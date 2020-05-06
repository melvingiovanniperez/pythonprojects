def digit_sum(nbr):
    calc = 0
    for n in str(nbr):
            calc += int(n)
    return calc

def is_harshad(nbr):
    calc = digit_sum(nbr)
    if (nbr % calc) == 0:
        return True
    else:
        return False
    

def all_harshad():
    for n in range(1,201):
        harshad = is_harshad(n)
        if harshad == True:
            print(n)
