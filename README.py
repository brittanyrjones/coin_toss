import random
x = 0
y = 0
#intro meant to be used once
def intro():
    print("----Welcome to heads or tails. Please use,\n")
    print("0 for heads  and   1 for tails\n")
    print(but first...)
#user input and compare to comp. results
def betta_work():
    x = eval(input("----Please select heads(0) or tails(1):"))
    list = [0,1]
    y = random.choice(list)
    if x == y:
        return 0
    else:
        return 1
#user input bet amount
def bet():
    z = eval(input("What would you like to bet?(0-100):"))
    a = 100
    e = a+z
    i = a-z
    if betta_work() == 0:
        print("you won and now have ")
        print(e)
        return e
    else:
        print("you lost and now have ")
        print(i)
        return i
#meant to loop program
def end_game():
    while bet() >= 1:
        bet()
#still need to store variable across loop
intro()
end_game()

