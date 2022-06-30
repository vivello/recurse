# write a program that prints out the numbers 1 to 100 (inclusive)
# if number is divisible by 3, print Crackle instead of the number
# if it's divisible by 5, print Pop
# if it's divisble by both 3 and 5, print CracklePop

def not_fizzbuzz():
    for i in range(1,101):
        word = ''
        if (i %3) == 0:
            word += 'Crackle'
        if (i % 5) == 0:
            word += 'Pop'
        if len(word) == 0:
            print(i)
        else:
            print(word)


not_fizzbuzz()
