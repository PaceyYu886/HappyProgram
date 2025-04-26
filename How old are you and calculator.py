from operator import truth

a=10
b=5

addition=a+b
difference=a-b
multiply=a*b
divide=a/b
print(difference)
print(addition)
print(multiply)
print(divide)


while truth:
     age=int(input('How old are you?input 0 to break'))
     isHappy=False
     if age == 0:
         print('Bye')
         break
     if age>20:
        print('You are old!')
     elif age > 17:
        print('You are going to be old!')
     else:
        print('You are still young')
