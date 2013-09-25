import random

rand_num = random.randint(1, 100)

tries = 0
print rand_num

name = raw_input("Howdy, what's your name? ")
print "%s, I'm thinking of a number between 1 and 100.  Try to guess my number." % name

def ord_check(guess):

    for x in guess:
        if ord(x) >= chr(0) and ord(x) <= chr(9):
            return True
    return False

while True:
    guess = raw_input("Your guess? ")

    if ord_check(guess):
        guess = int(guess)

        tries += 1

        if guess > rand_num:
            print "Your guess is too high, try again."
        elif guess < rand_num:
            print "You guess is too low, try again."
        else:
            if tries == 1:
                print "Well done, %s! You found my number in 1 try!" % name
            else:
                print "Well done, %s! You found my number in %d tries!" % (name, tries)
            break
    else:
        print "Please enter a positive whole number."