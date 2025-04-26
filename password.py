import random
def youguess():
    e = 0
    f = 1000

    c = random.randint(0,1000)
    while True:
        try:
            number = int(input("guess the number range,"+str(e)+"~"+str(f)))
            if number > c:
                print("less")
                if number < f:
                    f = number
            if number < c:
                print("more")
                if number > e:
                    e = number
            if number == c:
                print("correct!")
                break
        except ValueError:
            print("please input a number, not a word.")



def machineguess():
    AA = 1
    while AA == 1:
        A = int(input("Max=?"))
        B = int(input("Min=?"))
        if A >= 0 and B >= 0:
            D = (A + B)//2
            break

    while True:
        try:
            l=int(input("Is the number "+str(D)+"Yes=1,No=2"))
            if l==1:
                print("Yeah!")
                break
            l = int(input("More or less?more=3,less=4"))
            if l==3:

                B = D+1
                D = (B+A)//2
            else:
                A = D-1
                D = (A+B)//2
        except ValueError:
            print("please input a number, not a word.")



while True:
    try:
        z = int(input("Do you want me guess the number(input 2) or you guess(input 1)?"))
        if z==2:
            machineguess()
        else:
            youguess()
        y=int(input("Do you want to play again?(input 1) or No(input 2)?"))
        if y==1:
            continue
        else:
            print("Goodbye!")
            break
    except ValueError:
        print("please input a number, not a word.")